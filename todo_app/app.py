from flask import Flask, render_template, request, redirect, url_for
import requests
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_cards, post_add, update_status, get_card, delete_card, get_lists
from todo_app.data.Item import Item
from todo_app.data.viewmodel import ViewModel



def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config())#


    @app.route('/')
    def index():
        right_list = get_lists()[-1]["name"]
        items=get_cards()
        items=sorted (items,key=lambda item: item.status, reverse=True)
        view_model=ViewModel (items,right_list)
        return render_template ('index.html', view_model=view_model)

    @app.route('/Add', methods=['POST'])
    def Add():
        title = request.form.get ("title")
        post_add (title)
        return redirect (url_for("index"))

    @app.route('/update/<id>')
    def update(id):

        update_status (id)
        return redirect (url_for("index"))

    @app.route('/delete/<id>')
    def delete(id):
        delete_card (id)
        return redirect (url_for("index"))
        
    return app