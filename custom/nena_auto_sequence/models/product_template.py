from odoo import models, fields, _, api
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_codified = fields.Boolean('is codified?')

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(ProductTemplate, self).create(vals)
    #     if res.default_code:
    #         res.default_code = ''
    #     return res
 
    def write(self, vals):
        if vals.get('state', False) and vals.get('state') == 'published':
            if not self.is_codified:
                vals['default_code'] = self.env['ir.sequence'].next_by_code('soindi.codcli') or ('new')
                vals['is_codified'] = True
        res = super(ProductTemplate, self).write(vals)
        return res