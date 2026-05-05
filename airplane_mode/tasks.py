import frappe


def send_rent_reminders():
	if not frappe.db.get_single_value("Shop Settings", "enable_reminders"):
		return

	shops = frappe.get_all("Shop", filters={"status": "Occupied"}, fields=["name", "tenant"])

	for shop in shops:
		if not shop.tenant:
			continue

		tenant = frappe.get_doc("Tenant", shop.tenant)

		if tenant.email:
			frappe.sendmail(
				recipients=tenant.email,
				subject="Rent Due Reminder",
				message=f"""
                Dear {tenant.name},<br><br>
                Rent is due for your shop <b>{shop.name}</b>.<br><br>
                Please make payment.<br><br>
                Thank you.
                """,
			)
