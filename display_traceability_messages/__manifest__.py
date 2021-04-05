{
    'name': 'Date and time display in traceability messages',

    'version': '13.1',

    'author': "Todoo SAS",

    'contributors': ['Luis Felipe Navas ln@todoo.co'],

    'website': "www.todoo.co",

    'category': 'Reports',

    'depends': [
        'base', 
        'mail',
    ],
    
    'qweb': [       
        'static/src/xml/thread.xml',
    ],
    
    'installable': True
}