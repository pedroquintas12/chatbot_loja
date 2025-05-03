from flask import Flask, render_template, request
from chatbot import responder

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    user_input = request.form["mensagem"]
    resposta = responder(user_input)
    return {"resposta": resposta}


if __name__ == "__main__":
    app.run(debug=True)
