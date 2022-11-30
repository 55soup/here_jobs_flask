from flask import Flask, render_template, request
from db_saver import *
from flask_sqlalchemy import SQLAlchemy
from parser_dict import *

app = Flask("여기로가잡!")
# db=SQLAlchemy(app)

@app.route('/')
def home():
    jobs = select_all()
    # parse_jobs() # 구글클래스 채용공고 웹스크래핑
    return render_template("home.html", jobs=jobs)

# class Jobs(db.Model):
#     enterprise = 
#     enterprise_num = 
#     sector = 
#     employee = 
#     sales = 
#     address = 
#     weblink = 
#     introduce = 
#     work = 

@app.route('/search', methods = ['GET', 'POST'])
def search():
    keyword = request.args.get("keyword")
    # jobs = Jobs.query.filter().all()
        # name = request.form['name']
        # con = sqlite3.connect("database.db")
        # cur = con.cursor()
        # # cur.execute(f"SELECT * FROM jobs WHERE sector='{keyword}'")
        # cur.execute(f"SELECT * FROM jobs WHERE enterprise LIKE {keyword}?'")
        # rows = cur.fetchall()
        # print(rows)``
        # print("DB:")
        # for i in range(len(rows)):
        #     print(rows[i][0] + ':' + rows[i][1])
    jobs_list = select_all()
    index_list=search_keyword(keyword)
    return render_template('search.html', index_list = index_list, keyword=keyword, jobs=jobs_list)
    # return render_template('search.html', keyword=keyword, msg="찾는 결과가 없습니다.")
    
