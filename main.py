import os
from datetime import datetime
from scripts.processamento import processar_dados


def criar_pastas():
    """Garante que todas as pastas principais existam."""
    pastas = ["dados_brutos", "dados_processados", "resultados"]
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"📁 Pasta criada: {pasta}")
        else:
            print(f"✅ Pasta encontrada: {pasta}")


def registrar_log(mensagem):
    """Salva logs em resultados/log.txt"""
    log_path = os.path.join("resultados", "log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}\n")


def main():
    print("🚀 Iniciando pipeline de confiabilidade...\n")
    registrar_log("Início do processamento.")

    try:
        criar_pastas()
        processar_dados()  # 🔁 Função principal do script de processamento
        print("\n✅ Processamento concluído com sucesso!")
        registrar_log("Processamento concluído com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro durante o processamento: {e}")
        registrar_log(f"Erro: {e}")


if __name__ == "__main__":
    main()

