
from avg.scenarios.invoice_scenarios import create_invoice_scenario


class EnvironmentState:
    def __init__(self, scenario_id="S1"):
        scenario = create_invoice_scenario(scenario_id)

        invoice = scenario["invoice"]
        vendor = scenario["vendor"]
        purchase_order = scenario["purchase_order"]
        payments = scenario["payments"]

        self.invoices = {
            invoice.invoice_id: invoice
        }

        self.vendors = {
            vendor.vendor_id: vendor
        }

        self.purchase_orders = (
            {purchase_order.po_id: purchase_order}
            if purchase_order is not None
            else {}
        )

        self.payments = {
            payment.payment_id: payment
            for payment in payments
        }

        self.decisions = []
