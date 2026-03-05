import os
import platform

# 1. DETECTAR O SISTEMA OPERACIONAL (Sem acentos para o Linux)
SISTEMA = platform.system()

# 2. DEFINIR A RAIZ DOS DADOS
if SISTEMA == "Windows":
    # Caminho fixo para o seu Windows
    DIRETORIO_RAIZ = r"C:\Users\Acival-.DESKTOP-TTRED3S\SistemaRDO_Dados"
else:
    # No Android, usamos a pasta interna do aplicativo
    DIRETORIO_RAIZ = os.path.join(os.getcwd(), "dados_rdo")

# 3. CRIAR A ESTRUTURA SE NAO EXISTIR
if not os.path.exists(DIRETORIO_RAIZ):
    os.makedirs(DIRETORIO_RAIZ, exist_ok=True)

# 4. CAMINHOS DAS SUBPASTAS
PASTA_ATIVOS = os.path.join(DIRETORIO_RAIZ, "ativos")
PASTA_BANCO = os.path.join(DIRETORIO_RAIZ, "banco_rdos")

# Garante que as subpastas existam
for pasta in [PASTA_ATIVOS, PASTA_BANCO]:
    if not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

# 5. BANCO DE DADOS SQLITE PRINCIPAL
CAMINHO_DB = os.path.join(DIRETORIO_RAIZ, "database_rdo.db")