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
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}