document.addEventListener('DOMContentLoaded', () => {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').innerHTML = `
                <p>Projeto: ${data.project}</p>
                <p>Status: ${data.thoth_online ? 'ONLINE' : 'OFFLINE'}</p>
                <p>Última atualização: ${new Date(data.last_update).toLocaleString()}</p>
            `;
        });
});
