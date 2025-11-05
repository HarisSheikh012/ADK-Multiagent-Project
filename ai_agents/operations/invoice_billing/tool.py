def create_invoice(client: str, amount: float, due_days: int = 14) -> str:
    invoice_id = abs(hash(client + str(amount))) % 100000
    return f"Invoice #{invoice_id} for {client}: ${amount:.2f}, due in {due_days} days."
