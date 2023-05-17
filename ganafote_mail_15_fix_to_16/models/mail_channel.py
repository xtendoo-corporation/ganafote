from odoo import _, models, fields


class Channel(models.Model):
    _inherit = "mail.channel"

    public = fields.Selection([
        ('public', 'Everyone'),
        ('private', 'Invited people only'),
        ('groups', 'Selected group of users')], string='Privacy',
        required=True, default='groups',
        help='This group is visible by non members. Invisible groups can add members through the invite button.')
