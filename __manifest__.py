{
    'name': 'Wallet Balance',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Display wallet balances',
    'description': """
        This module allows:
        - Users to view their wallet balance
        - Administrators to view all users' wallets
    """,
    'depends': ['base', 'loyalty'],
    'data': [
        'views/wallet_balance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
} 