# Copyright 2021 Xtendoo (https://xtendoo.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    situation = fields.Selection([
        ('gestion', 'Gestion'),
        ('processed', 'Processed'),
        ('in_sample', 'In sample'),
        ('production', 'Production'),
        ('transport', 'Transport'),
    ],tracking=3, default='processed')
