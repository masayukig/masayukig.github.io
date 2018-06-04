Title: OpenStack Tempest の テストを実行する方法 (testr vs run_tempest.sh vs tox)
Date: 2014-12-17 05:34
Author: masayukig
Category: Uncategorized
Status: published
Attachments: 2014/12/ece92-executing_tempest_testr.png, 2014/12/20ebc-executing_tempest.png

Tempest は OpenStackのテストスイートです。  
これを実行することにより、OpenStackが"ちゃんとうごく"かどうかを確認できます。

準備
----

DevStackを使ってOpenStackをインストールして、一緒にTempestもインストールした場合には下記準備作業は不要です（自動的に設定ファイルを設定してくれるため）。  
なお、Tempestは現在３つのバージョン（Icehouse, Juno,
master）にブランチなしで対応していますので、基本的には最新版のTempestを使えば事足りるはずです。  
（サポートしていない機能などがあれば、下記に示す設定ファイル(tempest.conf)でテストするかどうかを設定できます。)

    mkdir -p /opt/stack
    cd /opt/stack
    git clone https://github.com/openstack/tempest
    cd /opt/stack/tempest
    cp etc/tempest.conf.sample etc/tempest.conf
    vi etc/tempest.conf

テスト対象の環境に合わせて、編集します。まずはidentityセクションを修正すれば、たぶんなんとかなるでしょう。

    [identity]
    auth_version = v2
    admin_domain_name = Default
    admin_tenant_id = d44ed5a94d4c4c70a4e91bb9c979eda1
    admin_tenant_name = admin
    admin_password = ぼくのかんがえたさいきょうのパスワード
    admin_username = admin
    alt_tenant_name = alt_demo
    alt_password = ぼくのかんがえたさいきょうのパスワード
    alt_username = alt_demo
    tenant_name = demo
    password = ぼくのかんがえたさいきょうのパスワード
    username = demo
    uri_v3 = http://192.168.1.xx:5000/v3/
    uri = http://192.168.1.xx:5000/v2.0/

実行
----

さて、いよいよ実行です。  
ただ、その実行方法はいくつかあり、少し混乱するときもあると思います。  
いくつかの例を示します。

なお、[公式ドキュメント](http://docs.openstack.org/developer/tempest/overview.html#quickstart)には、

    testr run --parallel
    testr run --parallel tempest.api.compute.servers.test_servers_negative.ServersNegativeTestJSON.test_reboot_non_existent_server

という方法が書かれています。  
一番目の方法では、全てのテストが実行されます。環境にも依存しますが、だいたい１時間程度はかかると思っておいたほうが良いでしょう。  
二番目の方法では、指定したテストが実行されます。なおここは正規表現が使えるようです。

以下、実行例です。

<div class="separator" style="clear:both;text-align:center;">

</div>

<div class="separator" style="clear:both;text-align:center;">

[![picture](https://masayukig.files.wordpress.com/2014/12/ece92-executing_tempest_testr.png)](https://masayukig.files.wordpress.com/2014/12/ece92-executing_tempest_testr.png)

</div>

<div>

一つのテストが3.512秒で実行されて、成功したことがわかります。

</div>

コレ以外にも、「run\_tempest.sh」「tox」を使って実行する方法も示されていますので、それらを使ってみましょう。

<div class="separator" style="clear:both;text-align:center;">

[![picture](https://masayukig.files.wordpress.com/2014/12/20ebc-executing_tempest.png)](https://masayukig.files.wordpress.com/2014/12/20ebc-executing_tempest.png)

</div>

まとめ
------

いずれも、同じテストケースを実行しているので、出力もほぼ同様です。好みに合わせて使い分ければ良いと思います。  
個人的な好みとしては、toxを使ったときの出力がわかりやすく、親しみやすい（フェイスマークもあるし）感じられるので、toxを使っていこうかなと思います。

Happy testing!
