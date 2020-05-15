# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class test_webpage(http.Controller):
	
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		current_user = http.request.session.uid
		big_context = http.request.context
		return http.request.render('chris_controller_testing.test_webpage', {'current_user' : current_user, 'big_context' : big_context})