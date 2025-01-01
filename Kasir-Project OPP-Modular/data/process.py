class Process:
    TAX_RATE = 0.1  # Pajak 10%
    SERVICE_CHARGE = 0.05  # Biaya layanan 5%

    def __init__(self, data):
        self.data = data

    def calculate_subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.data.get_all_items())

    def calculate_tax(self, subtotal):
        return subtotal * self.TAX_RATE

    def calculate_service_charge(self, subtotal):
        return subtotal * self.SERVICE_CHARGE

    def calculate_total(self, subtotal, tax, service_charge):
        return subtotal + tax + service_charge
