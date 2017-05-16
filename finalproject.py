from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page will show all my restaurants"

@app.route('/restaurant/new')
def newRestaurant():
    return "This page will be for making a new restaurant"

@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
    return "This page will be for editing restraunt %s" % restaurant_id

@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
    return "This page will be fore deleting restaurant %s" % restaurant_id

@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
    return "This page is the menu for restaurant %s" % restaurant_id

@app.route('/restaurant/restaurant_id/menu/new')
def newMenuItem():
    return "This Page is for making a new menu item for restraunt %s" % restaurant_id

@app.route('/restaurant/restaurant_id/menu/menu_id/edit')
def editMenuItem():
    return "This page is for editing menu item %s" % menu_id

@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def deleteMenuItem():
    return "This page is for deleting menu item %s" % menu_id

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
