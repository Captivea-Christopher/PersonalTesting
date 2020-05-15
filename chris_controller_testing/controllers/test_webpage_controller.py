# -*- coding: utf-8 -*-
from odoo import http


class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		current_user = request.session.uid
		return http.request.render('chris_controller_testing.test_webpage', {'customer_name' : current_user})