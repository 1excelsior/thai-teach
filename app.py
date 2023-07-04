from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required


#Configure application
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///thaidict.db")


@app.route("/", methods=["GET", "POST"])
def index():
    """Search desired words"""

    # Getting keyword from a form and search through it
    if request.method == "POST":
        keyword = request.form.get("keyword")
        results = db.execute("SELECT * FROM words WHERE Thai LIKE ? OR Pronunciation LIKE ? OR Meaning LIKE ? LIMIT 10", "%" + keyword + "%", "%" + keyword + "%", "%" + keyword + "%")

        if len(results) == 0:
            return apology("No matching result", 401)

        return render_template("index.html", results = results)

    else:
        return render_template("index.html")

@app.route("/export", methods=["GET", "POST"])
def export():
    """The words-exporting site"""

    # Ensure export exissts
    if "export" not in session:
        session["export"] = []

    # Add selected word
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["export"].append(id)

        # To check the elements inside
        print(session["export"])
        return redirect("/")

    # GET
    words = db.execute("SELECT * FROM words WHERE id IN (?)", session["export"])
    print(words)
    return render_template("export.html", words=words)

@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure they provide username to the form
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure they provide password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        print(rows)

        if len(rows) != 1 or rows[0]["password"] != request.form.get("password"):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/clear")
def clear():
    """Simple clear button in export site"""

    if session["export"]:
        session.pop("export")
        return redirect("/")

    # Do nothing if none is left
    return redirect("/export")

@app.route("/popexport", methods=["POST"])
def popexport():
    """Delete buttons in export site"""

    # Retrieve an idea of the pre-export word
    id = request.form.get("id")

    # Remove the word element from export list accordingly
    if id in session["export"]:
        session["export"].remove(id)

    return redirect("/export")

@app.route("/edit", methods=["POST"])
@login_required
def edit():
    """Routing to the hidden edit site for either info changing or deleting"""
    id = request.form.get("id")
    if id:
        edit_word = db.execute("SELECT * FROM words WHERE id IN (?)", id)

    return render_template("edit.html", editword = edit_word[0])



@app.route("/savechange", methods=["POST"])
@login_required
def savechange():
    """Editing a word in the database"""
    thai = request.form.get("new_thai")
    pronunciation = request.form.get("new_pronunciation")
    meaning = request.form.get("new_meaning")
    id = request.form.get("id")

    # Update the word info accordingly
    db.execute("UPDATE words SET Thai = ?, Pronunciation = ?, Meaning = ? WHERE id = ?", thai, pronunciation, meaning, id)
    return redirect("/")

@app.route("/delete", methods=["POST"])
@login_required
def delete():
    """Delete a word in the database"""
    id = request.form.get("id")

    db.execute("DELETE FROM words WHERE id = ?", id)
    return redirect("/")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add new word into the words table"""
    if request.method == "POST":
        thai = request.form.get("thai")
        pronunciation = request.form.get("pronunciation")
        meaning = request.form.get("meaning")

        db.execute("INSERT INTO words (Thai, Pronunciation, Meaning) VALUES (?, ?, ?)", thai, pronunciation, meaning)
        return redirect("/add")

    return render_template("add.html")



