// Conexão com o endpoint correto do backend
document.addEventListener('DOMContentLoaded', () => {
    fetch('/status')
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(data => {
            document.getElementById('status').innerHTML = `
                <p>Projeto: ${data.project}</p>
                <p>Versão: ${data.version}</p>
                <p>Status: ${data.thoth_online ? 'Online' : 'Offline'}</p>
                <p>Última atualização: ${new Date(data.last_update).toLocaleString()}</p>
            `;
        })
        .catch(error => {
            document.getElementById('status').innerHTML = 
                "Erro ao conectar ao backend. Verifique o console.";
            console.error("Erro na requisição:", error);
        });
});
