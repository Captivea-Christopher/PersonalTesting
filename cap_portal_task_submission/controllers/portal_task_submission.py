# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class portal_task_submission(http.Controller):
	@http.route('/test/webpage', type='http', auth='user', website=True)
	def index(self, **kw):
		partner_id = request.env.user.partner_id.id
		list_of_projects_owned_by_customer = request.env['project.project'].sudo().search([
			('partner_id', '=', partner_id)
		])
		test = list_of_projects_owned_by_customer
		customer_email = "placeholder_email"
		return http.request.render('chris_controller_testing.test_webpage', {
			'list_of_projects_owned_by_customer': list_of_projects_owned_by_customer,
			'customer_email' : customer_email,
			'test' : test
			})