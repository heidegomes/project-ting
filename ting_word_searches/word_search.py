def exists_word(word, instance):
    lista = []

    for i in range(len(instance)):
        result = instance.search(i)

        dicionario = {
            "palavra": word,
            "arquivo": result["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for i, linha in enumerate(result["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                dicionario["ocorrencias"].append({"linha": i + 1})

        if len(dicionario["ocorrencias"]):
            lista.append(dicionario)

    return lista


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
