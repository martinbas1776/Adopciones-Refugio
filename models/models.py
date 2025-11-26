# -*- coding: utf-8 -*-
from odoo import models, fields

class adoptante(models.Model):
    _name = 'adopciones_refugio.adoptante'
    _description = ''
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre de el adoptante", required=True)
    apellidos = fields.Char(string="Apellidos de el adoptante", required=True)
    animal_ids = fields.One2many('adopciones_refugio.adopcion', 'adoptante_id', string='Animales adoptados')

class adopcion(models.Model):
    _name = 'adopciones_refugio.adopcion'
    _description = ''

    animal_id = fields.Many2one('refugio_animales.animal', string='Animal', required=True)
    adoptante_id = fields.Many2one('adopciones_refugio.adoptante', string='Adoptante', required=True)
    fecha = fields.Date(string="Fecha de la adopcion", default=fields.Date.today)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('facturado', 'Facturado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='pendiente')