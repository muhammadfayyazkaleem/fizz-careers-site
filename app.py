from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS =[
    {
        "id": 1,
        "position":"Data Analyst",
        "location":"Lahore Pakistan",
        "salary":"RS. 1,000,00"

    },
        {
        "id": 1,
        "position":"Python Developer",
        "location":"Rahim Yar Khan Pakistan",
        

    },
    {
        "id": 1,
        "position":"Backend Engineer",
        "location":"Lahore Pakistan",
        "salary":"RS. 2,000,00"

    },
    {
        "id": 4,
        "position":"Front End Engineer",
        "location":"Karachi Pakistan",
        "salary":"RS. 1,000,00"

    },
        {
        "id": 5,
        "position":"Front End Engineer",
        "location":"Rahim Yar Khan Pakistan",
        "salary":"RS. 100,00"

    }

]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS, company_name="Fizz")

@app.route("/api/jobs")
def about():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)