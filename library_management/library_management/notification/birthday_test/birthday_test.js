frappe.ui.form.on('Employee', {
	refresh: function(frm) {
		console.log(frm.doc.name);
		frappe.call({
			// method: 'library_management.library_management.notification.birthday_test.birthday_test',
			method: 'frappe.core.doctype.communication.email.make',
            args: {
                communication_medium:"System Notification"
            },
            callback: function(r) {            	
                console.log(r);
            }
        });
	}
});