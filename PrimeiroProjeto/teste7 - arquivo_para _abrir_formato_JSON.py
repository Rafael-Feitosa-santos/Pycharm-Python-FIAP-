import json
arquivo = open("c:\\Arquivo teste\\dicionario.json", "r", encoding="UTF-8")
conteudo = arquivo.read()
arquivo.close()
agenda = json.loads(conteudo)

