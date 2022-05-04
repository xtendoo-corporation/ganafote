# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # company_so_factory_template_id = fields.Many2one(
    #     related="company_id.sale_order_factory_template_id",
    #     string="Factory Default Template",
    #     readonly=False,
    #     domain="[('model', '=', 'sale.order')]",
    # )
    so_factory_mail_template_id = fields.Many2one(
        comodel_name='mail.template',
        string='Factory Email Template',
        domain="[('model', '=', 'sale.order')]",
        config_parameter='sale.factory_mail_template',
        help="Email sent to factory when the order is validated."
    )
    # company_so_factory_email = fields.Char(
    #     related="company_id.sale_order_factory_email",
    #     string="Factory Default Mail",
    #     readonly=False,
    # )
    so_factory_mail_default = fields.Char(
        string="Factory Default Mail",
        config_parameter='sale.factory_mail_default',
        help="Email sent to factory when the order is validated."
    )
