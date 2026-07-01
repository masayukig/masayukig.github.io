---
title: gpsPhoto.plでGeoタグ付け
date: '2008-11-01T18:17:00+09:00'
slug: gpsphotoplでgeoタグ付け
tags:
- 画像
- GPS
- tips
- 写真
draft: false
disqus_identifier: 2008-11-01-gpsphotopldegeotagufu-ke
---

[gpsPhoto.pl](http://www.carto.net/projects/photoTools/gpsPhoto/)というのを使うと、geoタグをつけることが出来る。

`$ gpsPhoto.pl --dir JPEGファイルがあるディレクトリ --gpsfile GPSファイルパス.gpx --maxtimediff 500 --timeoffset -32400`

-32400=GMTからの時差。(JSTなら-0900なので-60\*60\*9)

必要なもの：
[gpsPhoto.pl](http://www.carto.net/projects/photoTools/gpsPhoto/)
Image-ExifTool-7.51(CPANでインストール可能)
...?

参考URL:

-   <http://www.tamichan.com/lost+found/gps.html>
-   <http://d.hatena.ne.jp/a10i/20080220/1203519480>
