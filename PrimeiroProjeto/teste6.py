import json

contatos = {
    "Clark Kent":{
       "Celular":"123456",
       "Email":"super@krypton.com"
    },
    "Bruce Wayne":{
       "Celular":"654321",
       "Email":"bat@caverna.com.br"
    }
 }


arquivo = open("c:\\Arquivo teste\\dicionario.json", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)

arquivo.write(conteudo)

arquivo.close()

