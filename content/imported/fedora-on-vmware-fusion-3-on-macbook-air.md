Title: Fedora on VMWare Fusion 3 on MacBook Air
Date: 2011-02-07 05:21
Author: masayukig
Tags: Apple, Fedora, Mac, OS, partition, PC, vmware, vmware fusion
Status: published

[![Fedora14 on VMware Fusion on MacBook
Air](http://farm6.static.flickr.com/5297/5422904210_999389cb72_m.jpg)
](http://www.flickr.com/photos/masayun/5422904210/ "Fedora14 on VMware Fusion on MacBook Air by masayukig, on Flickr")

[先日のエントリー](http://www.0r2.info/blog/2011/02/06/macbook-air%E3%81%ABlinuxfedora%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/)で、MacBook
AirにFedoraをインストールしたことを書きましたが、  
やはり、Mac OS X上からもLinuxを使いたいので試行錯誤して、  
VMWare Fusion 3上から使うことができました。

以下、その方法。

まずは、普通に別パーティション(私の場合/dev/disk0s3(Mac表記))へFedora14(x86\_64)をインストール。  
なお、swapパーティションは、とりあえず作らない。必要なら後からswapファイルを作ってそれをswapにする。  
(無駄なディスク領域は作りたくないので)  
また、MacのUSキーボードの場合、キーボードは無印の「アメリカ合衆国」を選んだ方がいいようだ。  
「日本語入力するから国際版(International)」かな？と思ってそれを選んだら、  
「\~, \`, ", '」  
などのキーがまともに入力できなくなってしまいました。

なお、設定は/etc/sysconfig/keyboardの

    KEYBOARD="acentos-us"

となっているところを

    KEYBOARD="us"

とすれば、普通のUSキーボードになるようです。  
2011/02/08追記：  
==========  
どうやらこれではダメだったみたいです。。もうちょっと解決策を探してみます。  
==========

で、肝心の別パーティションのディスクイメージを使用してのLinux起動ですが、  
以下の手順でできました。  
なお、<http://fearandloath.us/vmware-fusion-bootcamp-partition.html>のサイトの情報を  
参考（というかほぼそのまま）にさせてもらいました。

    $ cd "/Library/Application Support/VMware Fusion/"
    $ ./vmware-rawdiskCreator print /dev/disk0
    Nr      Start       Size Type Id Sytem                   
    -- ---------- ---------- ---- -- ------------------------
     1          1     409639 BIOS EE Unknown
     2     409640  196982744 BIOS AF HFS+
     3  197654528   39321600 BIOS 83 Linux
    (という感じの出力がされるので、インストールするパーティションの「Nr」を確認しておく
    私の場合は「３」)
    $ ./vmware-rawdiskCreator create /dev/disk0 3 /Users/igawa/Documents/Virtual\ Machines.localized/rawfedora_x86_64.vmwarevm/bootcamp_partition ide
    $ vim /Users/igawa/Documents/Virtual\ Machines.localized/rawfedora_x86_64.vmwarevm/rawfedora_x86_64.vmx
    ======
    ide0:0.present = "TRUE"
    ide0:0.fileName = "bootcamp_partition.vmdk"
    ======
    を適当なところに追加 or 置換する。

これでOKでした。
