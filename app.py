from flask import Flask, render_template, request
from db_saver import select_all
from parser_dict import *

app = Flask("여기로가잡!")

@app.route('/')
def home():
    jobs = select_all()
    return render_template("home.html", jobs=jobs)

@app.route('/search')
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    parse_jobs() # 구글클래스 채용공고 웹스크래핑
    jobs = select_all()
    print(jobs)
    return render_template('search.html', keyword=keyword, jobs=jobs)
