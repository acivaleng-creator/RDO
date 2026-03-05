import os
import platform

# 1. DETECTAR O SISTEMA OPERACIONAL
SISTEMA = platform.system()

# 2. DEFINIR A RAIZ DOS DADOS (Caminhos Blindados)
if SISTEMA == "Windows":
    # Caminho fixo para o seu Windows
    DIRETORIO_RAIZ = r"C:\Users\Acival-.DESKTOP-TTRED3S\SistemaRDO_Dados"
else:
    # A MÁGICA PARA O ANDROID: O Flet libera a pasta HOME para gravação nativa
    DIRETORIO_RAIZ = os.path.join(os.environ.get("HOME", os.path.expanduser("~")), "dados_rdo")

# 3. CRIAR A ESTRUTURA SE NÃO EXISTIR (Com proteção anti-travamento)
try:
    if not os.path.exists(DIRETORIO_RAIZ):
        os.makedirs(DIRETORIO_RAIZ, exist_ok=True)
except Exception as e:
    print(f"Erro ao criar pasta raiz: {e}")
    pass # Impede a tela branca se o celular bloquear

# 4. CAMINHOS DAS SUBPASTAS
PASTA_ATIVOS = os.path.join(DIRETORIO_RAIZ, "ativos")
PASTA_BANCO = os.path.join(DIRETORIO_RAIZ, "banco_rdos")

# Garante que as subpastas existam sem travar o app
for pasta in [PASTA_ATIVOS, PASTA_BANCO]:
    try:
        if not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)
    except:
        pass

# 5. BANCO DE DADOS SQLITE PRINCIPAL
CAMINHO_DB = os.path.join(DIRETORIO_RAIZ, "database_rdo.db")
