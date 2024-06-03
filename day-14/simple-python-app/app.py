from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'H e l l o,  world!'

if __name__ == '__main__':
    app.run()

