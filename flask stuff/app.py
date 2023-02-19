from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def index():
    if request.method == "POST":
        if request.form.get('action1') == "VALUE1":
            pass
        elif request.form.get("action2") == "VALUE2":
            pass
        else:
            pass
    
    elif request.method == "GET":
        return render_template('index.html', form=form)

    return render_template("index.html")

#app.run('0.0.0.0', port=81, debug=True)