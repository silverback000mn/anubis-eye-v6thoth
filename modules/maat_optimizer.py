class AccountOptimizer:
    def __init__(self):
        self.actions = [
            "follow",
            "like",
            "comment",
            "unfollow"
        ]
    
    def warmup_account(self, username):
        """Executa sequência de warmup em 7 dias"""
        schedule = {
            "day_1": {"actions": ["like", "follow"], "target": 10},
            "day_2": {"actions": ["like"], "target": 20},
            # ... (complete com os 7 dias)
        }
        return self._execute_schedule(username, schedule)
