from flask import Flask
app = Flask(__name__)

@app.route('/secret')
def secret():
    return "Sensitive backend data!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
