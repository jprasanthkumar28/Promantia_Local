// Copyright (c) 2022, Prasanth and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Deduction', {
	onload: function (frm) {
		frm.get_field("deduction_calculation").grid.cannot_add_rows = true;

		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-delete-row').hide();
		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-duplicate-row').hide();
		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-move-row').hide();
		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-append-row').hide();
		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-insert-row-below').hide();
		// frm.fields_dict["deduction_calculation"].grid.wrapper.find('.grid-insert-row').hide();
	}
});


//For Trigerring end_date based on the start_date
frappe.ui.form.on("Deduction Details", {

	before_deduction_details_remove: function(frm, cdt, cdn) {
    	var row = locals[cdt][cdn];
    	if (row.deduction_type === "Onetime") {
	    	alert(row.amount)
    		frappe.call({
				method: "library_management.library_management.doctype.employee_deduction.employee_deduction.add_data",
				args: {
						doc: frm.doc.name,
						deduction_type: row.deduction_type,
						s_date: row.start_date,
						amount: row.amount
					},
				async:false,
				callback: function(result) {
				var onetime = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'onetime')
				var namee = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'name')
				var prev_total = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'total')

				var new_onetime = parseFloat(onetime) - parseFloat(row.amount)
				var new_total = parseFloat(prev_total) - parseFloat(row.amount)
				console.log(new_onetime);

				frappe.model.set_value('Deduction Calculation', namee, { "onetime": new_onetime, "total": new_total})
				cur_frm.refresh_field("deduction_calculation")
				}
			});
    	}
    	else if (row.deduction_type === "Recurring") {
	    	// alert(row.amount)
    		frappe.call({
				method: "library_management.library_management.doctype.employee_deduction.employee_deduction.update_recurring",
				args: {
						doc: frm.doc.name, 
						deduction_type: row.deduction_type, 
						s_date: row.start_date,
						e_date: row.end_date,
						amount: row.amount
					},
				async:false,
				callback: function(result) {
					// alert(result.message.length)
					for (const element of result.message) {
						console.log(element['month']);
						var recurring = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'recurring')
						var namee = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'name')
						var prev_total = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'total')

						var new_recurring = parseFloat(recurring) - parseFloat(row.amount)/result.message.length
						var new_total = parseFloat(prev_total) - parseFloat(row.amount)/result.message.length
						console.log(new_recurring);

						frappe.model.set_value('Deduction Calculation', namee, { "recurring": new_recurring, "total": new_total})
						cur_frm.refresh_field("deduction_calculation");
					}
				}
			});
    	}

	},

	"start_date": function(frm, cdt, cdn) {
    	var row = locals[cdt][cdn];
    	if (row.deduction_type === "Onetime") {

    		var arr1 = row.start_date.split('-');
    		var d = new Date(Number(arr1[2]),Number(arr1[1]),0);
			var n = d.getDate();
			var result = n + "-" + arr1[1] + "-" + arr1[0]

			// alert(result);

			frappe.call({
				method: "library_management.library_management.doctype.employee_deduction.employee_deduction.get_end_date",
				args: {
					e_date: result
				},
				async:false,
				callback: function(result) {
					frappe.model.set_value("Deduction Details", row.name, { 'end_date': result.message})
					// alert(result.message);
				}
			});

    	}
	}
});

//For adding data to deduction calculation table
frappe.ui.form.on("Deduction Details", {
    "amount": function(frm, cdt, cdn) {
    	var row = locals[cdt][cdn];
        // frappe.msgprint("Changed deduction type");
        if (row.deduction_type === "Onetime") {
	        //START
	        frappe.call({
				method: "library_management.library_management.doctype.employee_deduction.employee_deduction.add_data",
				args: {
						doc: frm.doc.name,
						deduction_type: row.deduction_type,
						s_date: row.start_date,
						amount: row.amount
					},
				async:false,
				callback: function(result) {
					var child = cur_frm.add_child("deduction_calculation");

					frappe.call({
						method: "library_management.library_management.doctype.employee_deduction.employee_deduction.get_month",
						args: {
							doc: frm.doc.name,
							month: result.message['month'],
							bal: result.message['onetime']
						},
						async:false,
						callback: function(result1) {
							if (result1.message.length === 0 || result1.message === 0) {
								frappe.model.set_value(child.doctype, child.name, { "month": result.message['month'], "onetime": result.message['onetime'], "recurring": "0", "total": result.message['total']})
								
								cur_frm.refresh_field("deduction_calculation")
							}
							else {
								var prev_total = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'total')
								var onetime = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'onetime')
								var recurring = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': result.message['month'] }, 'recurring')
								var total = result.message['total'] + Number(prev_total)
								// console.log(total)
								frappe.model.set_value(child.doctype, result1.message, { "month": result.message['month'], "onetime": onetime + result.message['onetime'], "recurring": recurring, "total": total})
								cur_frm.refresh_field("deduction_calculation")
							}
						}

					});
				}
			});
			//End
        }
        else if (row.deduction_type === "Recurring") {
        	frappe.call({
				method: "library_management.library_management.doctype.employee_deduction.employee_deduction.update_recurring",
				args: {
						doc: frm.doc.name, 
						deduction_type: row.deduction_type, 
						s_date: row.start_date,
						e_date: row.end_date,
						amount: row.amount
					},
				async:false,
				callback: function(result) {
					console.log(result.message);

					for (const element of result.message) {
						// alert(element['month']);
						var child = cur_frm.add_child("deduction_calculation");

						frappe.call({
						method: "library_management.library_management.doctype.employee_deduction.employee_deduction.get_month",
						args: {
							doc: frm.doc.name,
							month: element['month'],
							bal: element['recurring']
						},
						async:false,
						callback: function(result1) {
							if (result1.message.length === 0 || result1.message === 0) {
								frappe.model.set_value(child.doctype, child.name, { "month": element['month'], "onetime": "0", "recurring": element['recurring'], "total": element['total']})
								cur_frm.refresh_field("deduction_calculation")
							}
							else {
								var prev_total = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'total')
								var recurring = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'recurring')
								var onetime = frappe.model.get_value('Deduction Calculation', {'parent': frm.doc.name, 'month': element['month'] }, 'onetime')
								var total = element['total'] + Number(prev_total)
								// console.log(total)
								frappe.model.set_value(child.doctype, result1.message, { "month": element['month'], "onetime": onetime, "recurring": recurring + element['recurring'], "total": total})
								cur_frm.refresh_field("deduction_calculation")
							}
						}

					});
					}
				}
			});
			//End
        }
        else {
        	alert("Please select deduction type");
        }
    }
});