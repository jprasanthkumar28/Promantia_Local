from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
import erpnext
from frappe import _
from frappe.desk.treeview import get_all_nodes,get_children


class Supplier(Document):
    pass


@frappe.whitelist()
def get_root_supplier(supplier):
    root_supplier = supplier
    parent = frappe.db.get_value(
        'Supplier', {'name': supplier}, 'parent_Supplier')
    if parent:
        root_supplier = get_root_supplier(parent)
    return root_supplier


@frappe.whitelist()
def get_descendents(doctype, parent=None, **filters):
    if not parent or parent == "Supplier":
        return get_children(doctype)
    if parent:
        supplier_doc = frappe.get_cached_doc(
            "Supplier", parent)
        frappe.has_permission("Supplier", doc=supplier_doc, throw=True)
        child_suppliers = frappe.get_all('Supplier',
                                         fields=['parent_supplier',
                                                 'name as value', 'is_group'],
                                         filters=[
                                             ['parent_supplier', '=', parent]],
                                         order_by='idx')
        for supplier in child_suppliers:
            supplier.expanded = 0 if supplier.is_group == 0 else 1
            supplier.expandable = 0 if supplier.is_group == 0 else 1
        return child_suppliers
