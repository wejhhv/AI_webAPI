### 簡単なWebAPIの作成

import json
from gensim.models import word2vec #word2vecモデルのインポート
from flask import Flask,jsonify,request #Flaskクラスのインポート

model   = word2vec.Word2Vec.load('wiki.model')

app = Flask(__name__) #appという名前のFlaskクラスのインスタンスを作成

"""
@app.route("/",methods=['GET']) 

def all():
    print("通信はできています")

    return jsonify("通信はできているよ")
"""
# 変更点  methodsの追加
@app.route("/hello/<string:words>",methods=['GET']) #ルーティング(URLの設定）及び引数の指定


def hello(words): #"/hello"のURLで呼び出される関数

#単語が辞書に存在するか確認
    if words in model.wv.vocab:
    
        r = model.most_similar(positive=[words], topn=1)
        x=r[0]
        
        # json形式で返す
        return jsonify(x)
    
    #この単語についてはその都度辞書にプラスするコードを書いておく
    else:
        
        # 辞書にない単語に対しては１で返す
        return jsonify(1)
        
        #return jsonify(words+"は未学習の言葉です")

#キーワードが空白の場合
@app.route("/hello/",methods=['GET']) #ルーティング(URLの設定）

def empty(): #"/hello/"のURLで呼び出される関数

    return jsonify(2)

"""
@app.route("/chat",methods=['GET']) #ルーティング(URLの設定）

def chat(): #"/chat?text=words"のURLで呼び出される関数
    # 確認用
    print("受信した文字はです")

    return jsonify("通信はできています")
"""
# 追加した部分
@app.route('/')
def get_request():
    value = request.args.get('text', '')
    callback = request.args.get('callback', '')

    if (value.find('おはよう') != -1):
        value = 'おはようございます。<br>ごきげんはいかがですか？'

    if (value.find('元気') != -1):
        value = '元気でよかったですね'

    if (value.find('天気') != -1):
        value = '今日の天気は晴れです。'

    dic = {'output' : [{'type' : 'text', 'value' : value }] }
    contents = callback + '(' + json.dumps(dic) + ')'
    return contents


if __name__ == "__main__":

    app.run() # Webサーバーを立ち上げる
