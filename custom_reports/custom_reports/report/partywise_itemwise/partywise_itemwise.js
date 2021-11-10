// Copyright (c) 2016, vals and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Partywise Itemwise"] = {
	"filters": [
		
			{
			"fieldname":"customer",
			"label":("Customer"),
			"fieldtype":"Link",
			"options":"Customer",
			},
			{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -12),
			"reqd": 1,
			"width": "60px"
			},
			{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
			}



	]
};


// frappe.query_reports["Partywise Itemwise"] = {
// 	"filters": [
// 		{
// 			"fieldname":"month",
// 			"label": __("Month"),
// 			"fieldtype": "Select",
// 			"options": "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec",
// 			"default": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
// 				"Dec"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
// 		},
// 		{
// 			"fieldname":"year",
// 			"label": __("Year"),
// 			"fieldtype": "Select",
// 			"reqd": 1
// 		},
// 		{
// 			"fieldname":"employee",
// 			"label": __("Employee"),
// 			"fieldtype": "Link",
// 			"options": "Employee"
// 		},
// 		{
// 			"fieldname":"company",
// 			"label": __("Company"),
// 			"fieldtype": "Link",
// 			"options": "Company",
// 			"default": frappe.defaults.get_user_default("Company"),
// 			"reqd": 1
// 		}
// 	],

// 	"onload": function() {
// 		return  frappe.call({
// 			method: "erpnext.hr.report.monthly_attendance_sheet.monthly_attendance_sheet.get_attendance_years",
// 			callback: function(r) {
// 				var year_filter = frappe.query_report_filters_by_name.year;
// 				year_filter.df.options = r.message;
// 				year_filter.df.default = r.message.split("\n")[0];
// 				year_filter.refresh();
// 				year_filter.set_input(year_filter.df.default);
// 			}
// 		});
// 	}
// }