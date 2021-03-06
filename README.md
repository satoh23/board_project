# Name
board_project
## Overview
匿名と記名どちらでも使える掲示板です。勉強として作りました。使うにはdockerがインストールされている必要があります。

## Description
ユーザーとしてログインしている場合は"ニックネーム"で、していない場合は"名無さん"として掲示板に書き込みができます。
その他ログイン中のユーザーとそうでないユーザで出来ることが違います。

#### ログインしていないユーザーができること
<p>・ユーザーの新規作成</p>
<p>・ログイン</p>
<p>・掲示板への書き込み(名前は強制的に"名無さん"になる)</p>

#### ログイン中のユーザーができること
<p>・スレッド作成</p>
<p>・ログアウト</p>
<p>・掲示板への書き込み(名前はユーザー作成時に設定した"ニックネーム"が使われる)</p>

こんな感じです。

## Install
board_projectをpullした後、anonumous_boardディレクトリ内に移動して
<p>$ docker-compose run web python3 manage.py makemigrations login_app</p>
<p>$ docker-compose run web python3 manage.py migrate</p>
します。

## Usage
まずanonumous_boardディレクトリ内で
<p>$ docker-compose up -d</p>
をします。その後「http://localhost:10000」に移動します。
<img width="1667" alt="スクリーンショット 2020-09-05 17 44 45" src="https://user-images.githubusercontent.com/55681554/92301578-e3dd6f80-ef9f-11ea-98f2-042a791f84b0.png">
<p>するとこのような画面に移動したと思います。</P>
<p>スレッドへの書き込みだけならこのまま使うこともできますが、ログインしないとスレッド作成ができません。</p>
<p>ユーザーの新規作成とログインは画面右上からできます。</p>
<p></p>
<p>また、スレッド名をクリックするとスレッドに移動することができます。</p>
<img width="1680" alt="スクリーンショット 2020-09-05 17 45 57" src="https://user-images.githubusercontent.com/55681554/92301712-dc6a9600-efa0-11ea-8edb-59bd7c171460.png">
<p>画面下のフォームからスレッドへの書き込みができます。</p>
<p>スレッドへの書き込みだけならこのまま使うこともできますが、ログインしないとスレッド作成ができません。</p>
<p>また、スレッド名をクリックするとスレッドに移動することができます。</p>

その他確認が完了したら
<p>$ docker-compose down</p>
 でコンテナを終了してください。
