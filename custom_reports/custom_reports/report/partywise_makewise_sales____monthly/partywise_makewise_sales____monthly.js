// Copyright (c) 2016, vals and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Partywise Makewise Sales  - Monthly"] = {
	"filters": [
		
					{
					 "fieldname":"from_date",
					 "label": __("From Date"),
					 "fieldtype": "Date",
					 "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
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
					},
					{
						"fieldname":"customer",
						"label":("Customer Name"),
						"fieldtype":"Link",
						"options":"Customer",
					},
					
					// {
					// 	"fieldname":"period",
					// 	"label": __("Period"),
					// 	"fieldtype": "Select",
					// 	"options": [
					// 		{ "value": "Monthly", "label": __("Monthly") },
					// 		{ "value": "Quarterly", "label": __("Quarterly") },
					// 		{ "value": "Half-Yearly", "label": __("Half-Yearly") },
					// 		{ "value": "Yearly", "label": __("Yearly") }
					// 	],
					// 	"default": "Monthly"
					// },
					
			]
		};
		