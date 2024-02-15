from odoo import models, fields

class ArtGallery(models.Model):
    _name = "art.gallery"
    _description = "Art Gallery"

    name = fields.Char(string='Artwork Name', required=True)
    description = fields.Text(string='Artwork Description')
    price = fields.Float(string='Artwork Price', required=True)
    artist = fields.Many2one('res.partner', string='Artist', required=True)
    creation_date = fields.Date(string='Creation Date')
    artist = fields.Many2one('res.partner', string='Artist', required=True)
    availability = fields.Selection(
        string='Availability',
        selection=[
            ('available', 'Available'),
            ('sold', 'Sold'),
            ('on_hold', 'On Hold')
        ],
        default='available'
    )
    active = fields.Boolean(string='Active', default=True)
    category = fields.Many2one('art.gallery.category', string='Category')
   

