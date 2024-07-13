import os
import re

def remove_linhas_comentadas(nome_arquivo):
    linhas_nao_comentadas = []

    padrao_comentario = r'#' 

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if not re.match(padrao_comentario, linha):
                    linhas_nao_comentadas.append(linha)

        with open(nome_arquivo, 'w') as arquivo:
            for linha in linhas_nao_comentadas:
                arquivo.write(linha)
        
        print(f"Linhas comentadas removidas de: {nome_arquivo}")

    except IOError as e:
        print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar {nome_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    try:
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if arquivo.endswith('.yaml'):
                    caminho_completo = os.path.join(raiz, arquivo)
                    remove_linhas_comentadas(caminho_completo)
        print("Processo concluído.")

    except Exception as e:
        print(f"Ocorreu um erro ao percorrer o diretório {diretorio}: {e}")

diretorio_alvo = '../applications'

percorrer_diretorio(diretorio_alvo)