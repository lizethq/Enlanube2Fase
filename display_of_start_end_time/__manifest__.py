{
    'name': 'Display of strat and end time',

    'version': '13.0',

    'author': "Luis Felipe Navas Pineda",

    'contributors': ['Luis Felipe Navas Pineda ln@todoo.co'],

    'website': "",

    'category': 'reports',

    'depends': [
        'base',
        'project',
        'account',       
        'account.analytic.line',        
    ],

    'data': [        
        'views/project.xml',
        'views/account.xml',       
    ],
    'installable': True
}
