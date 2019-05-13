from flask import *
from flask_table import Table, Col
import os
import scrape

app = Flask(__name__)

@app.route('/')
def home():
	# Declare your table
    class ItemTable(Table):
    	name = Col('Name')
    	description = Col('Description')

	# Get some objects
	class Item(object):
		def __init__(self, name, description):
			self.name = name
			self.description = Description
			items = [Item('Name1', 'Description1'),
			Item('Name2', 'Description2'),
			Item('Name3', 'Description3')]
		# Or, equivalently, some dicts
		items = [dict(name='Name1', description='Description1'),
         	dict(name='Name2', description='Description2'),
        	dict(name='Name3', description='Description3')]

	# Or, more likely, load items from your database with something like

	# Populate the table
	table = ItemTable(items)
	# Print the html
	print(table.__html__())
	# or just {{ table }} from within a Jinja template
    flash(scrape.getTotal('nanoluck'))
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)

