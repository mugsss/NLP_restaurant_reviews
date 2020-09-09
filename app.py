from flask import Flask, render_template, request, url_for, redirect
from sentimental_analysis import sentiments

app = Flask(__name__)
app.add_url_rule('/photos/<path:filename>', endpoint='photos',
                 view_func=app.send_static_file)

@app.route("/")
def home():
    return render_template("index.html", response=None)

@app.route("/analysis",methods=["POST"])
def result():
    data = request.form["card"]
    output = sentiments(data)
    return render_template("index.html",response=True,prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)