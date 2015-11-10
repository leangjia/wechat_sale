from openerp import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_button_confirm(self):
        super(SaleOrder, self).action_button_confirm()
        for order in self:
            order.partner_id.send_sale_order_data(order)

