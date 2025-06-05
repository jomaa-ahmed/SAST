from flask import Flask, request
import sqlite3, subprocess, json

app = Flask(__name__)

@app.route("/user")
def user():
    name = request.args.get("name", "")
    # BUG 1 – SQL injection
    rows = sqlite3.connect(":memory:")\
          .execute("SELECT * FROM users WHERE name = '" + name + "';")\
          .fetchall()
    return json.dumps([dict(r) for r in rows])

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # BUG 2 – command injection
    out = subprocess.check_output("ping -c 1 " + host, shell=True)
    return out

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    # BUG 3 – unsafe eval
    return str(eval(expr))
