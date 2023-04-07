from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Tratar os dados recebidos aqui
    print(data)
    return '', 200

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=3000,
    )
