from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pg3():
    return render_template('pg3.html')



if __name__ == '__main__':
    app.run()

