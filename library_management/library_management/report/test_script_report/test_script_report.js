// Copyright (c) 2016, Prasanth and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Test Script Report"] = {
	"filters": [
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ['', 'Available','Issued'],
			"reqd": 0
		}

	]
};
