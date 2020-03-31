from flask  import Flask
import psycopg2
from flask  import render_template, url_for, flash, redirect
from item_find.database import database_retrieve


app = Flask(__name__)

name = 'Star Market'
location = [42.352399, -71.123364]

# name = 'Trader Joes'
# location = [42.342306, -71.120524]

rows, area = database_retrieve(name,location)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/items")
def items():
    return render_template('items.html',area=area, rows=rows)


#starmarket 42.352399, -71.123364   '42.352399-71.123364'
#trader joes 42.342306, -71.120524   '42.342306-71.120524'
#target 42.350903, -71.114086      '42.350903-71.114086'
