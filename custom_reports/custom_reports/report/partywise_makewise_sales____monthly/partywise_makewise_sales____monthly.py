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
			

select
	DISTINCT
	si.customer,
    i.item_name,
    i.brand,
    
    sum(case when si.posting_date < '2021-01-01' then b.actual_qty else 0 end) jan_balance,
    
    sum(case when si.posting_date < '2021-02-01' then b.actual_qty else 0 end) feb_balance,
  
    sum(case when si.posting_date < '2021-03-01' then b.actual_qty else 0 end) mar_balance,
 
    sum(case when si.posting_date < '2021-04-01' then b.actual_qty else 0 end) apr_balance,
  
    sum(case when si.posting_date < '2021-05-01' then b.actual_qty else 0 end) may_balance,
  
    sum(case when si.posting_date < '2021-06-01' then b.actual_qty else 0 end) jun_balance,
  
    sum(case when si.posting_date < '2021-07-01' then b.actual_qty else 0 end) jul_balance,
  
    sum(case when si.posting_date < '2021-08-01' then b.actual_qty else 0 end) aug_balance,
    
    sum(case when si.posting_date < '2021-09-01' then b.actual_qty else 0 end) sep_balance,
  
    sum(case when si.posting_date < '2021-10-01' then b.actual_qty else 0 end) oct_balance,
    
    sum(case when si.posting_date < '2021-11-01' then b.actual_qty else 0 end) nov_balance,
    
    sum(case when si.posting_date < '2021-12-31' then b.actual_qty else 0 end) dec_balance,

	
          (sum(case when si.posting_date < '2021-01-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-02-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-03-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-04-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-05-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-06-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-07-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-08-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-09-01' then b.actual_qty else 0 end)+
          sum(case when si.posting_date < '2021-10-01' then b.actual_qty else 0 end)+
 		sum(case when si.posting_date < '2021-11-01' then b.actual_qty else 0 end)+
        sum(case when si.posting_date < '2021-12-31' then b.actual_qty else 0 end))Total
    
                     
                
			from 
            `tabBin`b,
            `tabSales Invoice Item`sii
            
            LEFT JOIN `tabSales Invoice` si ON sii.parent = si.name
            
            LEFT JOIN `tabItem` i ON sii.item_name = i.item_name AND sii.brand = i.brand
            

			where   si.customer = %(customer)s
            
GROUP BY i.item_name;


 """.format(conditions=conditions), filters, as_dict=1)
		
		return item

def get_conditions(filters):
        conditions = ""
        

        if filters.get("customer"):conditions += " and si.customer in %(customer)s"


        return conditions,filters


def get_columns(filters):

	return  [
		# {
		# 	"label": ("Customer Name"),
		# 	"fieldname": "customer",
		# 	"width": 120
		# },
		
		{
			"label": ("Brand"),
			"fieldname": "brand",
			"fieldtype": "Link",
			"options": "Brand",
			"width": 100
		},
		{
			"label": ("Jan"),
			"fieldname": "jan_balance",
			"width": 120
		},
		{
			"label": ("Feb"),
			"fieldname": "feb_balance",
			"width": 120
		},
		{
			"label": ("Mar"),
			"fieldname": "mar_balance",
			"width": 120
		},
		{
			"label": ("Apr"),
			"fieldname": "apr_balance",
			"width": 120
		},
		{
			"label": ("May"),
			"fieldname": "may_balance",
			"width": 120
		},
		{
			"label": ("Jun"),
			"fieldname": "jun_balance",
			"width": 120
		},
		{
			"label": ("Jul"),
			"fieldname": "jul_balance",
			"width": 120
		},
		{
			"label": ("Aug"),
			"fieldname": "aug_balance",
			"width": 120
		},
		{
			"label": ("Sep"),
			"fieldname": "sep_balance",
			"width": 120
		},
		{
			"label": ("Oct"),
			"fieldname": "oct_balance",
			"width": 120
		},
		{
			"label": ("Nov"),
			"fieldname": "nov_balance",
			"width": 120
		},
		{
			"label": ("Dec"),
			"fieldname": "dec_balance",
			"width": 120
		},
		{
			"label": ("Total"),
			"fieldname": "Total",
			"width": 120
		}


	
	]
