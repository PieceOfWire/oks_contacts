# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OksContact(models.Model):
    _inherit = "res.partner"
     
    # Extra field. Commercial name. Has no impact on workflow. Just used as an identifier
    x_commercial_name = fields.Char(string="Nombre comercial")

    # Overriden method. 
    @api.depends("is_company", "name", 'x_commercial_name')
    def _compute_display_name(self):
        for partner in self:
            if partner.is_company == True:
                if partner.x_commercial_name == "" or partner.x_commercial_name == False:
                    partner.display_name = partner.name
                else:
                    partner.display_name = partner.x_commercial_name
            else:
                partner.display_name = partner.name
