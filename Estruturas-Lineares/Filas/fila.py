'''
Implementação de Fila em Python

Este arquivo demonstra duas implementações de filas: uma baseada em lista Python (dinâmica) 
e outra implementando uma fila circular baseada em array com tamanho fixo.

Autores: Alef Khatab e Kaynã Barbosa de Miranda
'''

# Implementação 1: Fila usando lista Python (implementação dinâmica)
class Queue:
    '''
    Implementação de uma fila usando lista Python.
    Esta implementação é dinâmica (cresce conforme necessário).
    '''
    def __init__(self):
        self.items = []  # Lista vazia para armazenar elementos da fila
    
    def is_empty(self):
        '''
        Verifica se a fila está vazia
        Tempo: O(1)
        '''
        return len(self.items) == 0
    
    def enqueue(self, item):
        '''
        Adiciona um item ao final da fila
        Tempo: O(1) amortizado
        '''
        self.items.append(item)  # Adiciona ao final da lista
    
    def dequeue(self):
        '''
        Remove e retorna o item do início da fila
        Tempo: O(n) - devido à reorganização da lista
        '''
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)  # Remove do início da lista
    
    def peek(self):
        '''
        Retorna o item do início da fila sem removê-lo
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]  # Retorna o primeiro elemento
    
    def size(self):
        '''
        Retorna o número de itens na fila
        Tempo: O(1)
        '''
        return len(self.items)
    
    def __str__(self):
        '''
        Retorna uma representação em string da fila
        '''
        return str(self.items)

# Implementação 2: Fila circular baseada em array (tamanho fixo)
class CircularQueue:
    '''
    Implementação de uma fila circular usando um array de tamanho fixo.
    Evita o problema de reorganização da lista após dequeue.
    '''
    def __init__(self, capacity=10):
        self.capacity = capacity  # Tamanho máximo da fila
        self.queue = [None] * capacity  # Array para armazenar elementos
        self.front = 0  # Índice do primeiro elemento
        self.rear = 0  # Índice da próxima posição disponível
        self.size = 0  # Número de elementos na fila
    
    def is_empty(self):
        '''
        Verifica se a fila está vazia
        Tempo: O(1)
        '''
        return self.size == 0
    
    def is_full(self):
        '''
        Verifica se a fila está cheia
        Tempo: O(1)
        '''
        return self.size == self.capacity
    
    def enqueue(self, item):
        '''
        Adiciona um item ao final da fila
        Tempo: O(1)
        '''
        if self.is_full():
            raise IndexError("Enqueue to a full queue")
        
        self.queue[self.rear] = item  # Adiciona item no índice rear
        self.rear = (self.rear + 1) % self.capacity  # Atualiza rear de forma circular
        self.size += 1
    
    def dequeue(self):
        '''
        Remove e retorna o item do início da fila
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        item = self.queue[self.front]  # Obtém o item do início
        self.queue[self.front] = None  # Limpa a posição
        self.front = (self.front + 1) % self.capacity  # Atualiza front de forma circular
        self.size -= 1
        return item
    
    def peek(self):
        '''
        Retorna o item do início da fila sem removê-lo
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[self.front]
    
    def get_size(self):
        '''
        Retorna o número de itens na fila
        Tempo: O(1)
        '''
        return self.size
    
    def __str__(self):
        '''
        Retorna uma representação em string da fila
        '''
        if self.is_empty():
            return "[]"
        
        result = []
        index = self.front
        for _ in range(self.size):
            result.append(self.queue[index])
            index = (index + 1) % self.capacity
        
        return str(result)

# Demonstração de uso
def main():
    print("\n=== Demonstração de Filas ===\n")
    
    # Demonstração da fila baseada em lista
    print("--- Fila Dinâmica (baseada em lista) ---")
    queue = Queue()
    
    print("Enfileirando elementos: 10, 20, 30, 40")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    
    print(f"Fila: {queue}")
    print(f"Tamanho da fila: {queue.size()}")
    print(f"Elemento da frente: {queue.peek()}")
    
    print("\nDesenfileirando elementos:")
    print(f"Removido: {queue.dequeue()}")
    print(f"Removido: {queue.dequeue()}")
    print(f"Fila após remoções: {queue}")
    
    print("\nEnfileirando mais elementos: 50, 60")
    queue.enqueue(50)
    queue.enqueue(60)
    print(f"Fila final: {queue}")
    
    # Demonstração da fila circular
    print("\n--- Fila Circular (tamanho fixo) ---")
    circular_queue = CircularQueue(5)  # Capacidade de 5 elementos
    
    print("Enfileirando elementos: 'A', 'B', 'C', 'D', 'E'")
    circular_queue.enqueue('A')
    circular_queue.enqueue('B')
    circular_queue.enqueue('C')
    circular_queue.enqueue('D')
    circular_queue.enqueue('E')
    
    print(f"Fila: {circular_queue}")
    print(f"Tamanho da fila: {circular_queue.get_size()}")
    print(f"Fila cheia? {circular_queue.is_full()}")
    
    print("\nDesenfileirando elementos:")
    print(f"Removido: {circular_queue.dequeue()}")
    print(f"Removido: {circular_queue.dequeue()}")
    print(f"Fila após remoções: {circular_queue}")
    
    print("\nEnfileirando mais elementos: 'X', 'Y'")
    circular_queue.enqueue('X')
    circular_queue.enqueue('Y')
    print(f"Fila final: {circular_queue}")
    
    # Demonstrando a natureza circular
    print("\nDemonstrando a natureza circular:")
    print(f"Removido: {circular_queue.dequeue()}")
    print(f"Removido: {circular_queue.dequeue()}")
    print(f"Removido: {circular_queue.dequeue()}")
    
    print("\nEnfileirando elementos após circular: 'Z', '1', '2'")
    circular_queue.enqueue('Z')
    circular_queue.enqueue('1')
    circular_queue.enqueue('2')
    print(f"Fila final: {circular_queue}")

if __name__ == "__main__":
    main()