from flask import Flask, render_template, request
from parser_dict import select_all

app = Flask("여기로가잡!")

@app.route('/')
def home():
    jobs = select_all()
    return render_template("home.html", jobs=jobs)

@app.route('/search')
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    jobs = select_all()
    print(jobs)
    return render_template('search.html', keyword=keyword, jobs=jobs)
