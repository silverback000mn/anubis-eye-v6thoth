import asyncio
from modules.security import HorusFirewall, SecurityError
from core.hapi_distributor import HAPIDistributor
from core.thoth_ai import ThothAI

class AnubisOrchestrator:
    def __init__(self):
        self.firewall = HorusFirewall()
        self.distributor = HAPIDistributor()
        self.thoth = ThothAI()

    async def execute_divine_command(self, command: str):
        """Fluxo principal corrigido"""
        if not self.firewall.validate_command(command):
            raise SecurityError("Firewall bloqueou o comando")

        execution_plan = self.thoth.interpret(command)
        tasks = [
            self._execute_task(task, self.distributor.assign_proxy(task['type']))
            for task in execution_plan.get('tasks', [])
        ]
        return await asyncio.gather(*tasks)

    async def _execute_task(self, task, proxy):
        try:
            return await task['function'](proxy=proxy, **task.get('parameters', {}))
        except Exception as e:
            self.thoth.log_error(e)
            return {"status": "failed", "error": str(e)}
