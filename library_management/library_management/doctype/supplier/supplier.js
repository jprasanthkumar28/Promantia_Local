var parent_supplier;
var report_manager;
frappe.ui.form.on('Supplier', {
	refresh: function (frm) {
		var supplier=''
		sessionStorage.setItem("Supplier Name",frm.doc.name);
		if (!frm.doc.__islocal) {
			frappe.call({
				method: "library_management.library_management.doctype.supplier.supplier.get_root_supplier",
				args: {
					supplier: frm.doc.name
				},
				async: false,
				callback: function (r) {
					supplier = r.message
				}
			})
		}
		frm.add_custom_button(__("Browse Tree View"), function () {
			frappe.route_options = {
				"supplier_name": supplier
			};
			frappe.set_route("Tree", "Supplier");
		});
	},
	is_group: function (frm) {
		if (frm.doc.is_group == 0) {
			frappe.call({
				method: "frappe.client.get_list",
				args: {
					doctype: "Supplier",
					fields: ["name"],
					filters: {
						'parent_supplier': frm.doc.name,
					},
					"limit_page_length": 0
				},
				callback: function (r) {
					if (r.message.length > 0) {
						frm.set_value("is_group", 1)
						frappe.validated = false;
						msgprint("Unable to change " + frm.doc.supplier_name + " from parent to child.")
					}
				}
			})
		}
	}
})
