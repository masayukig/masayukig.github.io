---
title: 初めてのOpenStackリポジトリ追加
date: '2016-12-17T00:00:00+09:00'
slug: adding-a-new-repo-to-openstack
categories:
- Work
tags:
- work
- oss
- openstack
- development
draft: false
disqus_identifier: 2016-12-17-adding-a-new-repo-to-openstack
---

これは、 [OpenStack Advent Calendar 2016](http://www.adventar.org/calendars/1739) のエントリです。


先日、OpenStack に新たなリポジトリを追加したので、そのときに感じたことや経験を共有してみたいと思います。

## ナニを追加したのか？

* [coverage2sql](https://launchpad.net/coverage2sql)

[Coverage.py](http://coverage.readthedocs.io/) によって生成される、単体テストなどの coverage データを、データベースに時系列な
データとして保持するための小さなツールです。最終的には、 [openstack-health](https://launchpad.net/openstack-health) と連携して、
単体テストの coverage 推移を表示したいと考えてます。もちろん、:

```
「カバレッジ100%だったら品質が良いわけじゃないよね？」
```
という話はあります。しかし、少なくとも、カバレッジ率が意図せず下落傾向な場合は、問題がある可能性があり、
それを知ることができるというのが重要と考えています。

このような性質のコンポーネントのため、独立したプロジェクトではなく、 [Quality Assurance](https://wiki.openstack.org/wiki/QA)
プログラム配下のリポジトリとして追加しました。このようなリポジトリを追加することはなかなか無いこととは
思いますが、新しいリポジトリを追加した経験は、もしかしたら誰かの役に立つかもしれないと思い、共有します。

なお、似たようなツールとして [subunit2sql](https://launchpad.net/subunit2sql) と言うものがあるのですが、それにインスパイアされて作りました。




## 新しいリポジトリの追加方法

[Project Creator's Guide](http://docs.openstack.org/infra/manual/creators.html) をまずは読みます。ステップ・バイ・ステップで丁寧に説明された
ドキュメントです。このとおりやっていれば、あまり迷うことも無いと思います。


大きな流れとしては、

# Launchpad 設定
# PyPI 設定
# openstack-infra/project-config, openstack/governance 設定
# レビュー待ち＆対応
# 新しいリポジトリ作成（最初でもOK）
# Gateジョブ実行動作確認
# 初期バージョンリリース
# ...

という感じになると思います。


## ドキュメントに書いてないこと

ドキュメントのとおりに進んでいって、特に困ったことにはならなかったので、あまりないですね。強いて言えば、

* Launchpadの登録で、少しだけ記述が現状とあってない部分があった。

  * -> [ドキュメントの修正パッチ](https://review.openstack.org/#/c/393651) を出しています。（まだ誰もレビューしてくれないけどｗ）
* Ubuntuバージョンはxenialが基本(trustyが必要でなければそのジョブは入れないほうが良い)

くらいでしょうか。



## 感想・まとめ

* リポジトリ追加は比較的カンタン
* OpenStack Infra job設定わかりづらい。。(他のを真似してやればある程度は想像つくけど)
* でも、OpenStack インフラを使って自動ビルド・テストが実行できるのはとても便利


## 参考URL

* [Project Creator’s Guide](http://docs.openstack.org/infra/manual/creators.html)
* coverage2sql

  * https://launchpad.net/coverage2sql
  * openstack/governance: [Add coverage2sql to Quality Assurance](https://review.openstack.org/#/c/394276/)
  * openstack-infra/project-config: [Add coverage2sql project](https://review.openstack.org/#/c/393634/)



Happy Hacking!
