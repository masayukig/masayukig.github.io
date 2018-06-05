Title: Mac で Scala と Lift を使ってみる(2) Cloud Foundry編
Date: 2011-06-11 06:00
Author: masayukig
Tags: cloudfoundry, lift, Mac, scala
Status: published

「Mac で Scala と Lift を使ってみる」の2回目

今度は、作成したアプリをCloud Foundryへpushしてみます。
つい最近、[Cloud
Foundry](http://cloudfoundry.com/)が[Scala-Liftに対応した](http://blog.cloudfoundry.com/post/6109591023/cloud-foundry-now-supporting-scala)ので可能になりました。

今度は、「ゆろよろ日記」さんのサイト：
<http://d.hatena.ne.jp/yuroyoro/20080808/1218168453>
記述を参考にしました。

1.  アプリを作成

        $ mvn archetype:create -U  -DarchetypeGroupId=net.liftweb  -DarchetypeArtifactId=lift-archetype-basic -DarchetypeVersion=0.9  -DremoteRepositories=http://scala-tools.org/repo-releases  -DgroupId=org.orzlabs -DartifactId=hello-lift

2.  パッケージ作成

        $ cd hello-lift/
        $ mvn package
        $ ls -l target

    warファイルが作成されていることを確認します。

3.  Cloud Foundryへpush
   以下手順からは、事前に、[Cloud
    Foundry](http://cloudfoundry.com/)にて、sign
    upを済ませておく必要があります。

        $ gem install vmc (vmcをインストールしてない場合)
        $ vmc target api.cloudfoundry.com
        $ vmc login
        $ vmc push --path target/
        (以下の内容を聞かれるので、適当に入力)
        Application Name: xxxxx (アプリケーション名。好きな様につけて良い。)
        Application Deployed URL: 'xxxxx.cloudfoundry.com'? (デフォルトで良ければ単にEnter。アクセスするURLを指定する)
        Detected a Java Web Application, is this correct? [Yn]: (Enter)
        Memory Reservation [Default:512M] (64M, 128M, 256M, 512M or 1G) (デフォルトで良ければ単にEnter)
        Creating Application: OK
        Would you like to bind any services to 'nano'? [yN]: (DBを使用したければy。今回はとりあえず不要なのでN)
        Uploading Application:
          Checking for available resources: OK
          Processing resources: OK
          Packing application: OK
          Uploading (7M): OK
        Push Status: OK
        Staging Application: OK
        Starting Application: OK

4.  Webブラウザでアクセス

    [![Scala-Lift app push to
    CloudFoundry](http://farm4.static.flickr.com/3258/5819360632_a510807843.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5819360632/ "Scala-Lift app push to CloudFoundry")

    これだけ！。超絶簡単にScala-Liftアプリを公開できる！

TODO:

-   Cloud Foundryでの(DB)サービスの利用
-   Scala学習
-   Lift学習
-   もっとまともなアプリ作成

