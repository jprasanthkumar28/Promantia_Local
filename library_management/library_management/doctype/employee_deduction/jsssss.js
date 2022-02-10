// Copyright (c) 2022, Prasanth and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Deduction', {
	// refresh: function(frm) {

	// }
});

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
							alert(result1.message);
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
						alert(element['month']);
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


