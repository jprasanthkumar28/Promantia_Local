# Copyright (c) 2013, rangsutra_app and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	conditions = get_conditions(filters)
	data = get_data(filters,conditions)
	return columns, data

def get_columns():
	columns = [
		{
			"fieldname": "article_name",
			"label": _("Article Name"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "status",
			"label": _("Status/Availablity"),
			"fieldtype": "Select",
			"width": 200
		},
		{
			"fieldname": "publisher",
			"label": _("Publisher"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "description",
			"label": _("Description"),
			"fieldtype": "data",
			"width": 200
		},
		{
			"fieldname": "image",
			"label": _("Image"),
			"fieldtype": "Attach Image",
			"width": 200
		}
	]
	return columns

def get_data(filters,conditions):
	query="""select article_name, status, publisher, description, image from tabArticle where docstatus=0 {conditions}""".format(conditions=conditions)
	orders=frappe.db.sql(query, as_dict=True)
	return orders

def get_conditions(filters):
	conditions=""
	if filters.get('status'):
		conditions += "and status = '{}'".format(filters.get('status'))
	if filters.get('status'):
		conditions += "and author = '{}'".format(filters.get('author'))
	return conditions


