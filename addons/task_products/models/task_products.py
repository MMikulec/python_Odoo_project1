# models/task_products.py
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    online_tag = fields.Char(string='Online Tag')
