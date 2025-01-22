from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "The defining properties of an estate"


    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available Starting")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Number of Bedrooms")
    living_area = fields.Integer(string="Size of Living Area")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Garage Available")
    garden = fields.Boolean(string="Garden Available")
    garden_area = fields.Integer(string="Garden size")
    garden_orientation= fields.Selection(string='Garden Orientation',
                                         selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')],)