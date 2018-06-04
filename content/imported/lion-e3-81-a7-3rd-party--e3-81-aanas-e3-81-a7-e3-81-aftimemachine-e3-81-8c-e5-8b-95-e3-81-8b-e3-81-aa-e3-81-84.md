Title: Lionで 3rd party なNASではTimeMachineが動かない
Date: 2011-07-23 05:33
Author: masayukig
Tags: Apple, lion, Mac, nas, OS, timemachine
Status: published

昨日、Lionにアップデートしましたが、以下の様なエラーがでて  
Time Machineでバックアップができなくなりました。  
[![picture](https://lh5.googleusercontent.com/-eNFciYAVxnk/Tjr6xhXwX5I/AAAAAAAAg6M/p3ABUDEbpv8/s288/5964468227_f23fe1aabe_o.png)
](https://picasaweb.google.com/lh/photo/4ufmuZEyhHGTyu3bVo7Ysg?feat=embedwebsite)

ググってみたところ、いくつかの情報が得られました。

-   <http://slashdot.jp/apple/comments.pl?sid=539273&cid=1989826>
-   <http://amiens2009.tumblr.com/post/7886573873/timemachine-apple-nas-lion>

なお、今回のバックアップ失敗では、以下の様なログが/var/log/syslog.log
に出力されていました。  
<https://gist.github.com/1100364.js?file=Time-Machine-backup-failed-system.log>
