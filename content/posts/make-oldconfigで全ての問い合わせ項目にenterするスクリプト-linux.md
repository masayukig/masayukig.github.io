---
title: 'make oldconfigで全ての問い合わせ項目にEnterするスクリプト #Linux'
date: '2010-06-05T14:25:00+09:00'
slug: make-oldconfigで全ての問い合わせ項目にenterするスクリプト-linux
tags:
- 開発
- kernel
- OS
- tips
draft: false
disqus_identifier: 2010-06-05-make-oldconfigdequan-tenowen-ihe-wasexiang-mu-nientersurusukuriputo-linux
---

Linux
kernelのmakeのターゲットでありそうな気もするんですが、見つからなかったので。

\$ cat make\_oldconfig\_auto.sh

``` {.ruby}
#!/usr/bin/env expect

set timeout 10
spawn make oldconfig
while {1} {
        expect {
                "] (NEW)" { send "\n" }
                "# configuration written to .config" {break}
        }
}

interact
```

見てわかるとおり、expectを使って、"\]
(NEW)"というのが出てきたら、Enter入力。
"\# configuration written to .config"が出てきたらおしまい。

というスクリプトです。
