from flask import Flask, render_template, url_for, redirect, request
import json
from datetime import datetime
import sqlite3
import os
from templates import Home


app=Flask(__name__)

current_directory=os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['POST'])
def journal():
    return render_template(Home.html)

if __name__=='__main__':
    app.run(debug=True)
