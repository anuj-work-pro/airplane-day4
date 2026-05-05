# Copyright (c) 2026, anuj and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_update(self):
		# Trigger background job when gate changes
		enqueue(update_ticket_gate, flight=self.name, gate=self.gate_number)

	def before_save(self):
		if not self.route:
			self.route = f"flights/{self.name}"


def update_ticket_gate(flight, gate):
	tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight}, pluck="name")

	for t in tickets:
		doc = frappe.get_doc("Airplane Ticket", t)
		doc.gate_no = gate
		doc.save(ignore_permissions=True)
