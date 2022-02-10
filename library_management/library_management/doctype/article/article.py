# Copyright (c) 2021, Prasanth and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	pass

def db_API(doc,method):
	# print("\n\nCheck\n\n")
	subject, description = frappe.db.get_value('Article', 'Death', ['status', 'description'])
	print(subject, description, "\n\n\n\n")


	db_exists = frappe.db.exists({
	    'doctype': 'Article',
	    'status': 'Issued'
	})

	print(db_exists)

	# total number of Article records
	db_count = frappe.db.count('Article')
	print(db_count)
	# total number of Issed Articles
	db_count1 =	frappe.db.count('Article', {'status': 'Issued'})
	print(db_count1)

	frappe.db.set_value('Article', 'Eenadu', {
		'isbn': 'Eenadu ISBN',
   		'description': 'Total number of Article recordss --> '+ str(db_count) + '\n\n\n\n' + 'Total number of Issued Article records --> '+ str(db_count1) 
	})

	#To delete a table or table data 
	db_exists2 = frappe.db.exists({
	    'doctype': 'Article',
	    'name': 'Test4'
	})
	print(db_exists2,"\n\n\n\n\n\n")
	if any(item[0] == 'Test4' for item in db_exists2):
		frappe.db.delete("Article", {
	    	"name": ("=", 'Test4')
		})
	# else:
	# 	frappe.publish_realtime(event='eval_js', message='alert("No article with that name")')

	# desc = frappe.db.describe('Article')
	# frappe.throw(desc)
	# frappe.db.change_column_type('Article', 'description', 'text')

	# frappe.throw(
 #    	title='Error',
 #    	msg='This file does not exist',
 #    	exc=FileNotFoundError
	# )
	query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
	print(query,"\n\nQuery\n\n")

	url = doc.get_url()

	print("\n\n\n\n\n",url)

	doc.reload()