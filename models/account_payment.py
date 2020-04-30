# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OksPayment(models.Model):
    _inherit = "account.payment"
    
    x_partner_legal_name = fields.Char(string="Razón social", readonly=True, related="partner_id.name")