
from agent_eval_gym.environment.models import (
    Vendor,
    PurchaseOrder,
    Invoice,
    Payment,
)


class EnvironmentState:
    def __init__(self):
        self.vendors = {
            "V001": Vendor(
                vendor_id="V001",
                name="ABC Technologies",
                active=True,
            )
        }

        self.purchase_orders = {
            "PO001": PurchaseOrder(
                po_id="PO001",
                vendor_id="V001",
                approved_amount=5000,
                approved=True,
            )
        }

        self.invoices = {
            "INV001": Invoice(
                invoice_id="INV001",
                vendor_id="V001",
                po_id="PO001",
                amount=5000,
            )
        }

        self.payments = {}

        self.decisions = []
