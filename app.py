from flask import Flask, render_template, request


app = Flask("여기로가잡!")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    return render_template('search.html', keyword=keyword)
