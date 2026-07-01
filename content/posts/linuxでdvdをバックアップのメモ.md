---
title: LinuxでDVDをバックアップのメモ
date: '2009-01-30T12:14:00+09:00'
slug: linuxでdvdをバックアップのメモ
categories:
- Uncategorized
draft: false
disqus_identifier: 2009-01-30-linuxdedvdwobatsukuatsupunomemo
cover:
  image: /images/covers/uncategorized.jpg
  alt: LinuxでDVDをバックアップのメモ
---

DVDは、結構長期間保存がきくが、いつどうなるか分かったものではないので、
バックアップをするためのメモです。

私の趣味で(というかWindows環境が手元にないので)LinuxでDVDをバックアップしたときのメモです。

\$ sudo apt-get install dvdbackup
バックアップしたいDVDディスクを挿入。
\$ cd バックアップ先ディレクトリ; dvdbackup -M -v

これでOK。

さらに、ISOイメージにしたい場合には、genisoimageというソフトを使うらしいが、
まだ私は使っていない。
