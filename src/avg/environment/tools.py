
from avg.environment.state import EnvironmentState


class EnvironmentTools:
    def __init__(self, state: EnvironmentState):
        self.state = state

    def get_invoice(self, invoice_id: str):
        return self.state.invoices.get(invoice_id)

    def get_purchase_order(self, po_id: str):
        return self.state.purchase_orders.get(po_id)

    def get_vendor(self, vendor_id: str):
        return self.state.vendors.get(vendor_id)

    def get_payment_history(self, invoice_id: str):
        return [
            payment
            for payment in self.state.payments.values()
            if payment.invoice_id == invoice_id
        ]
