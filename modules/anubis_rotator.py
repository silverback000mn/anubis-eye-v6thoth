import requests

class ProxyRotator:
    def __init__(self):
        self.proxy_pool = []
        self.current_index = 0
    
    def _refresh_proxies(self):
        try:
            response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http")
            self.proxy_pool = response.text.split('\r\n')
        except:
            self.proxy_pool = ["default_proxy:8080"]  # Fallback

    def get_proxy(self):
        if not self.proxy_pool or self.current_index >= len(self.proxy_pool):
            self._refresh_proxies()
            self.current_index = 0
            
        proxy = self.proxy_pool[self.current_index]
        self.current_index += 1
        return proxy
