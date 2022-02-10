# Copyright (c) 2022, Prasanth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class EmployeeDeduction(Document):
    pass

@frappe.whitelist()
def add_data(doc, deduction_type=None, s_date=None, amount=None):

    s_date = s_date.split('-')
    
    month = datetime.date(1900, int(s_date[1]), 1).strftime('%b')
    
    onetime_amt = int(amount)
    recurring_amt = 0
    total =  onetime_amt + recurring_amt
    update_doc = {}
    update_doc.update({'month': month, 'recurring': recurring_amt, 'onetime': onetime_amt, 'total': total})

    return update_doc


@frappe.whitelist()
def update_recurring(doc, deduction_type=None, s_date=None, e_date=None, amount=None):
    s_date = s_date.split('-')
    e_date = e_date.split('-')

    onetime_amt = 0
    recurring_amt = int(amount)/(int(e_date[1])+1 - int(s_date[1]))
    total = onetime_amt + recurring_amt

    update_doc = []

    for i in range(int(s_date[1]), int(e_date[1])+1, 1):
        rec_month = datetime.date(1900, i, 1).strftime('%b')
        print(rec_month, "\n")
        update_doc.append({'month': rec_month, 'recurring': recurring_amt, 'onetime': onetime_amt, 'total': total})

    print(update_doc)
    return update_doc

@frappe.whitelist()
def get_month(doc, month, bal):
    name = frappe.db.get_value('Deduction Calculation', {'parent': doc, 'month': month}, ['name'])

    total = frappe.db.get_list('Deduction Calculation', {'parent': doc }, ['total'], pluck='total')
    print(doc, month ,"\n\n\n\n")
    print(sum(total), bal,"\n\nTotal\n")

    # frappe.db.set_value('Employee Deduction', doc , 'grand_total', sum(total)+int(bal))

    if name == None:
        return 0
    else:
        return name