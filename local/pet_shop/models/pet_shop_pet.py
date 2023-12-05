from odoo import models, fields


class PetShopPet(models.Model):
    _name = 'pet_shop.pet'
    _description = 'Pet'

    name = fields.Char(string='Name', size=10)
    
    bio = fields.Text(string='Bio', help="Pet bio with his history")

    sex = fields.Selection(string='Sex', selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ])

    birth_certificate = fields.Binary('Birth Certificate', attachment=True)

    photo = fields.Image(string='Photo')

    adopted = fields.Boolean(string='Adopted', help="True when pet is adopted", default=False)

    birthdate = fields.Date(string='Birthdate')

    age = fields.Integer(string='Age')

    weight = fields.Float(string='Weight', digits=(5, 2))
