from odoo import models, fields


class SaleModel(models.Model):
    _inherit = 'sale.order'
    test_field = fields.Char('Test field example', required=True)
