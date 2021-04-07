# -*- coding: utf-8 -*-
# BY: Luis Felipe Paternina - 
#
# lfpaternina93@gmail.com
#
# +57 3215062357 or +57 3046079971
#
# Bogota, Colombia
#
###############################################################################################

from odoo import fields, models, api, exceptions
import re
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta



class Project(models.Model):
    _inherit = "project.task"

    email2 = fields.Char(string="Correo 2")
    name = fields.Char(copy=False, default='New', readonly=True)
    number = fields.Integer()


    @api.model
    def create(self, vals):
    	if vals.get('name', 'New') == 'New':
    		vals['name'] = self.env['ir.sequence'].next_by_code('task.lfpv') or 'New'

    	result = super(Project, self).create(vals)
    	return result



   







    





   

    		

    
    
 
 
   

   

    

    
                


    

    
