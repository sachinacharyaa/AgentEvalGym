
from avg.environment.models import (
    Invoice,
    PurchaseOrder,
    Vendor,
    Payment,
)


def create_invoice_scenario(scenario_id: str):
    """
    Create a reproducible invoice reconciliation scenario.

    Returns the business records for a scenario.
    """

    if scenario_id == "S1":
        # Valid invoice: should be approved.
        return {
            "invoice": Invoice(
                invoice_id="INV001",
                vendor_id="V001",
                po_id="PO001",
                amount=5000,
            ),
            "purchase_order": PurchaseOrder(
                po_id="PO001",
                vendor_id="V001",
                approved_amount=5000,
                approved=True,
            ),
            "vendor": Vendor(
                vendor_id="V001",
                name="ABC Technologies",
                active=True,
            ),
            "payments": [],
        }

    elif scenario_id == "S2":
        # Invoice amount exceeds approved PO amount.
        return {
            "invoice": Invoice(
                invoice_id="INV002",
                vendor_id="V002",
                po_id="PO002",
                amount=7000,
            ),
            "purchase_order": PurchaseOrder(
                po_id="PO002",
                vendor_id="V002",
                approved_amount=5000,
                approved=True,
            ),
            "vendor": Vendor(
                vendor_id="V002",
                name="Tech Solutions",
                active=True,
            ),
            "payments": [],
        }

    elif scenario_id == "S3":
        # Vendor is inactive.
        return {
            "invoice": Invoice(
                invoice_id="INV003",
                vendor_id="V003",
                po_id="PO003",
                amount=3000,
            ),
            "purchase_order": PurchaseOrder(
                po_id="PO003",
                vendor_id="V003",
                approved_amount=3000,
                approved=True,
            ),
            "vendor": Vendor(
                vendor_id="V003",
                name="Inactive Supplies",
                active=False,
            ),
            "payments": [],
        }

    elif scenario_id == "S4":
        # Invoice has already been paid.
        return {
            "invoice": Invoice(
                invoice_id="INV004",
                vendor_id="V004",
                po_id="PO004",
                amount=4000,
            ),
            "purchase_order": PurchaseOrder(
                po_id="PO004",
                vendor_id="V004",
                approved_amount=4000,
                approved=True,
            ),
            "vendor": Vendor(
                vendor_id="V004",
                name="Global Services",
                active=True,
            ),
            "payments": [
                Payment(
                    payment_id="PAY004",
                    invoice_id="INV004",
                    amount=4000,
                    completed=True,
                )
            ],
        }

    elif scenario_id == "S5":
        # Purchase order is missing.
        return {
            "invoice": Invoice(
                invoice_id="INV005",
                vendor_id="V005",
                po_id="PO005",
                amount=2500,
            ),
            "purchase_order": None,
            "vendor": Vendor(
                vendor_id="V005",
                name="Unknown Contractor",
                active=True,
            ),
            "payments": [],
        }

    else:
        raise ValueError(
            f"Unknown scenario: {scenario_id}"
        )
