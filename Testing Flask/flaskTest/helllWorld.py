from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author':"Satwik Mishra",
        'age':'23',
        'content':"What is up guys!?"
    },
        {
        'author':"Sampu",
        'age':'20',
        'content':"Sab Badhiya!?"
    },
    
]

@app.route("/")
@app.route("/Home")
def Home():
    return render_template("home.html", posts=posts, title='yoyo')


@app.route("/about")
def About():
    return render_template("about.html")


if __name__=='__main__':
    app.run(debug=True)
