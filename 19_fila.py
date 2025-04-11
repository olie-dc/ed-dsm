from lib.queue import Queue

# Inicializa uma fila
fila_ubs = Queue()

# Insere algumas pessoas na fila
fila_ubs.enqueue("Leotildes")
fila_ubs.enqueue("Otacílio")
fila_ubs.enqueue("Waldisney")
fila_ubs.enqueue("Adamastor")
fila_ubs.enqueue("Marizete")
fila_ubs.enqueue("Bartira")

print(fila_ubs)

# Atende ao primeiro da fila
atendido = fila_ubs.dequeue()
print(f"Foi atendido: {atendido}")
print(fila_ubs)

# Consulta o próximo a ser atendido
proximo = fila_ubs.peek()
print(f"{proximo} será o próximo a ser chamado")
print(fila_ubs)

# Mais duas pessoas chegaram na fila
fila_ubs.enqueue("Gervásio")
fila_ubs.enqueue("Dulce")
print(fila_ubs)

# Atende ao primeiro da fila
atendido = fila_ubs.dequeue()
print(f"Foi atendido: {atendido}")
print(fila_ubs)