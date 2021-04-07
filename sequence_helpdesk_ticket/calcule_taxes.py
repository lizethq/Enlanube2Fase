from odoo import models, fields, api

class accountPayment(models.Model):
    _inherit = 'account.payment'
    
    def taxes(self):
        taxes = {
			'name': [],
			'tax_percentage': [],
			'product_value': [],
			'tax_value': []
		}		
        for line in self.reconciled_invoice_ids.invoice_line_ids:
            for tax in line.tax_ids:
                if 'RTE' in tax.name:
                    if tax.name in taxes['name']:
                        index = taxes['name'].index(tax.name)
                        taxes['product_value'][index] = taxes['product_value'][index] + line.price_subtotal
                    else:
                        taxes['name'].append(tax.name)
                        taxes['tax_percentage'].append(tax.amount)
                        taxes['product_value'].append(line.price_subtotal)	
        for x in range(len(taxes['product_value'])):
            retained_value = taxes['product_value'][x] * (taxes['tax_percentage'][x]/100)
            taxes['tax_value'].append(retained_value)
        taxes['total_retained'] = sum(taxes['tax_value'])				
        return taxes
    
    def busqueda(self, nombre):        
        wt = self.env['account.move']
        id_needed = wt.search([('name', '=', nombre)]).id
        new = wt.browse(id_needed)        
        return new

class accountMove(models.Model):
    _inherit = 'account.move'
    
    def taxes(self):
        taxes = {
			'name': [],
			'tax_percentage': [],
			'product_value': [],
			'tax_value': []
		}		
        for line in self.invoice_line_ids:
            for tax in line.tax_ids:                
                if tax.name in taxes['name']:
                    index = taxes['name'].index(tax.name)
                    if line.price_subtotal != 0:                     
                        taxes['product_value'][index] = taxes['product_value'][index] + line.price_subtotal
                    elif line.credit != 0:
                        taxes['product_value'][index] = taxes['product_value'][index] + line.credit
                    elif line.debit != 0:
                        taxes['product_value'][index] = taxes['product_value'][index] + line.debit
                else:
                    taxes['name'].append(tax.name)
                    taxes['tax_percentage'].append(tax.amount)
                    if line.price_subtotal != 0:                     
                        taxes['product_value'].append(line.price_subtotal)	
                    elif line.credit != 0:
                        taxes['product_value'].append(line.credit)	
                    elif line.debit != 0:
                        taxes['product_value'].append(line.debit)
        for x in range(len(taxes['product_value'])):
            retained_value = taxes['product_value'][x] * (taxes['tax_percentage'][x]/100)
            taxes['tax_value'].append(retained_value)
        taxes['total_retained'] = sum(taxes['tax_value'])				
        return taxes
    