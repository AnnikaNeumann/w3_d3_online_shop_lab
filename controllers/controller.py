from flask import render_template, url_for
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = "Home", orders=orders)

@app.route('/orders/<index>')
def get_order(index):
    order = orders[int(index)]
    return render_template("order.html", title = index , order = order)

