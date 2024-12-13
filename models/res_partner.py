from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string="Date of Birth")
    place_of_birth = fields.Char(string="Place of Birth")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender"
    )
