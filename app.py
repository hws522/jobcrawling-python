from flask import Flask, render_template, request, redirect
from saramin import get_jobs


app = Flask("jobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")
    return render_template("report.html", serchingBy=word, resultsNumber=len(jobs), jobs=jobs)
