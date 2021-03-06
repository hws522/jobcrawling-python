from flask import Flask, render_template, request, redirect, send_file
from jobkorea import get_jobkorea_jobs
from saramin import get_saramin_jobs
from save import save_to_file

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
            jobs = get_jobkorea_jobs(word) + get_saramin_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")
    return render_template(
        "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


# app.run(host="127.0.0.1")
