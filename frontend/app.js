// Conexão automática com o backend
fetch('/status')
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerHTML = `
            <p>Sistema: ${data.system}</p>
            <p>Status: ${data.status}</p>
            <p>IA Thoth: ${data.thoth_ai}</p>
        `;
    })
    .catch(error => {
        document.getElementById('status').innerHTML = 
            "Erro ao conectar ao backend. Verifique o console.";
        console.error(error);
    });
