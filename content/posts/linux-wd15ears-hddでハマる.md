---
title: Linux WD15EARS HDDでハマる
date: '2010-04-14T05:28:00+09:00'
slug: linux-wd15ears-hddでハマる
tags:
- HDD
- PC
draft: false
disqus_identifier: 2010-04-14-linux-wd15ears-hdddehamaru
---

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
