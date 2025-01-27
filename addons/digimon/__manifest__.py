{
    'name': "Digimon",
    'version': '1.0',
    'depends': ['base'],
    'author': "Aaron Frans",
    'category': 'Testing/Digimon',
    'description': """
    Module to display a list of digimon via the api at: https://digimon-api.vercel.app/?ref=public_apis&utm_medium=website
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/digimon_views.xml',
        'views/digimon_menus.xml'],
    'license': 'LGPL-3',
    'application': True
}