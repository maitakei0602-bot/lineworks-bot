from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])

def home():

    return "BOT is running!"

@app.route("/callback", methods=["POST"])

def callback():

    data = request.json

    text = str(data)

    if "残業申請" in text:

        return {

            "content": {

                "type": "text",

                "text": "【残業申請方法】\n①マネーフォワードを開く\n②申請を押す\n③残業申請を選択\n④時間と理由を入力\n⑤送信で完了"

            }

        }

    return "ok"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)
