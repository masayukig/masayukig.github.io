Title: Linux WD15EARS HDDでハマる
Date: 2010-04-14 05:28
Author: masayukig
Tags: HDD, PC
Status: published

WD15EARSというHDDでは、
「Advanced Format Technology」
というのを採用していて、セクタが4KBになっているそうです。

で、このHDDへLinuxをインストールして使ったところ、
「書き込みがやたら遅い」
という問題が発生しました。

[http://community.wdc.com/t5/Desktop/Problem-with-WD-Advanced-Format-drive-in-LINUX-WD15EARS/td-p/6395
](http://community.wdc.com/t5/Desktop/Problem-with-WD-Advanced-Format-drive-in-LINUX-WD15EARS/td-p/6395)
の投稿を参考に、

    # fdisk -H 224 -S 56 /dev/sda

として、
あとは、通常どおり、パーティションを区切りました。
(面倒なので「/」とswapの二つだけにしました。)
これで、ようやく正常な速度になりました。
