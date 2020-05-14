# -*- coding: utf-8 -*-
from odoo import http

class test_webpage(http.Controller):
	@http.route('/test/webpage',auth='user', website=True)
	def index(self, **kw):
		return http.request.render('test_webpage', {'name' :'slartybartfast'})