# Copyright 2021 Xtendoo (https://xtendoo.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        result = super().action_confirm()
        for order in self:
            print("*"*80)
            print("action_confirm:", order)
            print("*"*80)
        return result

    def _action_confirm(self):
        result = super()._action_confirm()

        print("*" * 80)
        print("_action_confirm:")
        print("*" * 80)

        email_values = {
            'email_from': self.env.user.email_formatted,
            'author_id': self.env.user.partner_id.id,
            'email_to': 'manuelcalerosolis@gmail.com',
            'email_cc': False,
            'auto_delete': True,
            'recipient_ids': [],
            'partner_ids': [],
            'scheduled_date': False,
        }

        for order in self:

            print("*"*80)
            print("order:", order)
            print("order.sale_order_template_id:", order.sale_order_template_id)
            print("*"*80)

            if order.sale_order_template_id and order.sale_order_template_id.mail_template_id:

                print("*" * 80)
                print("email_values:", email_values)
                print("*" * 80)

                order.sale_order_template_id.mail_template_id.send_mail(
                    order.id, force_send=False, raise_exception=False, email_values=None, notif_layout=False
                )

        return result
