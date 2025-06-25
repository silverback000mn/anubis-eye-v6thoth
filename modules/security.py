class HorusFirewall:
    def validate_command(self, command: str) -> bool:
        """Valida comandos contra padrões maliciosos"""
        blocked_patterns = [
            "rm -rf", "sudo", "drop table",
            "eval(", "exec(", "os.system"
        ]
        return not any(pattern in command.lower() for pattern in blocked_patterns)

class SecurityError(Exception):
    pass
