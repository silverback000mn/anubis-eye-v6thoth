class HorusFirewall:
    def __init__(self):
        self.rules = {
            "max_actions_per_minute": 20,
            "allowed_countries": ["BR", "US", "CA"],
            "forbidden_patterns": [
                "follow_spam",
                "like_bot"
            ]
        }

    def validate_command(self, command):
        """Aplica 7 camadas de segurança"""
        checks = [
            self._check_rate_limit(),
            self._check_geo_patterns(),
            self._detect_bot_patterns(command),
            self._verify_authorization(),
            self._inspect_proxy_health(),
            self._validate_time_window(),
            self._scan_for_ban_risk()
        ]
        return all(checks)

    def _detect_bot_patterns(self, command):
        patterns = {
            "repetitive": r"(.)\1{5}",
            "sequential": r"user\d{4}"
        }
        return not any(
            re.search(pattern, command, re.IGNORECASE)
            for pattern in patterns.values()
        )
