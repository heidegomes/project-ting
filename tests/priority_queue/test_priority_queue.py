import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 9})
    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 2})
    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 7})
    queue.enqueue({"qtd_linhas": 11})
    queue.enqueue({"qtd_linhas": 3})
    assert len(queue) == 7

    removed_item = queue.dequeue()
    assert removed_item == {"qtd_linhas": 4}

    item = queue.search(0)
    assert item == {"qtd_linhas": 2}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(len(queue))
