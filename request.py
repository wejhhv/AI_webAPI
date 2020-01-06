###簡易チャットボットの作成

import requests
import json


print("チャットボットを開始します\nbyeと発言すれば終了します\nまた空白でサーバーとの通信を確認します")
# webAPIのURL
#url="http://127.0.0.1:5000/hello/"
url="https://ganosu.herokuapp.com/"
word=input("you>>>>>>")

# 終了までループ
while word!="bye":

    #webAPIに入力した言葉を引き渡す
    r=requests.get(url+word.encode("utf-8"))
    
    # データはjson形式ではいる
    data = r.json()
    
    # 未学習かどうかの判定
    print("bot>>>>>"+data)
    # ユーザの表示
    word=input("you>>>>>>")


print("チャットボットを終了しました")
