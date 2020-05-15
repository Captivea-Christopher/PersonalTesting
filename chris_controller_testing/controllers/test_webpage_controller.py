# -*- coding: utf-8 -*-
from odoo import http


class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	#current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
	def index(self, **kw):
		return http.request.render('chris_controller_testing.test_webpage', {'customer_name' : current_user})