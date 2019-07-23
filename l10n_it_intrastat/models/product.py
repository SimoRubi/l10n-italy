from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    intrastat_code_id = fields.Many2one(
        'report.intrastat.code',
        string='Intrastat Code'
    )
    intrastat_type = fields.Selection(
        [
            ('good', 'Good'),
            ('service', 'Service'),
            ('misc', 'Miscellaneous'),
            ('exclude', 'Exclude')
        ],
        string='Intrastat Type')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    intrastat_code_id = fields.Many2one(
        comodel_name='report.intrastat.code',
        string='Intrastat Code')
    intrastat_type = fields.Selection(
        selection=[
            ('good', 'Good'),
            ('service', 'Service'),
            ('misc', 'Miscellaneous'),
            ('exclude', 'Exclude')],
        string='Intrastat Type')

    def get_intrastat_data(self):
        """
        The intrastat code with the following priority:

        - Intrastat Code on product template
        - Intrastat Code on product category
        """
        res = {
            'intrastat_code_id': False,
            'intrastat_type': False
        }
        # From Product
        if self.intrastat_type:
            res['intrastat_code_id'] = self.intrastat_code_id.id
            res['intrastat_type'] = self.intrastat_type
        elif self.categ_id and self.categ_id.intrastat_code_id:
            res['intrastat_code_id'] = self.categ_id.intrastat_code_id.id
            res['intrastat_type'] = self.categ_id.intrastat_type
        return res
