contatos = {
    "Clark Kent":{
        "celular":"123456",
        "email":"clark@krypton.com"
    },
    "Bruce Wayne":{
        "celular":"654321",
        "email":"bat@caverna.com"
    }
}

for nome, formas_contato in contatos.items():
    print(f"O contato {nome}")
    for forma, valor in formas_contato.items():
        print(f"pode ser contato pelo seu {forma}, através do {valor}")

    print("\n\n")
