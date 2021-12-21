from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item, get_item
app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items=get_items()
    items=sorted (items,key=lambda item: item["status"], reverse=True)
    return render_template ('index.html', items=items)

@app.route('/Add', methods=['POST'])
def Add():
    title = request.form.get ("title")
    add_item (title)
    return redirect (url_for("index"))

@app.route('/update/<id>')
def update(id):
    item = get_item(id)
    item ["status"] = "Completed"
    save_item (item)
    return redirect (url_for("index"))
