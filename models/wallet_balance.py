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
                
                # Call super to update the record
                result = super(LoyaltyCard, self).write(vals)
                
                # Send notification about balance change
                if old_points != new_points:
                    message = _(
                        'Your wallet balance has been updated from %(old)s to %(new)s points',
                        old=old_points,
                        new=new_points
                    )
                    record.message_post(
                        body=message,
                        message_type='notification',
                        subtype_id=self.env.ref('mail.mt_note').id,
                        partner_ids=[record.partner_id.id]
                    )
                return result
        return super(LoyaltyCard, self).write(vals) 