// Copyright (c) 2021, Prasanth and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer', {
	refresh: function(frm) {
		console.log(frm.doc.name);
		frappe.call({
				method: 'library_management.library_management.doctype.customer.customer.onload',
                args: {
                    doc: frm.doc.name
                },
                callback: function(r) {                	
                    console.log(r);
                	frm.set_df_property('contacts_test','options', r.message)
                	frm.refresh_fields();
                }
            });
	}
});

