from odoo import models, fields

class ArtGalleryCategory(models.Model):
    _name = "art.gallery.category"
    _description = "Art Gallery Category"

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Category Description')
    active = fields.Boolean(string='Active', default=True)
