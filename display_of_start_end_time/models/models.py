from odoo import fields, models, api, exceptions
import re
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    
    task_id = fields.Many2one('project.task', 'Task', index=True, domain="[('company_id', '=', company_id)]")
    project_id = fields.Many2one('project.project', 'Project', domain=[('allow_timesheets', '=', True)])
    employee_id = fields.Many2one('hr.employee', "Employee")
    
    def _compute_encoding_uom_id(self):
        for analytic_line in self:
            analytic_line.encoding_uom_id = self.env.company.timesheet_encode_uom_id
            
    encoding_uom_id = fields.Many2one('uom.uom', compute='_compute_encoding_uom_id')
    _start_date = fields.Datetime(string='Fecha inicio', index=True, copy=False)
    _end_date = fields.Datetime(string='Fecha fin', index=True, copy=False)
    
    @api.depends('_end_date')        
    def compute_field(self):    
        for rec in self:
            if rec._end_date > rec._start_date:
                diferencia = rec._end_date - rec._start_date
                diff = str(diferencia)
                dias = diferencia.days
                if dias != 0:
                    diff = diff.split(',')
                    diff = diff[1].strip()
                diff = diff.split(':')                
                horas_dias = dias * 24
                horas = int(diff[0]) + horas_dias
                minutos = float(diff[1]) / 60
                segundos = float(diff[2]) /3600
                tiempo = horas + minutos + segundos
                rec.unit_amount = tiempo
            else: 
                raise ValidationError('Fecha fin debe ser mayor a fecha inicio, incluyendo las horas')
        
    unit_amount = fields.Float(compute=compute_field, store=True, compute_sudo=True)
    
    
class Project(models.Model):
    _inherit = "project.project"

    allow_timesheets = fields.Boolean("Timesheets", default=True, help="Enable timesheeting on the project.")
    
class ProjectTask(models.Model):
    _inherit = "project.task"
    
    analytic_account_active = fields.Boolean("Analytic Account", related='project_id.analytic_account_id.active', readonly=True)
    allow_timesheets = fields.Boolean("Allow timesheets", related='project_id.allow_timesheets', help="Timesheets can be logged on this task.", readonly=True)
    remaining_hours = fields.Float("Remaining Hours", compute='_compute_remaining_hours', store=True, readonly=True, help="Total remaining time, can be re-estimated periodically by the assignee of the task.")
    effective_hours = fields.Float("Hours Spent", compute='_compute_effective_hours', compute_sudo=True, store=True, help="Computed using the sum of the task work done.")
    total_hours_spent = fields.Float("Total Hours", compute='_compute_total_hours_spent', store=True, help="Computed as: Time Spent + Sub-tasks Hours.")
    progress = fields.Float("Progress", compute='_compute_progress_hours', store=True, group_operator="avg", help="Display progress of current task.")
    subtask_effective_hours = fields.Float("Sub-tasks Hours Spent", compute='_compute_subtask_effective_hours', store=True, help="Sum of actually spent hours on the subtask(s)")
    timesheet_ids = fields.One2many('account.analytic.line', 'task_id', 'Timesheets')
