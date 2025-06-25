from collections import deque
import random

class HAPIDistributor:
    def __init__(self):
        self.proxy_pool = deque()
        self.performance_metrics = {}
        self.current_load = {}

    def assign_proxy(self, task_type):
        if not self.proxy_pool:
            self._refresh_proxy_pool()

        sorted_proxies = sorted(
            self.proxy_pool,
            key=lambda x: self.performance_metrics.get(x, {}).get('success_rate', 0),
            reverse=True
        )
        selected = next(
            (p for p in sorted_proxies if self.current_load.get(p, 0) < 3),
            random.choice(sorted_proxies) if sorted_proxies else None
        )
        
        if selected:
            self.current_load[selected] = self.current_load.get(selected, 0) + 1
        return selected

    def _refresh_proxy_pool(self):
        self.proxy_pool = deque([
            "194.32.78.1:8080",
            "185.243.56.2:3128",
            "201.166.34.3:8080"
        ])
