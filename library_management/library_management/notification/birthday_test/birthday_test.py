from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	pass

def sendmail():         
    content = "Test Content"
    recipient = self.email
    frappe.sendmail(recipients=[recipient],
        sender="prashu0561@gmail.com",
        subject="Test Subject", content=content)