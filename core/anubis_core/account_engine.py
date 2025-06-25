class AccountEngine:
    def __init__(self):
        self.creation_methods = {
            'primary': SeleniumCreator(),
            'secondary': PlaywrightCreator(),
            'fallback': PuppeteerCreator()
        }
    
    def create_account_flow(self):
        """Fluxo completo de criação"""
        for method_name, creator in self.creation_methods.items():
            result = creator.execute()
            if result['status'] == 'success':
                return self._optimize_new_account(result)
        
        raise CreationError("Todos os métodos falharam")

    def _optimize_new_account(self, account_data):
        """7 dias de otimização"""
        optimizer = MaatOptimizer()
        return optimizer.process(
            account_data,
            days=7,
            daily_actions={
                'follow': 15,
                'like': 30,
                'post': 1
            }
        )
