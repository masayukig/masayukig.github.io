---
title: LVM xfs使用時の領域拡張方法
date: '2008-12-14T08:04:00+09:00'
slug: lvm-xfs使用時の領域拡張方法
tags:
- LVM
- PC
- xfs
draft: false
disqus_identifier: 2008-12-14-lvm-xfsshi-yong-shi-noling-yu-kuo-zhang-fang-fa
cover:
  image: /images/covers/uncategorized.jpg
  alt: LVM xfs使用時の領域拡張方法
---

LVMは動的に領域を拡張できて便利なわけですが、ファイルシステムに、
xfsを使用している時の、領域拡張法法を記しておきます。

`# lvresize -L +500M /dev/vg01/lv01# xfs_growfs /mnt/lv01-mountpoint`
xfs\_growfsは、マウントポイントをパラメータにとるので注意。

> \# xfs\_growfs --help
> xfs\_growfs: invalid option -- '-'
> Usage: xfs\_growfs \[options\] mountpoint
>
> Options:
> -d grow data/metadata section
> -l grow log section
> -r grow realtime section
> -n don't change anything, just show geometry
> -I allow inode numbers to exceed 32 significant bits
> -i convert log from external to internal format
> -t alternate location for mount table (/etc/mtab)
> -x convert log from internal to external format
> -D size grow data/metadata section to size blks
> -L size grow/shrink log section to size blks
> -R size grow realtime section to size blks
> -e size set realtime extent size to size blks
> -m imaxpct set inode max percent to imaxpct
> -V print version information
