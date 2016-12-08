# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "ERP Events",
    "version": "0.2",
    "sequence": 100,
    "category": "Tools",
    "author": "Smile (Modified by AXOOM)",
    "license": 'AGPL-3',
    "website": 'http://www.smile.fr',
    "description":
"""
ERP Events
==========
    This module lets administrator track every user operation on all the objects of the system
    (for the moment, only create, write and unlink methods).

    WARNING: This module is not compatible with audit, so uninstall it before installing this one.

    Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr

Modifications by AXOOM
----------------------
    - Need to duplicate and rename the smile_audit module to install them parallel for different use cases
    - Allow to unlink logs
    - Added some default data

Suggestions & Feedback about this modifications to: info@axoom.com

""",
    "depends": [
        'base',
        'product',
        'mrp',
        'account'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/rule_view.xml',
        'views/log_view.xml',
        'data/rules_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
