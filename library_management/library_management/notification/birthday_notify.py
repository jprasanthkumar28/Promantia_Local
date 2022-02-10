import frappe
import frappe.desk.doctype.notification_log.notification_log as notify
from datetime import date, datetime

def birthday():
    birth = date.today()

    employees_born_today = frappe.db.sql("""SELECT employee,employee_name FROM `tabEmployee` WHERE DAY(date_of_birth) = DAY('{today}') 
        AND MONTH(date_of_birth) = MONTH('{today}') AND `status` = 'Active'""".format(today=birth), as_list=True)
    # print(employees_born_today,"\n\n\n\n\n")
    # frappe.msgprint(employees_born_today)

  
    for employee in employees_born_today:
        user_list = frappe.db.sql("""SELECT user_id FROM `tabEmployee` where employee = %s """,(employee[0]), as_list=True)
        if user_list[0][0] != frappe.session.user:
            subject = f"Today is {employee[1]}'s Birthday"
            message = f"Today is {employee[1]}'s birthday"
        else:
            subject = f"Happy Birthday { employee[1]}"
            message = f"Happy Birthday { employee[1]}"
        # print(user_list)
        notify.enqueue_create_notification(user_list[0][0], 
            {'type': 'Alert', 'document_type': 'Employee', 'document_name': None, 'subject': subject, 'from_user': 'Administrator', 'email_content': message, 'attached_file': None})
