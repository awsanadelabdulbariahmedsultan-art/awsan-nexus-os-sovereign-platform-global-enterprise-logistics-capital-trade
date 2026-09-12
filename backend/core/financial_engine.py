from typing import Dict, List
from datetime import datetime

class FinancialEngine:
    def __init__(self):
        self.ledger: List[Dict] = []
        self.models = [f"Model_{i+1:02d}" for i in range(94)]

    def create_journal_entry(self, dr: str, cr: str, amount: float, desc: str, user: str) -> Dict:
        entry = {
            "id": f"JE-{len(self.ledger)+1001}",
            "dr": dr, "cr": cr, "amount": amount, "desc": desc,
            "user": user, "status": "PENDING_APPROVAL", "created_at": datetime.utcnow().isoformat()
        }
        self.ledger.append(entry)
        return entry

    def post_entry(self, entry_id: str, role: str, approver: str) -> Dict:
        if role not in ["CFO", "CHIEF_AUDITOR", "SYSTEM_OWNER"]:
            raise PermissionError("يمنع ترحيل أي قيد دون إذن معتمد من المدير المالي أو المالك السيادي.")
        for e in self.ledger:
            if e["id"] == entry_id:
                e["status"] = "POSTED"
                e["approved_by"] = f"{approver} ({role})"
                return e
        raise ValueError("القيد غير موجود")

    def get_stats(self) -> Dict:
        return {
            "total_posted": sum(e["amount"] for e in self.ledger if e["status"] == "POSTED"),
            "pending_count": sum(1 for e in self.ledger if e["status"] == "PENDING_APPROVAL"),
            "models_available": len(self.models)
        }
