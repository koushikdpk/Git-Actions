from flask import Flask, render_template, request

from form import EmployeeForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

color="beige"

@app.route('/')
def home():
    form = EmployeeForm()    
    return render_template('Home Page.html', form=form, color=color)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("Result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
