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

    # Overriden method.
    @api.multi
    def name_get(self):
        res = []
        for partner in self:
             # Only change. Originally it was: name = partner.name or ''
            if self._context.get('legal_name'):
                name = partner.name or ''
            else:
                name = partner.display_name or ''
            # Only change 

            if partner.company_name or partner.parent_id:
                if not name and partner.type in ['invoice', 'delivery', 'other']:
                    name = dict(self.fields_get(['type'])['type']['selection'])[partner.type]
                if not partner.is_company:
                    name = "%s, %s" % (partner.commercial_company_name or partner.parent_id.name, name)
            if self._context.get('show_address_only'):
                name = partner._display_address(without_company=True)
            if self._context.get('show_address'):
                name = name + "\n" + partner._display_address(without_company=True)
            name = name.replace('\n\n', '\n')
            name = name.replace('\n\n', '\n')
            if self._context.get('show_email') and partner.email:
                name = "%s <%s>" % (name, partner.email)
            if self._context.get('html_format'):
                name = name.replace('\n', '<br/>')
            res.append((partner.id, name))
        return res
