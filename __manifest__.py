{
    'name': 'Wallet Balance',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Display wallet balances with notifications',
    'description': """
        This module allows:
        - Users to view their wallet balance
        - Receive notifications on balance updates
    """,
    'depends': ['base', 'loyalty', 'mail'],
    'data': [
        'views/wallet_balance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
} 