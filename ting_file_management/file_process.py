from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    dicionario = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    for i in range(len(instance)):
        result = instance.search(i)
        if result["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(dicionario)
    print(dicionario)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return None

    removed_item = instance.dequeue()
    print(f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        print(item, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
