from odoo import models, fields, _, api
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    def write(self, vals):
        if vals.get('state', False) and vals.get('state') == 'published':
            if self.client_type_ids and self.client_type_ids.id != self.env.ref('lixie_pharmaceutical_contact_approval.lx_client_type_7').id and not self.ref:
                vals['ref'] = self.env['ir.sequence'].next_by_code('soindi.codcli') or ('new')
        res = super(ResPartner, self).write(vals)
        return res