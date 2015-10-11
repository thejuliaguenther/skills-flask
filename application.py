from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/application-form")
def index_page():

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application",  methods=['POST', 'GET'])
def thank_you():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")

    person = firstname +" "+lastname

    # if position_type == "softwareeng":
    #     position = "Software Engineer"
    # elif position_type == "qaeng":
    #     position = "QA Engineer"
    # else:
    #     position = "Product Manager"

    return render_template("application.html", person=person, salary=salary, position=position)


if __name__ == "__main__":
    app.run(debug=True)
