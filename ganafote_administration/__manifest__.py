# Copyright 2021 ForgeFlow (http://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Ganafote Administration",
    "author": "DDL-Xtendoo",
    "company": "Xtendoo",
    "summary": "Ganafote Administration",
    "version": "16.0.1.0.0",
    "category": "Extra-tools",
    "website": "https://github.com/OCA/edi",
    "depends": [
        "base",
        "sale_margin",
        "sale",
    ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        # "views/crm_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
