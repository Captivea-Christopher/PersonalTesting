# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request

class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		current_user = http.request.session.uid
		big_context = http.request.context
		long_user = "I KINDA WORK"
		test_esc = 42
		return http.request.render('chris_controller_testing.test_webpage', {
			'current_user' : current_user,
			'big_context' : big_context,
			'long_user' : long_user ,
			'test_esc' : test_esc
			})