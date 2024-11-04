from odoo import models, fields, api, _

class LoyaltyCard(models.Model):
    _inherit = ['loyalty.card']
    _name = 'loyalty.card'

    def write(self, vals):
        """Override write to send notification when points are updated"""
        if 'points' in vals:
            for record in self:
                old_points = record.points
                new_points = vals['points']
                
                result = super(LoyaltyCard, self).write(vals)
                
                if old_points != new_points:
                    # Create notification message
                    message = _(
                        'Your wallet balance has been updated from %(old)s to %(new)s points',
                        old=old_points,
                        new=new_points
                    )
                    
                    # Send notification with sound
                    self.env['bus.bus']._sendone(
                        record.partner_id.user_ids[0].partner_id, 
                        'wallet.balance.update', 
                        {
                            'type': 'wallet_update',
                            'title': _('Wallet Balance Updated'),
                            'message': message,
                            'sticky': True,
                            'warning': True,  # This will play a sound
                        }
                    )
                    
                    # Send inbox notification
                    self.env['mail.message'].create({
                        'model': self._name,
                        'res_id': record.id,
                        'message_type': 'notification',
                        'subtype_id': self.env.ref('mail.mt_comment').id,
                        'partner_ids': [(4, record.partner_id.id)],
                        'body': message,
                        'notification_ids': [(0, 0, {
                            'res_partner_id': record.partner_id.id,
                            'notification_type': 'inbox',
                            'notification_status': 'sent',
                        })]
                    })
                    
                return result
        return super(LoyaltyCard, self).write(vals) 