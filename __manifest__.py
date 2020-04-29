# -*- coding: utf-8 -*-
{
    'name': "OKS Contacts",

    'summary': """
        Adds a commercial/trade name to companies.""",

    'description': """
        Adds an extra field to be used as commercial/trade name. The original
        name becomes the legal name to be used in invoices
    """,

    'author': "Antonio Aguilar",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Contacts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # Last module is not required. If you do not use it just delete it from the dependencies
    # and do not include cdfi_view.xml in this manifest
    'depends': ['base', 'contacts', 'account_invoicing', 'cdfi_invoice'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/cdfi_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}