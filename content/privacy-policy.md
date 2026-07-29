---
title: "Privacy Policy / プライバシーポリシー"
url: "/privacy-policy/"
---

Last updated: 2026-07-29 / 最終更新: 2026年7月29日

## English

### 1. Scope

This Privacy Policy covers:

1. **This website** (`https://igawa.io/`), a personal blog operated by Masayuki Igawa.
2. **health-tracker**, a personal, self-hosted application operated by Masayuki Igawa
   for the sole purpose of recording and visualizing his own health data. It is not
   offered to, and is not usable by, any other person.

### 2. This website

This website uses Google Analytics to collect anonymous aggregate access statistics
(such as page views and referrers). Google Analytics uses cookies. You can opt out via
the [Google Analytics Opt-out Browser Add-on](https://tools.google.com/dlpage/gaoptout).
This website does not otherwise collect personal information, and has no login,
no user accounts, and no forms.

### 3. health-tracker and Google user data

health-tracker reads the operator's own health and fitness data from the Google Health
API using the following OAuth scopes, all of which are read-only:

| Scope | Data | Why it is needed |
|---|---|---|
| `https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly` | Daily step counts | To chart daily activity over time |
| `https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly` | Resting heart rate, heart rate variability | To chart cardiovascular trends alongside blood test results |
| `https://www.googleapis.com/auth/googlehealth.sleep.readonly` | Sleep sessions and sleep stage durations | To chart sleep duration and quality over time |

No write scopes are requested. health-tracker never adds, modifies, or deletes any data
in the operator's Google account.

**How the data is used.** Solely to display the operator's own data back to the operator
as time-series charts in a private, self-hosted Grafana dashboard.

**How the data is stored.** In a PostgreSQL database running on the operator's own
hardware, on a private home network that is not reachable from the public internet.
OAuth tokens are stored in the same database.

**How the data is shared.** It is not. The data is never transferred to, sold to, or
disclosed to any third party. It is not used for advertising, and it is not used to
train, fine-tune, or evaluate any machine learning or AI model. No human other than the
operator has access to it.

**Retention and deletion.** Data is retained for as long as the operator finds it useful.
The operator can revoke health-tracker's access at any time at
[Google Account permissions](https://myaccount.google.com/permissions), which stops all
further access. Stored data can be deleted by dropping the relevant database tables.

### 4. Limited Use disclosure

The use of information received from Google Health API and/or Developer Tools will
adhere to the [Google Health API Developer and User Data Policy](https://developers.google.com/health/policies/health-api-developer-user-data-policy),
including the Limited Use requirements.

### 5. Children

Neither this website nor health-tracker is directed at children, and neither knowingly
collects any information from children.

### 6. Changes

Any change to this policy will be published on this page with an updated "Last updated"
date.

### 7. Contact

Masayuki Igawa — masayuki.igawa@gmail.com

---

## 日本語

### 1. 適用範囲

本プライバシーポリシーは以下を対象とします。

1. **本サイト**（`https://igawa.io/`）— 井川征幸が運営する個人ブログ
2. **health-tracker** — 井川征幸が自身の健康データを記録・可視化する目的のみで運用する、
   自宅ホストの個人用アプリケーション。他者へ提供しておらず、他者が利用することはできません

### 2. 本サイトについて

本サイトは Google Analytics により、ページビューやリファラといった匿名の集計アクセス統計を
取得します。Google Analytics は Cookie を使用します。
[Google アナリティクス オプトアウト アドオン](https://tools.google.com/dlpage/gaoptout)
により無効化できます。これ以外に個人情報を取得することはなく、ログイン機能・ユーザー登録・
入力フォームはいずれもありません。

### 3. health-tracker と Google ユーザーデータ

health-tracker は、運用者本人の健康・フィットネスデータを Google Health API から取得します。
使用するスコープは以下の3つで、いずれも読み取り専用です。

| スコープ | データ | 必要な理由 |
|---|---|---|
| `https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly` | 日次の歩数 | 日々の活動量を時系列で可視化するため |
| `https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly` | 安静時心拍数・心拍変動 | 血液検査結果と並べて循環器系の推移を可視化するため |
| `https://www.googleapis.com/auth/googlehealth.sleep.readonly` | 睡眠セッション・睡眠ステージ別時間 | 睡眠時間と睡眠の質の推移を可視化するため |

書き込み系スコープは一切要求しません。health-tracker が運用者の Google アカウント内の
データを追加・変更・削除することはありません。

**利用目的**: 運用者自身のデータを、自宅ホストの非公開 Grafana ダッシュボード上で
時系列グラフとして運用者本人に表示するためだけに使用します。

**保管方法**: 運用者所有のハードウェア上で動作する PostgreSQL に保存します。
当該ネットワークは自宅内の閉じたネットワークであり、インターネットからは到達できません。
OAuth トークンも同じデータベースに保存します。

**第三者提供**: 行いません。いかなる第三者へも、提供・販売・開示しません。
広告目的で利用することはなく、機械学習・AIモデルの学習・チューニング・評価にも利用しません。
運用者本人以外がアクセスすることはありません。

**保持期間と削除**: 運用者が有用と判断する限り保持します。
[Google アカウントの権限管理](https://myaccount.google.com/permissions) から
health-tracker のアクセス権をいつでも取り消すことができ、取り消し以降のアクセスは停止します。
保存済みデータは該当テーブルを削除することで消去できます。

### 4. Limited Use に関する表明

Google Health API および開発者向けツールから受け取った情報の利用は、Limited Use の要件を含む
[Google Health API Developer and User Data Policy](https://developers.google.com/health/policies/health-api-developer-user-data-policy)
に準拠します。

### 5. 子どもについて

本サイト・health-tracker のいずれも子どもを対象としておらず、
子どもから情報を取得することはありません。

### 6. 変更について

本ポリシーを変更した場合は、本ページ上で「最終更新」日を更新して公開します。

### 7. 連絡先

井川 征幸 (Masayuki Igawa) — masayuki.igawa@gmail.com
