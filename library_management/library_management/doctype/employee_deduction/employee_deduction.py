# Copyright (c) 2022, Prasanth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


class EmployeeDeduction(Document):
    def validate(self):
        bal = 0
        total_bal = 0

        today = date.today()
        today = str(today).split('-')
        month = datetime.date(1900, int(today[1]), 1).strftime('%b')
        month = month + "-" + today[0]

        for row in self.deduction_calculation:
            if row.total == 0:
                frappe.db.sql("""delete from `tabDeduction Calculation` where name = %s""", row.name)  
                # self.reload()
            bal = row.total - row.actual_paid

            row.balance = bal
            if row.month == month:
                self.month_total_balance = bal

            for ind in range(1,13):
                rec_month = datetime.date(1900, ind, 1).strftime('%b')
                rec_month = rec_month + "-" + today[0]
                # print(int(today[1]))
                if int(today[1]) >= ind and row.month == rec_month:
                    print(rec_month,"=", row.month, "\n\n\n")
                    bal = row.total - row.actual_paid
                    total_bal += bal

        self.grand_total = total_bal

 
@frappe.whitelist()
def add_data(doc, deduction_type=None, s_date=None, amount=None):

    s_date = s_date.split('-')

    month = datetime.date(1900, int(s_date[1]), 1).strftime('%b')
    month = month + "-" + s_date[0]

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
        rec_month = rec_month + "-" + s_date[0]
        
        print(rec_month, "\n")
        update_doc.append({'month': rec_month, 'recurring': recurring_amt, 'onetime': onetime_amt, 'total': total})

    # print(update_doc)
    return update_doc

@frappe.whitelist()
def get_month(doc, month, bal):
    name = frappe.db.get_value('Deduction Calculation', {'parent': doc, 'month': month}, ['name'])

    if name == None:
        return 0
    else:
        return name



@frappe.whitelist()
def get_end_date(e_date):
    print(e_date)
    # e_date = datetime.date(2022, 2, 16) + relativedelta(day=31)
    # formatted_date = datetime.strptime(e_date, "%d-%m-%Y")
    date = datetime.datetime.strptime(e_date, "%d-%m-%Y")

    # # frappe.db.set_value('Deduction Details', {'parent': doc} , 'end_date', formatted_date)
    print(type(date) ,"\n\n\n")
    return date
