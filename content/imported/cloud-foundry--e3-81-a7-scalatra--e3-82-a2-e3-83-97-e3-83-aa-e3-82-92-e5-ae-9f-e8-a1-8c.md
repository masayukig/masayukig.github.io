Title: Cloud Foundry で Scalatra アプリを実行
Date: 2011-07-02 05:43
Author: masayukig
Tags: cloud, scala, scalatra, Software
Status: published

[![](https://lh3.googleusercontent.com/-FMIXumcTAV0/Tjr6wfSrWEI/AAAAAAAAg6M/d80dUsZSc_A/s800/5892056768_b3f93f8618_o.png){width="269"
height="151"}](https://picasaweb.google.com/lh/photo/yZtdpG7qkZc_OfWy78PCPw?feat=embedwebsite)

Cloud Foundry で [Scalatra](https://github.com/scalatra/scalatra)
アプリを実行してみます。  
Scalatra
自体については、[ググって](http://www.google.co.jp/search?q=scalatra)ください。
:-P

1.  ~~sbtをインストール  
   インストール方法は、[Mac で Scala と Lift を使ってみる(1)
    インストール編](http://b.0r2.info/?p=1508)に記載した通りです。  
   Linuxならばapt-getやyum等でインストールできるかもしれません。  
   Windowsはわかりませんw~~  
   下記のgit cloneでsbtも取得できるので不要
2.  sbtアプリ作成＆テスト実行  
   [Quick start (SBT
    0.7.x)](https://github.com/scalatra/scalatra)に書かれている方法を実行します。

        $ git clone git://github.com/scalatra/scalatra-sbt-prototype.git my-app
        $ cd my-app
        $ ./sbt
        > update
        > jetty-run
        > ~prepare-webapp

    で、あとは、<http://localhost:8080/>
    へアクセスすれば、上記の様な画面が表示されると思います。

3.  Cloud Foundryへpush

        $ sbt package
        $ vmc push --path target/scala_2.8.1
        Application Name: 好きなアプリケーション名を入力
        Application Deployed URL: 'アプリケーション名.cloudfoundry.com'? 
        Detected a Java Web Application, is this correct? [Yn]: 
        Memory Reservation [Default:512M] (64M, 128M, 256M, 512M or 1G) 
        Creating Application: OK
        Would you like to bind any services to '好きなアプリケーション名'? [yN]: 
        Uploading Application:
          Checking for available resources: OK
          Processing resources: OK
          Packing application: OK
          Uploading (9K): OK   
        Push Status: OK
        Staging Application: OK                                                         
        Starting Application: OK                                                        

    とすれば、warファイルが作成され、Cloud Foundryへpushできますが、  
   １点注意点があります。デフォルトでは、scala-compiler.jarがwarファイルに含まれないらしく、  
   このwarファイルをvmc pushしても実行時にエラーとなります。  
   <http://d.hatena.ne.jp/fits/20110521/1305942644>  
   というわけで、以下の修正を加えた後、

        $ git diff
        diff --git a/project/build/MyProject.scala b/project/build/MyProject.scala
        index 0b8e9e0..c5fc24a 100644
        --- a/project/build/MyProject.scala
        +++ b/project/build/MyProject.scala
        @@ -15,6 +15,9 @@ class MyProject(info: ProjectInfo) extends DefaultWebProject(info) {
           // http://groups.google.com/group/simple-build-tool/msg/1f17b43807d06cda
           override def testClasspath = super.testClasspath +++ buildCompilerJar
         
        +  // http://d.hatena.ne.jp/fits/20110521/1305942644
        +  override def webappClasspath = super.webappClasspath +++ buildCompilerJar
        +
           val sonatypeNexusSnapshots = "Sonatype Nexus Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots"
           // For Scalate
           val fuseSourceSnapshots = "FuseSource Snapshot Repository" at "http://repo.fusesource.com/nexus/content/repositories/snapshots"

        $ vmc push

    します。

4.  Cloud Foundryで動作確認  
   http://好きなアプリケーション名.cloudfoundry.com/へアクセスし、  
   「hello to
    Scalate」リンクをクリックして、以下の画面が表示されれば成功です。

    [![](https://lh5.googleusercontent.com/-DXDGAlUBxGs/Tjr6wX1tfBI/AAAAAAAAg6M/KDKduMtW-1k/s288/5892086172_ca7c68dbd7_o.png){width="288"
    height="105"}](https://picasaweb.google.com/lh/photo/ZGgEZWkKrKmPl5X89-p1cQ?feat=embedwebsite)


