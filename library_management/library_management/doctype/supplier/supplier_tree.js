
frappe.treeview_settings["Supplier"] = {
    get_tree_nodes: 'library_management.library_management.doctype.supplier.supplier.get_descendents',
    filters: [
        {
            fieldname: "supplier_name",
            fieldtype: "Link",
            options: "Supplier",
            label: "Supplier",
            hidden: true,
        }
    ],
    title: "Supplier",
    breadcrumb: "Buying",
    disable_add_node: true,
    root_label: "Supplier",//fieldname from filters
    get_tree_root: false,
    show_expand_all: true,
    get_label: function (node) {
        
        var supplier_name = sessionStorage.getItem("Supplier Name")
        if (node.data.value == supplier_name) {
            var supplier = '<b>' + node.data.value + '</b>'
            return supplier
        }
        else {
            return node.data.value
        }
    },
    onload: function (me) {
        var supplier_name = sessionStorage.getItem("Supplier Name")
        // alert(supplier_name);
        me.page.add_inner_button(__('Back'), function () {
            frappe.set_route('Form', 'Supplier', supplier_name);
        });
        var label = frappe.get_route()[0] + "/" + frappe.get_route()[1];
        if (frappe.pages[label]) {
            delete frappe.pages[label];
        }

        var filter = me.opts.filters[0];
        if (frappe.route_options && frappe.route_options[filter.fieldname]) {
            var val = frappe.route_options[filter.fieldname];
            delete frappe.route_options[filter.fieldname];
            filter.default = "";
            me.args[filter.fieldname] = val;
            me.root_label = val;
            me.page.set_title(val);
        }
        me.make_tree()
    },
}
