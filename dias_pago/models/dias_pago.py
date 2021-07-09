#from odoo import api, fields, models, tools, _
#from odoo.modules import get_module_resource
#from odoo.release import version_info
#import logging

#class payment_frecuent(models.Model):
 #   _inherit = "website_sale.payment"
    
 #   tipo_pago = fields.Selection([('quincedias','15 dias'),('treintadias', '30 dias'), ('cuarentadias', '40 dias')],
#        string="Tipo de Pago")

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class productdiaspago(models.Model):
    _inherit = 'product.template'

    
    tipo_pago = fields.Selection([('quincedias','15 dias'),('treintadias', '30 dias'), ('cuarentadias', '40 dias')],
        string="Tipo de Pago")
