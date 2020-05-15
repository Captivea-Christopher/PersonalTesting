# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request

class test_webpage(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		list_of_projects_owned_by_customer = ["Office Design", "Research & Development", "Test Project"]
		user_email = "placeholder_email"
		return http.request.render('chris_controller_testing.test_webpage', {
			'list_of_projects_owned_by_customer': list_of_projects_owned_by_customer,
			'user_email' : user_email
			})