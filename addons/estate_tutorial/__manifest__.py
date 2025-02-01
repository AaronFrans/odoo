{
    'name': "Estate Tutorial",
    'version': '1.0',
    'depends': ['base'],
    'author': "Aaron Frans",
    'category': 'Category',
    'description': """
    The module made in the Odoo tutorial, see: https://www.odoo.com/documentation/16.0/developer/tutorials/getting_started/03_newapp.html
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml'],
    'license': 'LGPL-3',
    'application': True
}