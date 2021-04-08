from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    _rec_name = 'sequence'

    sequence = fields.Char(string="Secuencia Tickets")
    display_name = fields.Many2one("sla_status_ids.ticket_id", string="Ticket")

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sequence.ticket')
        vals['helpdesk_ticket_id.id'] = vals['sequence']
        result = super(HelpdeskTicket, self).create(vals)
        return result
