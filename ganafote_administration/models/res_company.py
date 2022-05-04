# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# from odoo import fields, models
#
#
# class ResCompany(models.Model):
#     _inherit = "res.company"
#
#     sale_order_factory_template_id = fields.Many2one(
#         comodel_name='mail.template',
#         string='Factory Email Template',
#         domain="[('model', '=', 'sale.order')]",
#         check_company=True,
#     )
#     sale_order_factory_email = fields.Char(
#         string="Factory Sale Email",
#     )
