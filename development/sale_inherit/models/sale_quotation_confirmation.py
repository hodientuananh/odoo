from odoo import models, fields, api


class SaleModel(models.Model):
    _inherit = 'sale.order'
    is_request_to_approval = fields.Boolean(string='Confirm Quotation', readonly=True)
    is_request_to_approval_trig = fields.Boolean(string='Confirm Quotation Trigger', compute="_is_request_to_approval", readonly=True)

    def _is_request_to_approval(self):
        for order in self:
            quotation_confirmation_setting = int(
                (self.env['ir.config_parameter'].get_param('sale_inherit.quotation_approval_amount')))
            total_amount = self._amount_all()
            order.is_request_to_approval_trig = total_amount > quotation_confirmation_setting

    def action_request_to_approval(self):
        for order in self:
            quotation_confirmation_setting = int(
                (self.env['ir.config_parameter'].get_param('sale_inherit.quotation_approval_amount')))
            order.is_request_to_approval = True
        self.write({
            'state': 'sale'
        })

    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            return amount_untaxed + amount_tax
