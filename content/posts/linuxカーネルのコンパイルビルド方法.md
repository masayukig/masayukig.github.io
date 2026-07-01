---
title: Linuxカーネルのコンパイル(ビルド)方法
date: '2008-06-20T23:45:00+09:00'
slug: linuxカーネルのコンパイルビルド方法
tags:
- カーネル
draft: false
disqus_identifier: 2008-06-20-linuxkanerunokonpairubirudofang-fa
cover:
  image: /images/covers/uncategorized.jpg
  alt: Linuxカーネルのコンパイル(ビルド)方法
---

突然だが、Linuxカーネルのコンパイル方法を書いてみる。

とは言っても、とても簡単です。


Linuxのディストリビューションは、とりあえず、Fedora8を基準に書きますが、

他のディストリビューションでも大きな違いはないでしょう。

### 手順：(比較的新しい(2.6.18〜)を想定)

1.  Linuxカーネルをダウンロード
2.  .configファイルの作成
3.  make && sudo make modules\_install && sudo make install
4.  再起動。(再起動時のGRUBの選択画面で、インストールしたカーネルを選ぶ。)

これぐらいでしょうか。それぞれを詳しく述べてみます。

1.  Linuxカーネルをダウンロード
2.  .configファイルの作成
3.  make && sudo make modules\_install && sudo make install
4.  再起動。(再起動時のGRUBの選択画面で、インストールしたカーネルを選ぶ。)
