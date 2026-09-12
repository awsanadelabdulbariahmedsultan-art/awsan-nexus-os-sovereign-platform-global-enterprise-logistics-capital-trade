class GlobalPortsEngine:
    def __init__(self):
        self.ports = [
            {"code": "YE-ADE", "name": "Aden Container Terminal", "country": "Yemen", "status": "ACTIVE"},
            {"code": "YE-HOD", "name": "Hodeidah Port", "country": "Yemen", "status": "ACTIVE"},
            {"code": "SG-SIN", "name": "Singapore Port", "country": "Singapore", "status": "OPTIMAL"}
        ]
    def get_ports(self):
        return self.ports
