---
title: ssh git@github.comで「Agent admitted failure to sign using the key. 」と なったら...
date: '2010-10-11T05:49:00+09:00'
slug: ssh-git@githubcomでagent-admitted-failure-to-sign-using-the-key-と-なったら
tags:
- 開発
- git
- github
draft: false
disqus_identifier: 2010-10-11-ssh-gitgithubcomdeagent-admitted-failure-to-sign-using-the-key-to-natsutara
---

ssh git@github.comで「Agent admitted failure to sign using the key.
」となったら、

`ssh-add ~/.ssh/id_rsa`
と、するとうまくいくかもしれない。

参考サイト：<http://ripan27.wordpress.com/2010/04/01/ssh-gitgithub-com-agent-admitted-failure-to-sign-using-the-key-permission-denied-publickey/>
