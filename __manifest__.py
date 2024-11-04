{
    'name': 'Wallet Balance',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Manage user wallet balances',
    'description': """
        This module allows:
        - Users to view their wallet balance
        - Administrators to view and manage all users' wallets
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security/wallet_balance_security.xml',
        'security/ir.model.access.csv',
        'data/wallet_balance_data.xml',
        'views/wallet_balance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
} 