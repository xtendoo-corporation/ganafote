# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    is_delivered = fields.Boolean(
        string="Entregado",
        default=False
    )

    @api.onchange('is_delivered')
    def _send_delivered_mail(self):
        template = self.env['ir.config_parameter'].sudo().get_param(
            'sale.default_send_invoice_email_template')
        template_id = self.env['mail.template'].search(
            [("id", "=", template)]
        )
        if not template_id:
            return

        for invoice in self:
            invoice_id = self.env['account.move'].search(
            [("name", "=", invoice.name)]
            )
            if invoice.is_delivered:
                email_values = {
                    'email_from': self.env.user.email_formatted,
                    'author_id': self.env.user.partner_id.id,
                    'email_to': invoice.partner_id.email,
                    'email_cc': False,
                    'auto_delete': True,
                    'recipient_ids': [],
                    'partner_ids': [],
                    'scheduled_date': False,
                }


                template_id.send_mail(invoice_id.id, force_send=False, raise_exception=False, email_values=None,
                                      notif_layout=False)

