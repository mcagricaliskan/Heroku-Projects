from flask import Flask, request

app = Flask(__name__)

@app.route('/about')
def index():
    return {"name": "Çağrı", "Year": "24", "Job": "Deep Learning Engineer"}

if __name__ == '__main__':

    app.run()