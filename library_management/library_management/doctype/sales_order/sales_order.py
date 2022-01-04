from __future__ import unicode_literals

import frappe
from frappe.model.document import Document



# def on_submit_test(doc, event):
#     print(doc.customer,"\n\n\n\n")

    # for row in doc.items:
    #     print(row.item_code,"<------\n\n")
    #     print(row.qty,"<------\n\n")
    #     print(row.rate,"<------\n\n")
    #     print(row.amount,"<------\n\n")

    # si_doc=frappe.get_doc(dict(doctype = 'Sales Invoice',
    #     customer = doc.customer,
    #     due_date = doc.delivery_date
    #     )).insert()
    # print(si_doc,"<========@======>")    
    # for row in doc.items:
    #     si_doc.append('items',{
    #         'item_code': row.item_code,
    #         'qty': row.qty,
    #         'rate': row.rate,
    #         'amount': row.amount
    #         })
    # # doc.insert()
    # si_doc.save()

def on_submit(doc,method):
    for row in doc.items:
        print(row.item_code,"<------\n\n")
        print(row.qty,"<------\n\n")
        print(row.rate,"<------\n\n")
        print(row.amount,"<------\n\n")
        print(row.delivery_date,"<------\n\n")
        print(row.uom,"<------\n\n")
        print(row.stock_uom,"<------\n\n")
        print(row.base_rate,"<------\n\n")
        print(row.base_amount,"<------\n\n")
        print(row.description,"<------\n\n")
        print(row.warehouse,"<------\n\n")
        print(row.conversion_factor,"<------\n\n")
        # print(row.tax_category,"<------\n\n")

    si_doc=frappe.get_doc(dict(doctype = 'Sales Invoice',
       company=doc.company,
       customer=doc.customer,
       due_date=doc.delivery_date,
       total_qty=doc.total_qty,
       total_net_weight=doc.total_net_weight,
       total=doc.total,
       grand_total=doc.grand_total,
       rounding_adjustment=doc.rounding_adjustment,
       rounded_total=doc.rounded_total,
       advance_paid=doc.advance_paid,
       base_grand_total=doc.base_grand_total,
       base_rounded_total=doc.base_rounded_total
    )).insert(ignore_mandatory=True)
    print(si_doc,"Debugger2<------\n\n\n")
    for val in doc.items:
        si_doc.append('items', {
           'item_code':val.item_code,
           'delivery_date':val.delivery_date,
           'qty':val.qty,
           'uom':val.uom,
           'stock_uom':val.stock_uom,
           'rate':val.rate,
           'amount':val.amount,
           'base_rate':val.base_rate,
           'base_amount':val.base_amount,
           'description':val.description,
           'warehouse':val.warehouse,
           'conversion_factor':val.conversion_factor
           # 'conversion_factor':val.tax_category
        })
    si_doc.save()
