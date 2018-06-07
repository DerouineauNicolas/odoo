# -*- coding: utf-8 -*-

from odoo import models, fields, api

class nicoapp(models.Model):
    _name = 'nicoapp.nicoapp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100