
from enum import Enum
from pydantic import BaseModel, Field


class Decision(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    FLAG = "flag"


class Vendor(BaseModel):
    vendor_id: str
    name: str
    active: bool = True


class PurchaseOrder(BaseModel):
    po_id: str
    vendor_id: str
    approved_amount: float = Field(ge=0)
    approved: bool = True


class Invoice(BaseModel):
    invoice_id: str
    vendor_id: str
    po_id: str
    amount: float = Field(gt=0)


class Payment(BaseModel):
    payment_id: str
    invoice_id: str
    amount: float = Field(gt=0)
    completed: bool = True


class AgentDecision(BaseModel):
    invoice_id: str
    decision: Decision
    reason: str
