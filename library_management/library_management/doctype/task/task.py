from __future__ import unicode_literals

import frappe

def on_save_validation(doc,method):
    # print(doc, method,"\n\n\n\n\n\n")
    designation_dict = {}
    for each in doc.assign_to:
        if each.designation in designation_dict:
            designation_dict[each.designation] += 1
        else:
            designation_dict[each.designation] = 1

    print(designation_dict,"\n\n\n\n")    

    # sales = frappe.db.sql("select sales_order from `tabProject` where name=%s", doc.project)
    # print(sales,"\n\n\n\n")

    # name = frappe.db.sql("select name from `tabResource Planning` where sales_orders=%s", sales)
    # print(name,"\n\n\n\n")

    # desg = frappe.db.sql("select no_of_employees from `tabResource Planning Employee` where parent=%s", name)
    # print(desg,"\n\n\n\n\n")