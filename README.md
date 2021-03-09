<div align="center">
<img width="300" src="https://user-images.githubusercontent.com/67186355/110197054-3387ef80-7e8c-11eb-96f6-6b2b2bc2512f.jpg">
</div>

# アプリの説明
こちらのWebアプリは観光スポットと、なっております。行きたい観光スポットをエリア一覧で選択、出来ますし観光スポットの情報や他のユーザーが観光に行った時の感想なのが投稿されていて見られる事が出来ます。自分でも観光に行った時の感想を投稿する事も出来ます。もちろん、投稿したのを編集、削除と言った事も出来ます。

# アプリの機能について
* ログイン機能
  * ログインには、ユーザー名、パスワードでログイン出来ます。
  * [ログイン画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/login/)
  * HTMlは「polls/templates/polls/signup」
  * 実際のログイン画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110495787-33138100-8138-11eb-8db0-e8fd9dfd76fa.png">
</div>

* アカウント登録機能
  * アカウント登録には、ユーザー名、パスワード、再度パスワードがあります。
  * [アカウント画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/signup/)
  * HTMlは「polls/templates/polls/signup」
  * 実際のアカウント画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110509549-8f30d200-8145-11eb-9f36-19a8bb3be07d.png">
</div>

* ログアウト機能
  * ログアウトをすると、ログイン画面に飛ばされます。
  * HTMlは「polls/templates/polls/login」

* 投稿機能
  * 投稿機能には
    * タイトル名
    * テキスト
    * 画像選択
  * [投稿画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/upload/)
  * HTMlは「album/templates/album/upload」
  * 実際の投稿画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110510495-94dae780-8146-11eb-80c2-3a819d4b23a7.png">
</div>

* 履歴機能
  * 履歴機能には、投稿したのが履歴として表示されます。
  * [履歴画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/betails/)
  * HTMlは「album/templates/album/betails」
  * 実際の履歴画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110510982-16cb1080-8147-11eb-8794-47f607e6ddbe.png">
</div>

* 編集機能
  * 投稿した、タイトル名、テキスト、画像選択を編集する事が出来ます。
  * [編集画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit)
  * HTMlは「album/templates/album/betails」
  * 実際の編集画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110511201-5691f800-8147-11eb-9f21-67ffc9931ddc.png">
</div>

* 削除機能
  * 投稿したのを削除出来ます。
  * [削除画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/82/delete)
  * HTMlは「album/templates/album/delete」
  * 実際の削除画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110511496-a07ade00-8147-11eb-96b9-57ef2b87757e.png">
</div>

# アプリの画面について
* ログイン画面
  * ログイン画面には、ユーザーとパスワードを入力します。入力したら、ログインボタンを押して、ホーム画面に行くようになっています。
  * [ログイン画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/login/)

* アカウント画面
  * アカウント登録画面には、ユーザー名、パスワード、再度パスワードを入力する枠が表示されます。
  * [アカウント画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/signup/)
  * 実際のアカウント画面です。☟
<div align="center">
<img src="https://user-images.githubusercontent.com/67186355/110509549-8f30d200-8145-11eb-9f36-19a8bb3be07d.png">
</div>
 
* ホーム画面
  * ホーム画面には観光名と画像が表示されます。
  * [ホーム画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/index.html)

* 観光スポット情報画面
  * 観光スポット情報画面には、観光スポットの情報と口コミが表示されます。
  * [観光スポット](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/showall/)

* 投稿画面
  * 投稿画面には、タイトル、内容、画像選択が表示されます。
  * [投稿画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/upload/)

* 履歴画面
  * 履歴画面には、投稿したのが履歴として表示されます。
  * [履歴画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/betails/)

* 編集画面
  * 編集画面には、タイトル、内容、画像を編集出来て投稿する事ができます。
  * [編集画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit)

* 削除画面
  * 削除画面には、投稿したのを削除できます。
  * [削除画面](https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/82/delete)

* アプリ画面には、アプリ名とハンバーガーメニューがフッターに表示されます。(ログイン画面とログアウト画面には表示させていません)
  * アプリ名には、リンクがありホーム画面に飛ばされます。
  * ハンバーガーメニューには
    * ホーム
    * 投稿する
    * 投稿履歴
    * ログアウト
