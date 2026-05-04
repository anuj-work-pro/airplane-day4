import frappe


def get_context(context):
	flight_name = frappe.form_dict.get("name") or frappe.request.path.split("/")[-1]

	context.flight = frappe.get_doc("Flight", flight_name)
