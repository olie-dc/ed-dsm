from lib.deque import Deque

# Instancia um novo deque
deque = Deque()

# PARTE 1: deque se comportando como fila comum

deque.insert_back("Antero")      # deque.insert_back = fila.enqueue
deque.insert_back("Ermelinda")
deque.insert_back("Procópio")
deque.insert_back("Hermógenes")
deque.insert_back("Ivanildes")
deque.insert_back("Olentina")
print(deque)

removido = deque.remove_front()  # deque.remove_front = fila.dequeue
print(f"{removido} foi removido do início do deque")
print(deque)

nome = "Tibúrcio"
deque.insert_back(nome)
print(f"{nome} foi inserido no final do deque")
print(deque)

primeiro = deque.peek()
print(f"{primeiro} é quem está no início do deque")
print(deque)

print("-" * 80)

# PARTE 2: funcionalidades exclusivas do deque

# Inserção prioritária (na primeira posição)
nome = "Bartira"
deque.insert_front(nome)        # insert_front só existe no deque
print(f"{nome} foi inserida no início do deque")
print(deque)

# Desistência (remoção do último item)
desistente = deque.remove_back()    # remove_back só existe no deque
print(f"{desistente} foi removido do final do deque")
print(deque)

# Consultando o último elemento do deque
ultimo = deque.peek(False)           # peek(False) só existe no deque
print(f"Agora, {ultimo} está no final do deque")
print(deque)