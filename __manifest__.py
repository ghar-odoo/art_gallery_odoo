# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ART GALLERY',
    'version': '1.0',
    'summary': 'Art Gallery Module',
    'description': "",
    'author': "Ghanshyam Rathore",
    'depends' : ['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/art_gallery_views.xml',
        'views/art_gallery_category_views.xml',
        'views/art_menus.xml'
        
    ],
     'installable': True,
    'application': True,
    'license': 'LGPL-3'
}