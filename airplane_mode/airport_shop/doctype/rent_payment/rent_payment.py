# Copyright (c) 2026, anuj and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class RentPayment(Document):
	def before_insert(self):
		shop = frappe.get_doc("Shop", self.shop)
		self.tenant = shop.tenant_name
		self.amount = shop.rent_amount
