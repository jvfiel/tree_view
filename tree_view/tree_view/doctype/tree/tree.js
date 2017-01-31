// Copyright (c) 2016, MN Tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tree', {
	refresh: function(frm) {

	}

});

frappe.ui.form.on('Tree', {
	save_file: function (doctype, docname, callback) {
		/*var d = new frappe.ui.Dialog({
			title: __("Rename {0}", [__(docname)]),
			fields: [
				{label: __("New Name"), fieldname: "new_name", fieldtype: "Data", reqd: 1, "default": docname},
				{label: __("Merge with existing"), fieldtype: "Check", fieldname: "merge"},
			]
		});
		d.set_primary_action(__("Rename"), function () {
			var args = d.get_values();
			if (!args) return;
			return frappe.call({
				method: "frappe.model.rename_doc.rename_doc",
				args: {
					doctype: doctype,
					old: docname,
					"new": args.new_name,
					"merge": args.merge
				},
				btn: d.get_primary_btn(),
				callback: function (r, rt) {
					if (!r.exc) {
						$(document).trigger('rename', [doctype, docname,
							r.message || args.new_name]);
						if (locals[doctype] && locals[doctype][docname])
							delete locals[doctype][docname];
						d.hide();
						if (callback)
							callback(r.message);
					}
				}
			});
		});
		d.show();*/
		if (cur_frm.doc.attachment) {
			return frappe.call({
				method: "frappe.model.rename_doc.rename_doc",
				args: {
					doctype: "Tree",
					old: cur_frm.doc.name,
					//"new": args.new_name,
					"new": cur_frm.doc.new_name,
					"merge": 0,
					"ignore_permissions": 1,
				},
				callback: function (r, rt) {
					//callback(r.message);
					if (!r.exc) {
						$(document).trigger('rename', [doctype, docname,
							r.message || args.new_name]);
						if (locals[doctype] && locals[doctype][docname])
							delete locals[doctype][docname];
						//d.hide();
						//if (callback)
						//	callback(r.message);
						frappe.set_route("Form", "Tree", cur_frm.doc.new_name)
					}
				}
			});
		}
		else
		{
			//this.frm.save();
		}
	},
});