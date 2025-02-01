from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The type of a property"


    name = fields.Char(string="Name", required=True)