# -*- coding: utf-8 -*-
"""
    Author: Tobias Reinwarth (tobias.reinwarth@manatec.de)
    Copyright: 2019, manaTec GmbH
    Date created: 25.01.19
"""

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    DESCRIPTION_FIELD_NAME = 'name'
    HELPDESK_TICKET_FIELD_NAME = 'helpdesk_ticket_id'

    @api.multi
    def write(self, vals):
        if self.DESCRIPTION_FIELD_NAME in vals and vals.get(self.DESCRIPTION_FIELD_NAME) and self.helpdesk_ticket_id:
            value = ' | #%s' % self.helpdesk_ticket_id.id
            if not vals.get(self.DESCRIPTION_FIELD_NAME, "").find(value):
                vals.update({self.DESCRIPTION_FIELD_NAME: "%s%s" % (vals.get(self.DESCRIPTION_FIELD_NAME), value)})

        super(AccountAnalyticLine, self).write(vals)

    @api.model
    def create(self, vals):
        if self.DESCRIPTION_FIELD_NAME in vals and vals.get(self.DESCRIPTION_FIELD_NAME) and vals.get(self.HELPDESK_TICKET_FIELD_NAME, False):
            value = ' | #%s' % vals.get(self.HELPDESK_TICKET_FIELD_NAME)
            if not vals.get(self.DESCRIPTION_FIELD_NAME, "").find(value):
                vals.update({self.DESCRIPTION_FIELD_NAME: "%s%s" % (vals.get(self.DESCRIPTION_FIELD_NAME), value)})

        return super(AccountAnalyticLine, self).create(vals)
