# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Inheritance Module',
    'category': 'Website/Website',
    'summary': 'Sale inheritance',
    'version': '1.0',
    'description': """
This module adds a Twitter scroller building block to the website builder, so that you can display Twitter feeds on any page of your website.
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_inherit_views.xml',
        'views/sale_quotation_confirmation_views.xml',
        'report/sale_inherit_templates.xml'
    ],
    'installable': True,
}
