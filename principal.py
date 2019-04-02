arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

for linha in arquivo_contatos:
    print(linha, end='')
