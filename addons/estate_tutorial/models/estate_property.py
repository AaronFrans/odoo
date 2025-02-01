from odoo import models, fields, api
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
    living_area = fields.Integer(string="Size of Living Area (sqm)")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Garage Available")
    garden = fields.Boolean(string="Garden Available")
    garden_area = fields.Integer(string="Garden size (sqm)")
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('north', 'North'),
                                                     ('east', 'East'),
                                                     ('south', 'South'),
                                                     ('west', 'West')
                                                     ],)
    
    
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string='Status',
                             selection=[('new', ' New'),
                                        ('offer_received', 'Offer Received'),
                                        ('offer_accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'),
                                        ('canceled', 'Canceled')
                                        ],
                             default = 'new',
                             required = True,
                             copy = False,)
    
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    
    total_area = fields.Float(string="Total Are (sqm)", compute="_compute_total_area")
    
    
    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    
    