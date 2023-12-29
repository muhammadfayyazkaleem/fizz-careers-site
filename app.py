from flask import Flask, render_template, jsonify
from database import load_job_from_db
app = Flask(__name__)

    
@app.route("/")
def home():
    jobs = load_job_from_db()
    return render_template('home.html', 
                           jobs=jobs, company_name="Fizz")


@app.route("/api/jobs")
def about():
    jobs = load_job_from_db()
    return jsonify(jobs)


@app.route("/apply")
def job_apply(): 
    return render_template('apply.html')

if __name__ == "__main__":
    app.run(debug=True)