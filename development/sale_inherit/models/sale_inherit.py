from odoo import models, fields


class SaleModel(models.Model):
    _inherit = 'sale.order'
    quotation_type = fields.Selection([ ('Commercial', 'Commercial'),('Residential', 'Residential'),],'Type', default='Commercial')
