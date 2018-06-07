# -*- coding: utf-8 -*-
from odoo import http

# class Nicoapp(http.Controller):
#     @http.route('/nicoapp/nicoapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nicoapp/nicoapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nicoapp.listing', {
#             'root': '/nicoapp/nicoapp',
#             'objects': http.request.env['nicoapp.nicoapp'].search([]),
#         })

#     @http.route('/nicoapp/nicoapp/objects/<model("nicoapp.nicoapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nicoapp.object', {
#             'object': obj
#         })