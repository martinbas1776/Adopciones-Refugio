# -*- coding: utf-8 -*-
# from odoo import http


# class AdopcionesRefugio(http.Controller):
#     @http.route('/adopciones_refugio/adopciones_refugio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adopciones_refugio/adopciones_refugio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('adopciones_refugio.listing', {
#             'root': '/adopciones_refugio/adopciones_refugio',
#             'objects': http.request.env['adopciones_refugio.adopciones_refugio'].search([]),
#         })

#     @http.route('/adopciones_refugio/adopciones_refugio/objects/<model("adopciones_refugio.adopciones_refugio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adopciones_refugio.object', {
#             'object': obj
#         })

