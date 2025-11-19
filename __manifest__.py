# -*- coding: utf-8 -*-
{
    'name': 'Custom Warehouse Barcode',
    'version': '19.0.1.0.0',
    'depends': ['stock_barcode'],
    'data': [
        'views/custom_barcode_menu.xml',
        'data/window_actions.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'custom_inventory_barcode/static/src/main_menu/main_menu_patch.xml'
        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
