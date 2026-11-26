
from avg.environment.state import EnvironmentState
from avg.environment.tools import EnvironmentTools
from avg.environment.models import AgentDecision


class InvoiceEnvironment:
def __init__(self, scenario_id="S1"):
        self.state = EnvironmentState(scenario_id)
        self.tools = EnvironmentTools(self.state)
        self.trajectory = []

    def observe_invoice(self, invoice_id: str):
        invoice = self.tools.get_invoice(invoice_id)

        if invoice is None:
            raise ValueError(f"Invoice {invoice_id} not found")

        observation = {
            "invoice": invoice,
            "purchase_order": self.tools.get_purchase_order(
                invoice.po_id
            ),
            "vendor": self.tools.get_vendor(
                invoice.vendor_id
            ),
            "payment_history": self.tools.get_payment_history(
                invoice_id
            ),
        }

        self.trajectory.append({
            "action": "observe_invoice",
            "invoice_id": invoice_id,
        })

        return observation

    def submit_decision(self, decision: AgentDecision):
        self.state.decisions.append(decision)

        self.trajectory.append({
            "action": "submit_decision",
            "decision": decision.model_dump(),
        })

        return {"status": "recorded"}
