# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OksInvoice(models.Model):
    _inherit = "account.invoice"
    
    # By default the commercial name is always displayed for companies, this is
    # fine in other modules but accountants need the legal name. There is a bug 
    # with adding context to name_get() on res.partner so this is a workaround
    # a new field with the legal name is added and this field will be used
    # to show the legal name in accounting module
    x_partner_legal_name = fields.Char(string="Razón social", compute='_compute_legal_name', readonly=True)

    @api.depends("partner_id")
    def _compute_legal_name(self):
        for invoice in self:
            invoice.x_partner_legal_name = invoice.partner_id.name