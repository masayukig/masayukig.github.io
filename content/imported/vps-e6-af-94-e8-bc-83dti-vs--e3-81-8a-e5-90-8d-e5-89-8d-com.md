Title: VPS比較(DTI vs お名前.com)
Date: 2010-07-17 22:27
Author: masayukig
Tags: お名前.com, DTI, VPS
Status: published

現在、このサイトは[お名前.comのVPS](http://px.a8.net/svt/ejp?a8mat=1NUO6C+EAG2I+50+35IPWY)![](http://www13.a8.net/0.gif?a8mat=1NUO6C+EAG2I+50+35IPWY){width="1"
height="1"}上で動作しているが、  
[DTIのServersMan
VPS](http://dream.jp/vps/)が期間限定ながら無料で試せるようだったので、  
試してみた。

結論から言うと、お名前.comの方が私は好みです。  
お名前.com
VPS：x86\_64カーネル、CPU:16コア、(下記の単純なベンチマークで)２倍程度早い  
DTI VPS：x86カーネル、CPU:2コア、お名前.comの半分程度のスピード

というわけで、お名前.comのVPSを使ってみようと思った方は、  
下記のリンクから、どうぞお申し込みください。  
[  
![](http://www29.a8.net/svt/bgt?aid=100528356024&wid=002&eno=01&mid=s00000000018019040000&mc=1){width="350"
height="80"}](http://px.a8.net/svt/ejp?a8mat=1NUO6C+EAG2I+50+35CXKX)![](http://www.0r2.info/blog/wp-content/uploads/2011/01/01.gif){width="1"
height="1"}

以下、計測ログ等。

お名前.comサーバ

    $ grep processor /proc/cpuinfo |wc -l
    16
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m0.640s
    user    0m0.187s
    sys     0m0.453s
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m0.641s
    user    0m0.187s
    sys     0m0.454s
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m0.780s
    user    0m0.359s
    sys     0m0.421s
    $ uname -a
    Linux 0r2.info 2.6.18-028stab068.9 #1 SMP Tue Mar 30 17:22:31 MSD 2010 x86_64 x86_64 x86_64 GNU/Linux
    $ cat /etc/redhat-release 
    CentOS release 5.5 (Final)

DTI VPS

    $ grep processor /proc/cpuinfo |wc -l
    2
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m1.485s
    user    0m1.065s
    sys     0m0.382s
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m1.499s
    user    0m1.074s
    sys     0m0.383s
    $ time for ((i=0; i<100000; i++)); do :; done

    real    0m1.488s
    user    0m1.045s
    sys     0m0.405s

    $ 
    $ uname -a
    Linux localhost 2.6.18-194.3.1.el5.028stab069.6 #1 SMP Wed May 26 18:31:05 MSD 2010 i686 i686 i386 GNU/Linux
    $ cat /etc/redhat-release 
    CentOS release 5.5 (Final)
