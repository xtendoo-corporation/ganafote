# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    so_factory_mail_template_id = fields.Many2one(
        comodel_name='mail.template',
        string='Factory Email Template',
        domain="[('model', '=', 'sale.order')]",
        config_parameter='sale.factory_mail_template',
        help="Email sent to factory when the order is validated."
    )
    so_factory_mail_default = fields.Char(
        string="Factory Default Mail",
        config_parameter='sale.factory_mail_default',
        help="Email sent to factory when the order is validated."
    )
