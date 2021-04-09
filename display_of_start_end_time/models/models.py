from odoo import fields, models, api, exceptions
import re
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta

class Project(models.Model):
    _inherit = "project.task"

    _date_start = fields.Datetime(string='Fecha inicio', index=True, copy=False)
    _date_end = fields.Datetime(string='Fecha final', index=True, copy=False)

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    _date_start = fields.Datetime(string='Fecha inicio', index=True, copy=False)
    _date_end = fields.Datetime(string='Fecha final', index=True, copy=False)
