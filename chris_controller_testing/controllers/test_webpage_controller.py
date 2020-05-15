# -*- coding: utf-8 -*-
from odoo import http


class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	customer_name = 
	def index(self, **kw):
		return http.request.render('chris_controller_testing.test_webpage', {'customer_name' : "helaeld"})