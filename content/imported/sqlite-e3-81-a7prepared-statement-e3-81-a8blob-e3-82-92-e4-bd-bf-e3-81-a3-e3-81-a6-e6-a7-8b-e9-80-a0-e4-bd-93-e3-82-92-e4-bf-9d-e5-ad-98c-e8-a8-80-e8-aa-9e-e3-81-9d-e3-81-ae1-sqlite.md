Title: SQLiteでprepared statementとBLOBを使って構造体を保存(C言語)その1 #sqlite
Date: 2010-06-19 08:28
Author: masayukig
Tags: C++, C言語, DB, 開発, 言語, Software
Status: published

SQLiteのC言語APIを使ってprepared statementで、BLOBを使ってみます。

基本的には、以下のサイトに書いてある方法ですが、日本語で書いてみることにします。  
<http://www.sqlite.org/capi3ref.html#sqlite3_stmt>

1.  sqlite3\_prepare\_v2()(あるいはそれに類するもの)を使って、sqlite3\_stmtのオブジェクトを作る。
2.  sqlite3\_bind\_\*() インターフェースを使ってパラメータに値をBind。
3.  sqlite3\_step()を使ってSQL実行。(sqlite3\_step()は何回でも実行できる)
4.  sqlite3\_reset()を使ってstatementをリセットして、step
    2に戻る。これは何度でもできるし、やらなくても良い。
5.  sqlite3\_finalize()を使ってオブジェクトを破棄する。


というわけで、いきなりサンプルコードw  
便利だなーと思ったのは、sqlite3\_errmsg()関数。dbを引数にすると、

    $ gcc -o sqlite_test sqlite_test.c -lsqlite3
    $ chmod 000 test.db 

と、DBファイルを読み書き出来ないようにして、実行すると、

    $ ./sqlite_test 
    open error:14, unable to open database file

と、何でエラーになったのかが表示されます。

さらに、このDBファイルをsqlite3コマンドで見たときの話は次回のエントリに書きたいと思います。

``` {.c}
#include 
#include 
#include 
#include 

struct human {
  char name[256];
  int age;
  int height;
  int sex;
};

int main(int argc, char *argv[])
{
  struct human human[5] = {
    { "Isono Katsuo", 32, 168, 0 },
    { "Isono Wakame", 29, 158, 1 },
    { "Huguta Tarao", 20, 180, 0 },
    { "Huguta Masuo", 52, 178, 0 },
    { "Huguta Sazae", 48, 161, 1 } };
  sqlite3 *db;
  sqlite3_stmt *dropStmt = NULL;
  sqlite3_stmt *createStmt = NULL;
  sqlite3_stmt *selectStmt = NULL;
  sqlite3_stmt *insertStmt = NULL;
  char *drop_tbl_sql = "drop table member";
  char *create_tbl_sql = "create table member"
    "(id INTEGER PRIMARY KEY,"
    "human BLOB NOT NULL )";
  char *insert_tbl_sql = "INSERT INTO member (id, human) values (?, ?)";
  char *select_tbl_sql = "select human from member where id = ?";
  char *pzTail;
  int rc = 0;
  int exitcode = 0;

  rc = sqlite3_open("test.db", &db);
  //rc = sqlite3_open(":memory:", &db);
  if (rc != SQLITE_OK) {
    printf("open error:%d, %s\n", rc, sqlite3_errmsg(db));
    exitcode = 1;
    goto end;
  }

  /* cleanup. ignore error. */
  sqlite3_prepare_v2(db, drop_tbl_sql, -1, &dropStmt, NULL);
  sqlite3_step(dropStmt);

  rc = sqlite3_prepare_v2(db, create_tbl_sql, -1, &createStmt, NULL);
  if (rc != SQLITE_OK) {
    printf("create error:%d, %s\n", rc, sqlite3_errmsg(db));
    exitcode = 1;
    goto end;
  }
  rc = sqlite3_step(createStmt);
  if (rc != SQLITE_DONE) {
    printf("create error:%d, %s\n", rc, sqlite3_errmsg(db));
    exitcode = 1;
    goto end;
  }

  rc = sqlite3_prepare_v2(db, insert_tbl_sql, -1, &insertStmt, NULL);
  if (rc != SQLITE_OK) {
    printf("insert error:%d, %s\n", rc, sqlite3_errmsg(db));
    exitcode = 1;
    goto end;
  }
  rc = sqlite3_prepare_v2(db, select_tbl_sql, -1, &selectStmt, NULL);
  if (rc != SQLITE_OK) {
    printf("select error:%d, %s\n", rc, sqlite3_errmsg(db));
    exitcode = 1;
    goto end;
  }

  int i = 0;
  for (i = 0; i < 5; i++) {
    sqlite3_reset(insertStmt);
    sqlite3_bind_int(insertStmt, 1, i);
    sqlite3_bind_blob(insertStmt, 2, &human[i], sizeof(struct human), SQLITE_STATIC);
    rc = sqlite3_step(insertStmt);
    if (rc != SQLITE_DONE) {
      printf("insert error:%d, %s\n", rc, sqlite3_errmsg(db));
      exitcode = 1;
      goto end;
    }
  }

  printf("-------------------------------------\n");
  for (i = 0; i < 5; i++) {
    sqlite3_reset(selectStmt);
    sqlite3_bind_int(selectStmt, 1, i);
    rc = sqlite3_step(selectStmt);
    //printf("select result:%d\n", rc);
    if (rc == SQLITE_ROW) {
      struct human *t = (struct human*)sqlite3_column_blob(selectStmt, 0);
      printf("ID: %d\n\t name: %s\n\t age: %d\n\t height: %d\n\t sex: %s\n",
       i, t->name, t->age, t->height, t->sex == 0 ? "M" : "F");
      printf("-------------------------------------\n");
    }
  }

 end:
  sqlite3_finalize(selectStmt);
  sqlite3_finalize(insertStmt);
  sqlite3_finalize(createStmt);
  sqlite3_finalize(dropStmt);
  
  return exitcode;
}
```
