# Copyright (c) 2013, rangsutra_app and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	conditions = get_conditions(filters)
	data = get_data(filters,conditions)
	chart = get_chart_data(data)
	return columns, data, None, chart

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
	if filters.get('creation'):
		conditions += "and DATE(creation) <= '{}'".format(filters.get('creation'))
	return conditions


def get_chart_data(data):
	print("In Get Chart")

	labels = []
	labels1 = []
	avail = []
	issued = []
	for con in data:
		if con.status == 'Available':
			avail.append(con.status)
		else:
			issued.append(con.status)
	labels.append(len(avail))
	labels1.append(len(issued))

	return {
		"data": {
			'labels': ['Available', 'Issued'],
			'datasets': [
				{
					"name": "Available",
					"values": labels[:10]
				},
				{
					"name": "Issued",
					"values": labels1[:10]
				}
			]
		},
		"type": "bar",
		"colors": ["#fc4f51","#ffd343"],
		"barOptions": {
			"stacked": False
		}
	}
