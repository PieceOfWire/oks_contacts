# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OksContact(models.Model):
    _inherit = "res.partner"

    #Extra field. Commercial name.
    x_commercial_name = fields.Text(string="Nombre comercial", default=_compute_commercial_name)

    @api.depends("is_company")
    def _remove_commercial_name(self):
        if self.is_company == False:
            self.x_commercial_name = ""

    @api.one
    def _compute_commercial_name(self):
        if self.is_company == True:
            if self.name != "" and self.name != None:
                self.x_commercial_name = self.name
        else:
            self.x_commercial_name = ""            