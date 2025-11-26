# -*- coding: utf-8 -*-
{
    'name': "adopciones_refugio",

    'summary': "Gestión de adopciones",

    'description': """
    """,

    'author': "",
    'website': "https://www.wikipedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'refugio_animales'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/report_adoptante.xml',
        'reports/report_adopcion.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

