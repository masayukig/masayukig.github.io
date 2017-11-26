Title: lvremove出来ない！(Can't remove open logical volume "hogehoge")
Date: 2009-03-20 09:13
Author: masayukig
Tags: サーバ管理, dm, LVM, lvremove
Status: published

lvmを使っていて、必要なくなったlvを削除するためのコマンドである、  
lvremove  
というのがあります。  
先日、iscsiテスト用に作ったlvを、これを使って削除しようとしたら、

    $ sudo lvremove  /dev/vg01/iscsi
    Can't remove open logical volume "iscsi"

と、言われて削除できなかったので、その解決方法など。  
[]{#more}  
結論を言うと、

    $ sudo dmsetup ls
    vg01-iscsip3  (254, 4)
    vg01-iscsip1  (254, 3)
    vg01-iscsi    (254, 0)
    $ sudo dmsetup remove vg01-iscsip1
    $ sudo dmsetup remove vg01-iscsip3
    $ sudo dmsetup remove vg01-iscsi
    $ sudo lvremove  /dev/vg01/iscsi
      Logical volume "iscsi" successfully removed

と、すれば良い模様。  
最初、

    $ sudo dmsetup remove vg01-iscsi

をやったのですが、

    device-mapper: remove ioctl failed: Device or resource busy
    Command failed

と、言われて削除できませんでした。

vg01-iscsip1,3というのが(多分)勝手に作られていて、  
それがあったために、vg01-iscsiを削除できなかったのではないかと思っています。

\#記憶は若干あやふやなので、参考程度に。。
