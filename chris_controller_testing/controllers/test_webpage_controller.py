# -*- coding: utf-8 -*-
from odoo import http


class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		context = self._context
		current_uid = context.get('uid')
		current_user = self.env['res.users'].browse(current_uid)
		return http.request.render('chris_controller_testing.test_webpage', {'customer_name' : current_user})