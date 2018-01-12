# -*- coding: utf-8 -*-
# © 2016 Apulia Software S.r.l. (<info@apuliasoftware.it>)
# © 2018 Apulia Software S.r.l. (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _


class IrSequence(models.Model):

    _inherit = 'ir.sequence'

    name = fields.Char(size=256)
