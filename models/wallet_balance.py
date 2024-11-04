from odoo import models, fields, api, _
from odoo.exceptions import UserError

class WalletBalance(models.Model):
    _name = 'wallet.balance'
    _description = 'Wallet Balance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('wallet.balance') or _('New')
        return super().create(vals)