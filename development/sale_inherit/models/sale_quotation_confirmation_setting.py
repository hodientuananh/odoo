from odoo import models, fields, api


class SaleQuotationConfirmation(models.TransientModel):
    _inherit = 'res.config.settings'
    quotation_approval_amount = fields.Integer("Amount Approval", default_model="res.config.settings")

    @api.model
    def get_values(self):
        res = super(SaleQuotationConfirmation, self).get_values()
        param = self.env['ir.config_parameter'].sudo()
        res.update(
            quotation_approval_amount = int(param.get_param('sale_inherit.quotation_approval_amount', default=0))
        )
        return res

    def set_values(self):
        super(SaleQuotationConfirmation, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('sale_inherit.quotation_approval_amount', self.quotation_approval_amount)
