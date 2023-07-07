{
    'name': 'Kosmos Sign & Remark DO',
    'version': '1.0',
    'summary': 'Custom module for DO Report PT Kosmos Wavelength Technology',
    'description': 'Add Sign table that has 4 column, add No. and Remark column to existing table.',
    'category': 'Productivity',
    'author': 'https://github.com/Zizz4',
    'website': 'erp.kosmoswave.com',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'report/no_and_remark_done.xml',
        'report/no_and_remark_undone.xml',
        'report/sign.xml',
        'views/remark.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
