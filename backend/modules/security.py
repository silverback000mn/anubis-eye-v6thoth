class HorusFirewall:
    def validate_command(self, command: str) -> bool:
        blocked = ["rm", "sudo", "drop"]
        return not any(cmd in command.lower() for cmd in blocked)

class SecurityError(Exception):
    pass
