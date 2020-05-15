# -*- coding: utf-8 -*-
from odoo import http


class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		current_user = http.request.session.uid
		return http.request.render('chris_controller_testing.test_webpage', {'current_user' : current_user})