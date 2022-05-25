# GitHubImageMaker
GitHubのグリッド風の画像生成プログラムです

## 機能
入力した文字に合わせGitHubのグリッド風に画像を出力するプログラムです。

## ざっくりとした仕組み
iniファイルやjsonファイルからフォントデータや色情報の取得<br>
↓<br>
tkinterを用いたデスクトップアプリの起動<br>
↓<br>
Entryに入力された情報を元にキャンバス上に描画

## 動かない場合
・実行できない！<br>
→Python実行環境がない可能性があります。Pythonの実行環境を用意してください。

## 使用ライブラリ
使用したライブラリは以下の通りです。<br>
今回使用したライブラリはデフォルトで入っているはずなのでpip等でインストールする必要はないと思います。<br>
| ライブラリ名   | 使用目的                            |
|:--------------|:------------------------------------|
| tkinter       | デスクトップアプリ用ライブラリ        |
| random        | ランダム抽出                        |
| json          | jsonファイル読み込み                |
| configparser  | iniファイル読み込み                 |

## お問い合わせ
何かございましたら「shaneron@sumahotektek.com」まで連絡ください。反応は非常に遅いです。<br>

### 変更履歴
Ver1.0:初期バージョン<br>
Ver1.1:アルファベット小文字に対応しました
