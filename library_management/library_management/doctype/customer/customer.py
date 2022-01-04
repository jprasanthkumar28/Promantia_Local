# Copyright (c) 2021, Prasanth and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Customer(WebsiteGenerator):
	pass

@frappe.whitelist()
def onload(doc):
	listt = frappe.db.sql(""" select c.first_name from tabContact c 
            INNER JOIN tabCustomer tcc  on c.first_name=tcc.customer_name
            where  c.designation ='Tech Consultant'""", as_dict=True)
	print(listt)
	return get_data(listt)

def get_data(doc):
	print(doc,"Testttttttttttttttttttttt")
	return frappe.render_template(
		"templates/includes/Test_contacts.html", {'doc':doc}
	)
