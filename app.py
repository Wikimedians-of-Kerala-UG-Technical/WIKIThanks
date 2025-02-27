from flask import Flask, render_template, jsonify
from wiki_api import WikiAPI
app = Flask(__name__)
wiki_api = WikiAPI()
@app.route("/")
def earth_page():
    return render_template("indexpage.html")
@app.route("/contributors/<page_title>")
def contributors(page_title):
    return render_template("indexpage.html")
@app.route("/contributor/<page_title>/<username>")
def contributor_details(page_title, username):
    return render_template("contributor.html", username=username, page_title=page_title)
@app.route("/api/contributor/<page_title>/<username>")
def get_contributor_changes(page_title, username):
    changes = wiki_api.get_user_contributions(page_title, username)
    return jsonify(changes)
@app.route("/api/contributors/<page_title>")
def get_contributors(page_title):
    contributors = wiki_api.get_page_history(page_title)
    return jsonify(contributors)
if __name__ == "__main__":
    app.run(debug=True)
