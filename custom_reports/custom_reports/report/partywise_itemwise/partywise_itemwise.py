# Copyright (c) 2013, vals and contributors
# For license information, please see license.txt

# import frappe

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	conditions, filters = get_conditions(filters)
	columns = get_columns(filters)
	# columns2 = get_columns2(filters)
	# test = get_mapped_pri_records(conditions,filters)
	data = get_data(conditions,filters)

	return columns,data


def get_data(conditions,filters):
	
	
        
		
		item = frappe.db.sql(""" 

		select DISTINCT  si.customer,
				sii.item_code,
				sii.item_name,
				sii.packaging,
                SUM(DISTINCT sii.qty),
				
				sii.is_free_item,
               	SUM(DISTINCT sii.amount)  / SUM(DISTINCT sii.qty),
                SUM(DISTINCT sii.amount)



			from 
			`tabSales Invoice`si,
			`tabSales Invoice Item`sii



			where sii.parent = si.name and customer = %(customer)s
	GROUP BY sii.item_name;

 """.format(conditions=conditions), filters, as_dict=1)
		
 
		return item

def get_conditions(filters):
        conditions = ""
        

        if filters.get("customer"):conditions += " and si.customer in %(customer)s"

		
        
    
 
        return conditions,filters


 
def get_columns(filters):

	return  [
		# {
		# 	"fieldname":"customer",
		# 	"label":("Customer"),
		# 	"fieldtype":"Link",
		# 	"options":"Customer",
		# },
		{
			"label": ("Item code"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 100
		},
		{
			"label": ("Item Name"),
			"fieldname": "item_name",
			"width": 120
		},
		{
			"label": ("Pack"),
			"fieldname": "packaging",
			"width": 120
		},
		{
			"label": ("Qty"),
			"fieldname": "SUM(DISTINCT sii.qty)",
			"width": 50
		},
		{
			"label": ("Free"),
			"fieldname": "is_free_item",
			"width": 80
		},
		{
			"label": ("Avg.Rate"),
			"fieldname": "SUM(DISTINCT sii.amount)  / SUM(DISTINCT sii.qty)",
			"width": 120
		},
		{
			"label": ("Amount"),
			"fieldname": "SUM(DISTINCT sii.amount)",
			"width": 120
		}


	]
