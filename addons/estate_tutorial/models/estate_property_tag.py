from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "The tag of a property"


    name = fields.Char(string="Name", required=True)