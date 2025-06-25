class DivineAPI:
    def __init__(self):
        self.endpoints = {
            "check_ban": "https://api.anubis-eye.com/v1/bancheck",
            "proxy_health": "https://api.anubis-eye.com/v1/proxystatus"
        }

    def send_offering(self, data):
        """Envia dados com criptografia de Thoth"""
        encrypted = self._encrypt(data)
        return requests.post(
            self.endpoints["check_ban"],
            json={"hieroglyph": encrypted},
            headers={"Authorization": f"Bearer {os.getenv('DIVINE_KEY')}"}
        )
