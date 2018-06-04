Title: Challenging OpenStack on Nexus 7... but failed #openstack #nexus7
Date: 2013-01-02 10:47
Author: masayukig
Category: openstack
Tags: nexus7
Status: published
Attachments: 2013/01/93fbd-dashboard.png, 2013/01/21730-errorlog.png

[Nexus
7にUbuntuをインストールできる](https://wiki.ubuntu.com/Nexus7/Installation)というのをみて、  
「もしかしたらOpenStackも動くかも？！」と思ってやってみたのですが、

あえなく撃沈。。


[![picture](https://masayukig.files.wordpress.com/2013/01/93fbd-dashboard.png)
](https://masayukig.files.wordpress.com/2013/01/93fbd-dashboard.png)



[![picture](https://masayukig.files.wordpress.com/2013/01/21730-errorlog.png)
](https://masayukig.files.wordpress.com/2013/01/21730-errorlog.png)




具体的には、以下のような感じでインストールを行った。

1.  DevStackのインストール
2.  stack.shの実行
3.  Horizonの起動を確認
4.  Dashboardへアクセス成功(だいぶ動作がとろいが)
5.  いきなりDashboardからインスタンス起動
6.  → エラー
7.  ログ確認(nova-compute)
8.  最終的には起動時に以下の理由(ログ)で、nova-computeの起動に失敗している模様

<!-- -->

    2013-01-02 06:10:42 TRACE nova libvirtError: internal error Cannot find suitable emulator for armv7l

ARM＆libvirtdの対応が行われていないらしい。  
libvirtのソースも多少読んだが、大枠の構造を理解してないので直せる力量をつけるにはまだまだ時間が掛かりそう。

このままだとさすがにNexus7使いづらいので、[Dual
Boot](https://wiki.ubuntu.com/Nexus7/Installation#Having_both_Android_and_Ubuntu_installed_for_dual_boot)できるようにしてから  
再挑戦しようとおもいます。
