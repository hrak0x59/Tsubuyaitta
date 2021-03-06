# インセプションデッキ（チームメンバー間で共有すべき認識）

## プロジェクトの名前

# ツブヤイッター

## 名前をつけた理由

- 呟きを拾うツイッターみたいなアプリということで一時的に付けました

<div style="page-break-before:always">
</div>

## 1\. なぜこれを我々は作るのか？

1. ”授業中先生は個人チャットを見ないのでSlackで質問せよ”とのことだが実名で質問することによる抵抗が少なからずあり、インターラクティヴな授業が行われていない。= **活発性**
2. 授業後スラックで直ぐには返信されない長時間残るコメントを送信することに対する抵抗がある、これを解決したい。= **ラフさ**
3. 質問の緊急性、重要度が分からず乱雑に質問が乱立する場合があり、教師陣が困る。= **利便性**

### 目指す立ち位置

**スラックのようなある程度の閉塞性を持ちつつ、ツイッターのようなラフさを内包した中間的立ち位置のWebApplication**

<div style="page-break-before:always">
</div>


## 2\. 大まかな全体の流れ <!-- 未決定 -->

1. 機能提案
2. 大まかなデザイン決定
3. データベース格納要素決定
4. UMLフレーム
5. 機能追加削減
6. タスク振り分け（ブランチを切りアジャイルで簡易版を作る）
7. フロントエンド技術選定
8. ちゃんと開発（タスク分担）

### 技術的な解決策の概要

![概要レベルのアーキテクチャ設計図の画像]()

### 採用する技術

- [プログラミング言語]
- [ライブラリ]
- [ツール]
- [その他の要素技術]

<div style="page-break-before:always">
</div>


## 3\. 参考パッケージデザイン                                                      <!-- 未決定 -->

プロダクトの名前

![素敵な写真]()

### 最高のキャッチコピー

[最高のキャッチコピー]

### ユーザーへのアピール

1. [ユーザーへのアピールその1]
2. [ユーザーへのアピールその2]
3. [ユーザーへのアピールその3]

<div style="page-break-before:always">
</div>

## 4\. やらないことリスト                                                             <!-- 未決定 -->

カテゴリ   | 項目       | やる / やらない / あとで決める | 理由
------ | -------- | ------------------ | --------------
[カテゴリ] | [やること]   | やる                 | [やると決めた理由]
[カテゴリ] | [やらないこと] | やらない               | [やらないと決めた理由]
[カテゴリ] | [あとで決める] | あとで決める             | [あとで決めると決めた理由]

<div style="page-break-before:always">
</div>


## 5\. 夜も眠れなくなるような問題は何だろう？(もし起きたらこわーいこと、その3)

- チームメンバー間での足並みが揃わない
- レスポンスが返ってこない

<div style="page-break-before:always">
</div>

## 6\. 期間を見極める                                                                 <!-- 未決定 -->

![ざっくりしたタイムラインの画像]()

**アジャイル開発でやっていきましょう。**

<div style="page-break-before:always">
</div>

## 7\. トレードオフ・スライダー（優先度）

### 重要度

|  小|  >>>  |  >>>  |  >>>  |  大  | 項目                       |
| :---: | :---: | :---: | :---: | :---: | :------------------------ |
|      |       |       |       |   o    |  使いやすさ（利便性）|
|       |     |       |       |   o    |  シンプルでラフなビジュアル（仰々しくないビジュアル) |
|       |       |      |       |   o    |  アジャイル開発で時間を死守（最低２回）|
|       |    o   |       |     |       |  機能の充実（プラスαの機能）  |


<div style="page-break-before:always">
</div>

## 8\. 何がどれだけ必要なのか                                                         <!-- 未決定 -->

要素 | 値
--- | -----
人数 | 4名
期間 | 1ヶ月

### "チーム13"

名前  | 役割     | 強みや期待すること
---- | ------- | ---------------------------------------------------------
Hyoshida  | PM | シンプルなデザインが好きです。かなり細かいです。
Tkomeda  |     |
Hkumagaya  |      |
Hitou |      |
