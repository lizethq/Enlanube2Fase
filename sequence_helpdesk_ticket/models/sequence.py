from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    _rec_name = 'sequence'

    sequence = fields.Char(copy=False, string='Secuencia Tickets', invisible=True)

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket')
        result = super(HelpdeskTicket, self).create(vals)
        return result
