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
    # cdfi_invoice is used for a specific scenario. If you don't use the module
    # just leave the lines commented
    'depends': ['base', 'contacts', 'account_invoicing', 'l10n_mx'
    # 'cdfi_invoice'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/account_payment_view.xml',
        'data/res_partner_data.xml',
        # 'views/cdfi_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}