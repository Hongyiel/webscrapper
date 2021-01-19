from flask import Flask, render_template,request,redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("potatos.html")

@app.route("/report")
def report():

    # print(request.args.get('word'))
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
        # fromDb = db.get(word)
        # if fromDb:
        #     jobs = fromDb
        # else:
        #     jobs = get_jobs(word)
        #     db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)
app.run()

# app.run(host="0.0.0.0")
