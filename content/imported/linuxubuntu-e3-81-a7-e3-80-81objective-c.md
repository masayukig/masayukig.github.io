Title: Linux(Ubuntu)で、Objective-C
Date: 2009-08-15 05:54
Author: masayukig
Tags: 開発, Linux, Objective-C, Software
Status: published

iPhoneアプリを作るなら、Objective-Cという言語を知っておく必要が  
ありそうなので、とりあえず、LinuxでObjective-Cをやってみる。  
参考にしている書籍は、以下。  
<http://rcm-jp.amazon.co.jp/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=hughundercons-22&o=9&p=8&l=as1&m=amazon&f=ifr&md=1X69VDGQCMF7Z30FM082&asins=4797346809>  
私は、とりあえず、図書館で借りました。  
が、図書館に無かったり、近くに図書館が内容な場合は、上記からご購入ください
:-)

Apple製品専用言語なのかと思ったが、ググったら、Linuxでも動きそうだったので、  
挑戦してみる。

以下、その内容。  
[]{#more}  
まずは、Objective-Cの環境をインストール。  
[Linux で Objective C
を走らせてみた](http://d.hatena.ne.jp/elm200/20080426/1209211127)  
の記事を参照して、以下の様にインストール。

    $ sudo aptitude install gobjc
    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています
    状態情報を読み取っています... 完了
    拡張状態情報を読み込んでいます
    パッケージの状態を初期化しています... 完了
    拡張状態情報を書き込んでいます... 完了
    以下の新規パッケージがインストールされます:
      gobjc gobjc-4.3{a} libobjc2{a}
    0 個のパッケージを更新、 3 個を新たにインストール、 0 個を削除予定、1 個が更新されていない。
    3700kB のアーカイブを取得する必要があります。 展開後に 9478kB のディスク領域が新たに消費されます。
    先に進みますか? [Y/n/?] Y
    拡張状態情報を書き込んでいます... 完了
    取得:1 http://jp.archive.ubuntu.com jaunty/main libobjc2 4.3.3-5ubuntu4 [160kB]
    取得:2 http://jp.archive.ubuntu.com jaunty/main gobjc-4.3 4.3.3-5ubuntu4 [3538kB]
    取得:3 http://jp.archive.ubuntu.com jaunty/main gobjc 4:4.3.3-1ubuntu1 [894B]
    3700kB を 2s 秒でダウンロードしました (1552kB/s)
    未選択パッケージ libobjc2 を選択しています。
    (データベースを読み込んでいます ... 現在 250930 個のファイルとディレクトリがインストールされています。)
    (.../libobjc2_4.3.3-5ubuntu4_amd64.deb から) libobjc2 を展開しています...
    未選択パッケージ gobjc-4.3 を選択しています。
    (.../gobjc-4.3_4.3.3-5ubuntu4_amd64.deb から) gobjc-4.3 を展開しています...
    未選択パッケージ gobjc を選択しています。
    (.../gobjc_4%3a4.3.3-1ubuntu1_amd64.deb から) gobjc を展開しています...
    libobjc2 (4.3.3-5ubuntu4) を設定しています ...

    gobjc-4.3 (4.3.3-5ubuntu4) を設定しています ...
    gobjc (4:4.3.3-1ubuntu1) を設定しています ...
    libc6 のトリガを処理しています ...
    ldconfig deferred processing now taking place
    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています
    状態情報を読み取っています... 完了
    拡張状態情報を読み込んでいます
    パッケージの状態を初期化しています... 完了
    拡張状態情報を書き込んでいます... 完了

で、まずは、お約束Hello Worldからw（インターネットはどれくらい"Hello
World"であふれているのだろうか..）

test1.m というファイル名で以下のソースを記述。

``` {.cpp}
#import 

int main() {
        printf("Hello World!\n");
        return 0;
}
```

で、以下のコマンドを実行。

    $ gcc test1.m -lobjc
    $ ./a.out
    Hello World!

って、これじゃ、普通のC言語と変わらない！w

というわけで、インターフェース、クラスを使ってみる。

``` {.cpp}
#import 

@interface Human : Object
{
        int age;
}
-setAge :(int) a;
-(int) getAge;
@end

@implementation Human
-setAge :(int) a { age = a; return self; }
-(int) getAge { return age; }
-(void) sayAge { printf("I'm %d years old.\n", age); }
@end

int main() {
        id human = [Human alloc];
        [human setAge: 23];
        [human sayAge];

        return 0;
}
```

で、コンパイル＆実行すると、

    $ gcc test1.m -lobjc
    $ ./a.out
    I'm 23 years old.

インターフェースにないメソッド(メッセージ？)を、実装で追加しても良いらしい。。  
というわけで、なんとなく雰囲気をつかんだので、今のところは、まぁ良しとします。

参考サイト：

-   <http://d.hatena.ne.jp/elm200/20080426/1209211127>
-   <http://d.hatena.ne.jp/ntaku/20080802/1217603923>

