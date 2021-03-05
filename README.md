# アプリの説明
こちらのWebアプリは観光スポットと、なっております。行きたい観光スポットをエリア一覧で選択、出来ますし観光スポットの情報や他のユーザーが観光に行った時の感想なのが投稿されていて見られる事が出来ます。自分でも観光に行った時の感想を投稿する事も出来ます。もちろん、投稿したのを編集、削除と言った事も出来ます。

# アプリの機能性について
1. ログイン機能
2. アカウント登録機能
3. ログアウト機能
4. 投稿機能
5. 履歴機能
6. 編集機能
7. 削除機能
# 機能性の説明
1. ログイン機能
* ログインには、ユーザー名、パスワードでログイン出来ます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/login/ 」
* テンプレートは「polls/templates/polls/signup」

2. アカウント登録機能
* アカウント登録には、ユーザー名、パスワード、再度パスワードがあります。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/signup/ 」
* テンプレートは「polls/templates/polls/signup」

3. ログアウト機能
* ログアウトをすると、ログイン画面に飛ばされます。
* テンプレートは「polls/templates/polls/login」

4. 投稿機能
* 投稿機能には
  * タイトル名
  * テキスト
  * 画像選択
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/upload/ 」
* テンプレートは「album/templates/album/upload」

5. 履歴機能
* 履歴機能には、投稿したのが履歴として表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/betails/ 」
* テンプレートは「album/templates/album/betails」

6. 編集機能
* 投稿した、タイトル名、テキスト、画像選択を編集する事が出来ます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit 」
* テンプレートは「album/templates/album/betails」

7. 削除機能
* 投稿したのを削除出来ます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/82/delete 」
* テンプレートは「album/templates/album/delete」

# アプリ画面について
1. ログイン画面
* ログイン画面には、ユーザーとパスワードを入力します。入力したら、ログインボタンを押して、ホーム画面に行くようになっています。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/login/ 」

2. アカウント画面
* アカウント登録画面には、ユーザー名、パスワード、再度パスワードを入力する枠が表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/signup/ 」
 
3. ホーム画面
* ホーム画面には観光名と画像が表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/polls/index.html 」

4. 観光スポット情報画面
* 観光スポット情報画面には、観光スポットの情報と口コミが表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/showall/ 」

5. 投稿画面
* 投稿画面には、タイトル、内容、画像選択が表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/upload/ 」

6. 履歴画面
* 履歴画面には、投稿したのが履歴として表示されます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/betails/ 」

7. 編集画面
* 編集画面には、タイトル、内容、画像を編集出来て投稿する事ができます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit 」

8. 削除画面
* 削除画面には、投稿したのを削除できます。
* URL「https://5b133c76535a4926883f182367974d03.vfs.cloud9.us-east-2.amazonaws.com/album/83/edit 」

9. アプリ画面には、アプリ名とハンバーガーメニューがフッターに表示されます。(ログイン画面とログアウト画面には表示されません。)
* アプリ名には、リンクがありホーム画面に飛ばされます。
* ハンバーガーメニューには
  * ホーム
  * 投稿する
  * 投稿履歴
  * ログアウト
