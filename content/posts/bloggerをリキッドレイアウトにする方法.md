---
title: Bloggerをリキッドレイアウトにする方法
date: '2012-03-23T21:57:00+09:00'
slug: bloggerをリキッドレイアウトにする方法
tags:
- blogger
- customize
- html
draft: false
disqus_identifier: 2012-03-23-bloggerworikitsudoreiautonisurufang-fa
---

Bloggerを使い始めたのですが、「動的レイアウト」以外は、横幅固定のテンプレートしか
無い様で、若干ガッカリでした。

で、ググってみたところ、

[bloggerでリキッドレイアウト（横幅可変）にするには](http://hibilig.blogspot.jp/2011/06/blogger.html)

> HTMLの編集で「content.width」を設定している行を根こそぎ削除。 

というのが見つかったので、やってみました。


    「テンプレート」-&gt; 「HTMLの編集」を選択



    警告が出ますが、無視して「続行」



    「content.width」がある行を根こそぎ、コメントアウト。プレビューして問題なければテンプレートを保存します。


以上。やってみれば、簡単でした。
