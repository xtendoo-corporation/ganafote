# Copyright 2021 Xtendoo (https://xtendoo.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        result = super().action_confirm()
        self._template_send_mail()
        return result

    def _template_send_mail(self):
        template_id = self.env['mail.template'].search(
            [('id', '=', int(self.env['ir.config_parameter'].sudo().get_param('sale.factory_mail_template')))]
        )
        if not template_id:
            return

        factory_mail = self.env['ir.config_parameter'].sudo().get_param('sale.factory_mail_default')
        if not factory_mail:
            return

        email_values = {
            'email_from': self.env.user.email_formatted,
            'author_id': self.env.user.partner_id.id,
            'email_to': factory_mail,
            'email_cc': False,
            'auto_delete': True,
            'recipient_ids': [],
            'partner_ids': [],
            'scheduled_date': False,
        }

        for order in self:
            template_id.send_mail(
                order.id, force_send=False, raise_exception=True, email_values=email_values, notif_layout=False
            )
        return
