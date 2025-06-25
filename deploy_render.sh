#!/bin/bash
# Configuração Divina para o Render

echo "𓃭 Iniciando Deploy do Anúbis Eye v6 𓃭"

# 1. Instalação de Dependências
pip install -r requirements.txt
npm install --prefix frontend

# 2. Configuração do Banco de Dados
if [ ! -f "DATA/sacred_storage/book_of_thoth.db" ]; then
    sqlite3 DATA/sacred_storage/book_of_thoth.db < DATA/sacred_storage/init_db.sql
    echo "Banco de dados sagrado inicializado"
fi

# 3. Build do Frontend
npm run build --prefix frontend

# 4. Inicialização do Sistema
uvicorn core.anubis_connector:AnubisOrchestrator --host 0.0.0.0 --port $PORT --reload
