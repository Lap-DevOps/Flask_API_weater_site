from flask import Flask
app = Flask(__name__)

# Импортируем переменные из config.py
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()