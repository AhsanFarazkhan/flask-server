from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.data.decode()
    print("Received data:", data)
    return "Data received!"

if __name__ == '__main__':
    app.run()
