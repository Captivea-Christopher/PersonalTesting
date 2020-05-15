# -*- coding: utf-8 -*-
{
    'name': "chris_controller_testing",

    'summary': """
        Testing Platform for Website""",

    'description': """
        Where i will mess around with website features and development
    """,

    'author': "Christopher_Beirne",
    'website': "https://captivea-christopher-personaltesting-task-submission-1094177.dev.odoo.com/web?debug=true#id=544&action=32&model=ir.module.module&view_type=form&menu_id=5",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ]
}