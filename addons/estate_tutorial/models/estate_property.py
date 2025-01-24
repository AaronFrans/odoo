from odoo import models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "The defining properties of an estate"


    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available Starting", default = datetime.today() + relativedelta(months=3), copy = False)
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly = True, copy = False)
    bedrooms = fields.Integer(string="Number of Bedrooms", default = 2)
    living_area = fields.Integer(string="Size of Living Area")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Garage Available")
    garden = fields.Boolean(string="Garden Available")
    garden_area = fields.Integer(string="Garden size")
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')],)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string='Status',
                             selection=[('new', ' New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
                             default = 'new',
                             required = True,
                             copy = False,)