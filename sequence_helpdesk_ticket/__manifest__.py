{
    'name': 'Reports account thomas',

    'version': '13.1',

    'author': "Todoo SAS",

    'contributors': ['Luis Felipe Navas ln@todoo.co'],

    'website': "www.todoo.co",

    'category': 'Reports',

    'depends': [

        'account_accountant',
        'account',

    ],

    'data': [       
        'reports/report_advances.xml',                   
        'reports/report_cash.xml',                   
        'reports/report_credit_note.xml',                   
        'reports/report_discharge.xml',                   
        'reports/report_accounting_entries.xml',
        'reports/report_purchase_invoice.xml',
    ],
    'installable': True
}