Title: SQLiteでprepared statementとBLOBを使って構造体を保存(C言語)その2 #sqlite
Date: 2010-06-19 21:25
Author: masayukig
Tags: C言語, Software
Status: published

と言うわけで、[前回](http://www.0r2.info/blog/2010/06/19/sqlite%E3%81%A7prepared-statement%E3%81%A8blob%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E6%A7%8B%E9%80%A0%E4%BD%93%E3%82%92%E4%BF%9D%E5%AD%98c%E8%A8%80%E8%AA%9E/)に続き今回は、前回作成したDBファイルをsqlite3コマンドで見てみます。

以下の様に構造体はBLOBで格納したのですが、最初のメンバーはsqlite3コマンドで見られます。
Oracleではちょっと考えられませんが、この辺がsqliteらしいとこでしょうか。
`$ sqlite3 test.dbSQLite version 3.6.22Enter ".help" for instructionsEnter SQL statements terminated with a ";"sqlite> select * from member;0|Isono Katsuo1|Isono Wakame2|Huguta Tarao3|Huguta Masuo4|Huguta Sazaesqlite> `
