# © 2016 Apulia Software S.r.l. (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product Code from Category',
    'version': '11.0.1.0.0',
    'category': 'product',
    'author': 'Apulia Software S.r.l. <info@apuliasoftware.it>',
    'website': 'www.apuliasoftware.it',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'account',
    ],
    'data': [
        'views/product_view.xml',
        'views/category_view.xml',
        'wizard/update_code.xml',
    ],
    'installable': True,
}
