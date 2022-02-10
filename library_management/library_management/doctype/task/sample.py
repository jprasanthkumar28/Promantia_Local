from __future__ import unicode_literals

import frappe

def on_save_validation(doc,method):
    # print(doc, method,"\n\n\n\n\n\n")
    # print(doc.project,"Project\n\n\n\n")

    # dictt = {}
    # for val in doc.assign_to:
    #     sales = frappe.db.sql("select sales_order from `tabProject` where name=%s", doc.project)
        # print(sales,"Sales Order\n\n\n\n")

        # name = frappe.db.sql("select name from `tabResource Planning` where sales_orders=%s", sales)
        # print(name,"\n\n\n\n")
        # use --> .getvalue



        # dictt[name] = val.assign_too

    # print(dictt,"\n\n\n\n")



    # for key,value in dictt.items():
    #     print(key," : ", value,"\n\n\n\n")
        
    #     desg = frappe.db.sql("select designation from `tabResource Planning Employee` where parent=%s", key)
    #     count = frappe.db.sql("select no_of_employees from `tabResource Planning Employee` where parent=%s", key)
    #     print(desg[0][0],count,"\n\n\n\n")

    #     if(desg[0][0] == "Tech Consultant" and (count[0][0] != 2)):
    #         print("Error")
    #         frappe.throw("Invalid Count, Cannot save the file ")
    #     elif(desg[0][0] == "Sr Tech Consultant" and (count[0][0] != 1)):
    #         frappe.throw("Invalid Count, Cannot save the file ")
    
    # print(frappe.session.user)