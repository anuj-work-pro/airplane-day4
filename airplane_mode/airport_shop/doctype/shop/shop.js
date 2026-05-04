frappe.ui.form.on("Shop", {
	onload: function (frm) {
		frm.set_query("shop_type", function () {
			return {
				filters: {
					enabled: 1,
				},
			};
		});
	},
});
