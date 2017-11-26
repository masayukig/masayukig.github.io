Title: Play framework で Scala を 試してみる
Date: 2011-06-18 05:19
Author: masayukig
Tags: play, scala
Status: published

[![Scala
Play](http://farm4.static.flickr.com/3010/5843344046_490f31de82.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5843344046/ "Scala Play")

[Typesafe.com](http://typesafe.com/)のページを見ていたところ、右下に、

[![for
Play](http://farm4.static.flickr.com/3102/5843344316_86b19cf8ae_m.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5843344316/ "for Play")

の、アイコン＆リンクがあるのに気づき、クリックしたところ、前述の[scala.playframework.org](http://scala.playframework.org/)の
Play framework Scala ページにたどり着きました。  
なんだか面白そうなので、試してみることにしました。

バイナリダウンロード  
<http://www.playframework.org/download>より、Play
frameworkバイナリをダウンロードします。

[![Play
download](http://farm6.static.flickr.com/5075/5843344188_57d2960417.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5843344188/ "Play download")

ダウンロードファイル解凍

    $ unzip Downloads/play-1.2.1.zip 
    Archive:  Downloads/play-1.2.1.zip
    Play! 1.2.1
    (省略)

リンク作成

    $ ln -s play-1.2.1 play-latest

環境変数PATHに追加  
以下の様なものを.bashrcに追加し、反映させます。

    $ cat ~/.bashrc 
    export PLAY_HOME=${HOME}/play-latest
    export PATH=${PATH}:${PLAY_HOME}
    $ . ~/.bashrc

テスト

    $ play -version
    ~        _            _ 
    ~  _ __ | | __ _ _  _| |
    ~ | '_ \| |/ _' | || |_|
    ~ |  __/|_|\____|\__ (_)
    ~ |_|            |__/   
    ~
    ~ play! 1.2.1, http://www.playframework.org
    ~
    ~ Usage: play cmd [app_path] [--options]
    ~ 
    ~ with,  new      Create a new application
    ~        run      Run the application in the current shell
    ~        help     Show play help
    ~
    ~ Invalid command: -version
    ~

問題無し。

play scalaインストール

    $ play install scala
    ~        _            _ 
    ~  _ __ | | __ _ _  _| |
    ~ | '_ \| |/ _' | || |_|
    ~ |  __/|_|\____|\__ (_)
    ~ |_|            |__/   
    ~
    ~ play! 1.2.1, http://www.playframework.org
    ~
    ~ Will install scala-0.9
    ~ This module is compatible with: 1.2
    ~ Do you want to install this version (y/n)? y
    ~ Installing module scala-0.9...
    ~
    ~ Fetching http://www.playframework.org/modules/scala-0.9.zip
    ~ [--------------------------100%-------------------------] 28983.6 KiB/s   
    ~ Unzipping...
    ~
    ~ Module scala-0.9 is installed!
    ~ You can now use it by adding it to the dependencies.yml file:
    ~
    ~ require:
    ~     play -> scala 0.9
    ~

サンプルアプリ作成

    $ play new myScalaWebapp --with scala
    ~        _            _ 
    ~  _ __ | | __ _ _  _| |
    ~ | '_ \| |/ _' | || |_|
    ~ |  __/|_|\____|\__ (_)
    ~ |_|            |__/   
    ~
    ~ play! 1.2.1, http://www.playframework.org
    ~
    ~ The new application will be created in /Users/igawa/src/myScalaWebapp
    ~ What is the application name? [myScalaWebapp] 
    ~
    ~ Resolving dependencies using /Users/igawa/src/myScalaWebapp/conf/dependencies.yml,
    ~
    ~     play->scala 0.9 (from playLocalModules)
    ~
    ~ Some dependencies have been evicted,
    ~
    ~ play 1.2 is overriden by play 1.2.1
    ~
    ~ Installing resolved dependencies,
    ~
    ~   modules/scala-0.9 -> /Users/igawa/play-1.2.1/modules/scala-0.9
    ~
    ~ Done!
    ~
    ~ OK, the application is created.
    ~ Start it with : play run myScalaWebapp
    ~ Have fun!
    ~
    $ find myScalaWebapp -type f
    myScalaWebapp/app/controllers.scala
    myScalaWebapp/app/views/Application/index.html
    myScalaWebapp/app/views/errors/404.html
    myScalaWebapp/app/views/errors/500.html
    myScalaWebapp/app/views/main.html
    myScalaWebapp/conf/application.conf
    myScalaWebapp/conf/dependencies.yml
    myScalaWebapp/conf/messages
    myScalaWebapp/conf/routes
    myScalaWebapp/modules/scala-0.9
    myScalaWebapp/public/images/favicon.png
    myScalaWebapp/public/javascripts/jquery-1.5.2.min.js
    myScalaWebapp/public/stylesheets/main.css
    myScalaWebapp/test/Application.test.html
    myScalaWebapp/test/data.yml
    myScalaWebapp/test/Tests.scala

実行

    $ cd myScalaWebapp/
    $ play run
    ~        _            _ 
    ~  _ __ | | __ _ _  _| |
    ~ | '_ \| |/ _' | || |_|
    ~ |  __/|_|\____|\__ (_)
    ~ |_|            |__/   
    ~
    ~ play! 1.2.1, http://www.playframework.org
    ~
    ~ Ctrl+C to stop
    ~ 
    Listening for transport dt_socket at address: 8000
    04:57:23,101 INFO  ~ Starting /Users/igawa/src/myScalaWebapp
    04:57:23,107 INFO  ~ Module scala is available (/Users/igawa/play-1.2.1/modules/scala-0.9)
    04:57:25,615 WARN  ~ You're running Play! in DEV mode
    04:57:25,720 INFO  ~ Listening for HTTP on port 9000 (Waiting a first request to start) ...
    04:57:40,996 INFO  ~ Application 'myScalaWebapp' is now started !

アプリケーションの起動までに結構時間がかかるので注意。  
ブラウザでhttp://localhost:9000/にアクセスし、以下の画面が表示されれば成功。

[![Play Scala sample
application](http://farm6.static.flickr.com/5319/5843420398_cd2d48d759.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5843420398/ "Play Scala sample application")

若干モディファイ  
自動的に変更が反映されるのか？を  
<http://localhost:9000/@documentation/modules/scala/hello-world>  
のチュートリアルを参考に確認してみます。

動いた。  
チュートリアルにはまだまだ続きがありますが、続きはまた気が向いたらやります
:-)
