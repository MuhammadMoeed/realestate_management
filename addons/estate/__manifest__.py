{
    'name': "Realestate Management",
    'version': '14.1.0',
    'depends': ['base'],
    'sequence': '1',
    'author': "Muhammad Moeed",
    'category': 'Category',
    'description': """This is a  module of Real-Estate Management as an assignment work!""",
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/user_inherited.xml',
        'data/estate_property_data.xml',

    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
