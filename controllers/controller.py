from flask import render_template
from app import app
from models.order_list import orders

@app.route("/orders")
def index():
    return render_template("index.html", dynamic_sitename="Home", activeOrders = orders)

@app.route("/orders/<index>")
def order(index):
    return render_template("order.html", currentOrder = orders[int(index)])

# STEVE'S VERSION OF THE ABOVE
# @app.route("/orders/<index>")
# def order(index):
#     chosen_order = orders[int(index)]
#     return render_template("order.html", order = chosen_order)

# render_template always takes the first argument as a webpage it renders - any other arguments are passed to the webpage
