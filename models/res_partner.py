from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string="Tanggal Lahir")
    place_of_birth = fields.Char(string="Tempat Lahir")
    gender = fields.Selection(
        [('male', 'Laki-laki'), ('female', 'Perempuan')],
        string="Gender"
    )
    school = fields.Char(string="Asal Sekolah")
    pengalaman = fields.Char(string="Pengalaman Belajar Jepang (Opsional)")
