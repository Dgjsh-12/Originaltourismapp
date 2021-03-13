<div align="center">
<img width="300" src="https://user-images.githubusercontent.com/67186355/110197054-3387ef80-7e8c-11eb-96f6-6b2b2bc2512f.jpg">
</div>
<br>

観光アプリはユーザーの訪れた観光スポットの情報を共有する SNS です。自分が観光で訪れたスポットを投稿したり、他のユーザーの投稿した観光情報を参考にしたり、感想を投稿したりすることができます。

# 環境
* AWS Cloud9
* Python3 3.7.7
* django 3.1.5
* SQLite3 3.34.0

# インストール手順
```
$ git clone https://github.com/Dgjsh-12/tourismapp.git
$ python3 manage.py runserver 0.0.0.0:8080
```

# ログイン
* ユーザー名：安宅
* パスワード：Ataka111

# 画像の説明

## ログイン画面
* https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/login/
![ログイン画面](https://user-images.githubusercontent.com/67186355/110622349-aff93600-81de-11eb-8a23-5d12c114e340.png)
* ユーザー名、パスワードでログインします。

## アカウント登録画面
* https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/signup/
![アカウント画面](https://user-images.githubusercontent.com/67186355/110622625-0f574600-81df-11eb-8336-4937b104a10a.png)
* ユーザー名、パスワード、再度パスワードでアカウントを登録します。

## ホーム画面
* https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/
![ホーム画面](https://user-images.githubusercontent.com/67186355/110510095-344baa80-8146-11eb-8951-34b36bf0a044.png)
* 観光名と観光スポットの画像が表示されます。観光名もしくは画像をクリックすると観光スポットの情報と口コミが見られます。情報と口コミは今の所、清水寺をクリックすると表示されます。

## 観光スポットの情報画面
* https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/showall/
![観光スポットの情報画面](https://user-images.githubusercontent.com/67186355/110683863-dbe8db80-821f-11eb-8fd4-66704be887e4.png)
* 情報には、観光スポットの歴史の内容と基本情報と口コミが表示します。

## 投稿画面
* https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/upload/
![投稿画面](https://user-images.githubusercontent.com/67186355/110510495-94dae780-8146-11eb-80c2-3a819d4b23a7.png)
* 投稿には、タイトル、内容、画像で投稿が出来ます。

## 履歴画面
* (https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/betails/)
![履歴画面](https://user-images.githubusercontent.com/67186355/110510982-16cb1080-8147-11eb-8794-47f607e6ddbe.png)
* 投稿したのが表示され、編集、削除ボタンも表示します。

## 編集画面
* (https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit)
![編集画面](https://user-images.githubusercontent.com/67186355/110511201-5691f800-8147-11eb-9f21-67ffc9931ddc.png)
* 投稿したのを編集出来ます。

## 削除画面
* (https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/82/delete)
![削除画面](https://user-images.githubusercontent.com/67186355/110578924-14999e00-81a9-11eb-9b99-9f7f058706b8.png)
* 投稿したのを削除出来ます。

## ログアウト
* ログアウトをすると、ログイン画面に飛ばされます。

## ハンバーガーメニュー
* ハンバーガーメニューには、ホーム、投稿、履歴、ログアウトが表示されます。
<img src="https://user-images.githubusercontent.com/67186355/110513640-cbfec800-8149-11eb-955b-29d340c6adcd.png">

## ナビゲーションバー
* ナビゲーションバーには、日本地域 ⇨ 都道府県 ⇨ 区、市、町、村の順で表示されます。
<img src="https://user-images.githubusercontent.com/67186355/110579361-fda77b80-81a9-11eb-88e0-0d96a431b24c.png">

