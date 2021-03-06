# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from gerp import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    l10n_in_hsn_code = fields.Char(string="HSN/SAC Code", help="Harmonized System Nomenclature/Services Accounting Code")
