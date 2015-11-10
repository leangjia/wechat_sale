from openerp import models, fields, api, _


class Partner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def send_sale_order_data(self, order):
        self.ensure_one()
        data = dict()
        data["no"] = {"value": order.name, "color": "#173177"}
        data["client"] = {"value": order.partner_id.name, "color": "#173177"}
        data["total"] = {"value": "%.2f" % order.amount_total, "color": "#173177"}
        self.send_template_message("h7VXsZOEa03dxL-xBcc6rdnEeAzmZrkj3tzv1ExqQoE", data,
                                   url="http://odoo.wangting.name")
