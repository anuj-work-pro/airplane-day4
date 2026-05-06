# Copyright (c) 2026, anuj and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"flights/{self.name}"
