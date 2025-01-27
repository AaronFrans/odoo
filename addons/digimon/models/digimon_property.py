from odoo import models, fields


class DigimonProperty(models.Model):
    _name = "digimon.property"
    _description = "The defining properties of a digimon"
    
    
    name = fields.Char(string="Name", required=True)
    image =  fields.Char(string="Image URL", required=True)
    level =  fields.Char(string="Level", required=True)