# Copyright 2021 Xtendoo (https://xtendoo.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    situation = fields.Selection([
        ('processed', 'Processed'),
        ('in_sample', 'In sample'),
        ('production', 'Production'),
    ],tracking=3, default='processed')
