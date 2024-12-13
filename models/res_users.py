from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    date_of_birth = fields.Date(related='partner_id.date_of_birth', string="Date of Birth", store=True, readonly=False)
    place_of_birth = fields.Char(related='partner_id.place_of_birth', string="Place of Birth", store=True, readonly=False)
    gender = fields.Selection(related='partner_id.gender', string="Gender", store=True, readonly=False)
