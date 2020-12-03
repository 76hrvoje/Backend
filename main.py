from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/BootstrapHomework1")
def BootstrapHomework1():
    return render_template("BootstrapHomework1.html")

if __name__ == '__main__':
    app.run()

