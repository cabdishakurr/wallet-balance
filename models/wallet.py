from odoo import models, fields, api, _
from odoo.exceptions import UserError

class UserWallet(models.Model):
    _name = 'user.wallet'
    _description = 'User Wallet'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Reference',
        required=True,
        readonly=True,
        default=lambda self: _('New')
    )
    user_id = fields.Many2one(
        'res.users',
        string='User',
        required=True,
        default=lambda self: self.env.user,
        tracking=True
    )
    balance = fields.Float(
        string='Balance',
        default=0.0,
        tracking=True
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    state = fields.Selection([
        ('active', 'Active'),
        ('blocked', 'Blocked')
    ], string='Status', default='active', tracking=True)
    last_transaction_date = fields.Datetime(
        string='Last Transaction',
        readonly=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('user.wallet') or _('New')
        return super().create(vals_list)

    def action_block(self):
        self.write({'state': 'blocked'})

    def action_unblock(self):
        self.write({'state': 'active'})

    @api.constrains('balance')
    def _check_balance(self):
        for wallet in self:
            if wallet.balance < 0:
                raise UserError(_('Wallet balance cannot be negative.')) 