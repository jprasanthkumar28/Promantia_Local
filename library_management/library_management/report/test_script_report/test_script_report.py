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
	labels = []
	date_per = []
	completed = []
	bill_per = []

	for order in data:
		labels.append(order.name)
		date_per.append(order.date_percentage)
		completed.append(order.per_delivered)
		bill_per.append(order.per_billed)

	return {
		"data": {
			'labels': labels[:30],
			'datasets': [
				{
					"name": "Date %",
					"values": date_per[:30]
				},
				{
					"name": "Delivered %",
					"values": completed[:30]
				},
				{
					"name": "Billed %",
					"values": bill_per[:30]
				}
			]
		},
		"type": "bar",
		"colors": ["#fc4f51", "#ffd343","#00FF00"],
		"barOptions": {
			"stacked": False
		}
	}