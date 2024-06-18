# __manifest__.py
{
    'name': 'Task Products',
    'version': '1.0',
    'summary': 'Module to manage task products',
    'description': """
        This module adds a new field 'online_tag' to the product model and a new menu item 'Task Products'
    """,
    'author': 'Marek Mikulec',
    'website': 'https://github.com/MMikulec',
    'category': 'Inventory',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_products_views.xml',
        'views/task_products_menu.xml',
    ],
    'installable': True,
    'application': True,
}
