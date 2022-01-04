from __future__ import unicode_literals

import frappe

def on_submit(doc,method):
    print(doc.customer_name,"\n\n\n\n")
    # frappe.throw("Testing")
    for val in doc.items:
        print(val.item_code, doc.valid_till, val.qty, val.rate, val.amount, "\n\n\n\n")


    si_doc=frappe.get_doc(dict(doctype = 'Sales Order',
       customer=doc.customer_name,
       delivery_date=doc.valid_till,
       total_qty=doc.total_qty,
       total_net_weight=doc.total_net_weight,
       total=doc.total,
       grand_total=doc.grand_total,
       rounding_adjustment=doc.rounding_adjustment,
       rounded_total=doc.rounded_total,
       base_grand_total=doc.base_grand_total,
       base_rounded_total=doc.base_rounded_total
    )).insert(ignore_mandatory=True)
    print(si_doc,"Debugger2<------\n\n\n")
    for val in doc.items:
        si_doc.append('items', {
           'item_code':val.item_code,
           'delivery_date':doc.valid_till,
           'qty':val.qty,
           'rate':val.rate,
           'amount':val.amount
        })
    si_doc.save()
