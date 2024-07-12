import os
import re

def remove_linhas_comentadas(nome_arquivo):
    # Lista para armazenar linhas não comentadas
    linhas_nao_comentadas = []

    # Expressão regular para identificar comentários no início da linha
    padrao_comentario = r'#'

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Verifica se a linha é um comentário
            if not re.match(padrao_comentario, linha):
                linhas_nao_comentadas.append(linha)

    # Sobrescreve o arquivo com as linhas não comentadas
    with open(nome_arquivo, 'w') as arquivo:
        for linha in linhas_nao_comentadas:
            arquivo.write(linha)

def percorrer_diretorio(diretorio):
    # Percorre todos os arquivos no diretório
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            # Verifica se o arquivo é um arquivo de texto (pode ajustar conforme necessário)
            if arquivo.endswith('.yaml'):
                caminho_completo = os.path.join(raiz, arquivo)
                remove_linhas_comentadas(caminho_completo)

diretorio_alvo = 'C:/Users/Motta/Desktop/devops/rodar'
percorrer_diretorio(diretorio_alvo)
