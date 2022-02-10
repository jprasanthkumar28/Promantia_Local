from . import __version__ as app_version

app_name = "library_management"
app_title = "Library Management"
app_publisher = "Prasanth"
app_description = "We will build a simple Library Management System in which the Librarian can log in and manage Articles and Memberships."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = ";"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_js = "/assets/js/aka.min.js"

doctype_js = {
	"Supplier" : "library_management/doctype/supplier/supplier.js",
	"Customer" : "library_management/doctype/customer/customer.js"
	# ,
	# "Employee Deduction" : "library_management/doctype/employee_deduction/employee_deduction.js"
}


doctype_tree_js = {"Supplier" : "library_management/doctype/supplier/supplier_tree.js"}


fixtures = ["Server Script",
{"dt": "Custom Field",
		"filters": [
        [
        "name","in",[
		"Supplier-is_group",
		"Supplier-parent_supplier"
		]
		]
	]
},
{"dt": "Property Setter",
		"filters":[
	["name","in",[
		"Supplier-address_contacts-label",
		"Supplier-contact_html-permlevel",
		"Item Supplier-supplier_part_no-hidden",
		"Item Supplier-supplier_part_no-in_list_view",
		"Customer-customer_name-in_list_view"	
	]
	]
	
]
},
{"dt": "Custom Field",
		"filters":[
	["name","in",[
		"Customer-customer_test_field"
	]
	]
	
]
}
]

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Quotation": {
		"before_submit": "library_management.library_management.doctype.quotation.quotation.on_submit"
	},
	"Task": {
		"before_save": "library_management.library_management.doctype.task.task.on_save_validation"
	},
	"Article": {
		"before_save": "library_management.library_management.doctype.article.article.db_API"
	}
}

# birthday_notify = [
# 	"library_management.library_management.notification.birthday_notify.birthday",
# ]


# on_session_creation = [
# 	"library_management.library_management.notification.birthday_notify.birthday",
# ]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"cron": {
# 		"0 10 * * *": [
# 			"library_management.library_management.notification.birthday_notify.birthday",
# 		]
# 	}
# }
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	]
	# "hourly": [
	# 	"library_management.library_management.notification.birthday_notify.birthday",
	# ],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	]

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
 	"Customer": "library_management.library_management.doctype.customer.customer_dashboard.get_dashboard_data"
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

