class AnubisDashboard {
    constructor() {
        this.socket = new WebSocket("wss://anubis-eye.com/realtime");
        this.stats = {
            accounts: 0,
            proxies: 0,
            creationSpeed: 0
        };
    }

    init() {
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this._updateStats(data);
            this._animateTempleLights(data.status);
        };
    }

    _updateStats(data) {
        document.getElementById("live-accounts").textContent = data.accounts;
        document.getElementById("creation-speed").textContent = `${data.speed} contas/h`;
        
        // Atualiza gráfico de performance
        performanceChart.update(data.performance);
    }
}
