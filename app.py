# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá, mundo da AWS com Terraform e Ansible!"
