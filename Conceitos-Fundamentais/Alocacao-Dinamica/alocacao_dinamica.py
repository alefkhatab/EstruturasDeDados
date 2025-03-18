'''
Demonstração de Alocação Dinâmica de Memória em Python

Observação: Python gerencia automaticamente a alocação de memória,
mas este exemplo ilustra o conceito de alocação dinâmica através
de estruturas que crescem conforme necessário.

Autores: Alef Khatab
'''

# 1. Lista dinâmica
class DynamicList:
    def __init__(self):
        self.items = []  # Lista vazia - cresce dinamicamente
    
    def add(self, item):
        self.items.append(item)  # Adiciona item, memória é alocada conforme necessário
    
    def remove(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice fora dos limites!")
        return self.items.pop(index)  # Remove e retorna o item, libera memória
    
    def get(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice fora dos limites!")
        return self.items[index]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# 2. Lista encadeada - exemplo clássico de estrutura com alocação dinâmica
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Referência para o próximo nó

class LinkedList:
    def __init__(self):
        self.head = None  # Início da lista
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)  # Aloca dinamicamente um novo nó
        
        if not self.head:  # Se a lista estiver vazia
            self.head = new_node
        else:
            current = self.head
            # Navega até o último nó
            while current.next:
                current = current.next
            current.next = new_node  # Liga o último nó ao novo
        
        self.size += 1
    
    def prepend(self, data):
        new_node = Node(data)  # Aloca dinamicamente um novo nó
        new_node.next = self.head  # Novo nó aponta para o antigo head
        self.head = new_node  # Atualiza o head
        self.size += 1
    
    def delete(self, data):
        if not self.head:  # Se a lista estiver vazia
            return False
        
        # Caso especial: o nó a ser removido é o head
        if self.head.data == data:
            self.head = self.head.next  # O head passa a ser o próximo nó
            self.size -= 1
            return True
        
        # Caso geral: busca o nó a ser removido
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        # Se encontrou o nó
        if current.next:
            current.next = current.next.next  # Pula o nó a ser removido
            self.size -= 1
            return True
        
        return False  # Nó não encontrado
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

# 3. Matriz dinâmica
class DynamicMatrix:
    def __init__(self):
        self.rows = []  # Lista de linhas (cada linha é uma lista)
    
    def add_row(self, row_data=None):
        if row_data is None:
            self.rows.append([])  # Adiciona uma linha vazia
        else:
            self.rows.append(list(row_data))  # Adiciona linha com dados
    
    def set_value(self, row, col, value):
        # Expande a matriz se necessário
        while row >= len(self.rows):
            self.add_row()
        
        current_row = self.rows[row]
        while col >= len(current_row):
            current_row.append(None)  # Expande a coluna
        
        self.rows[row][col] = value
    
    def get_value(self, row, col):
        if row < 0 or row >= len(self.rows):
            raise IndexError("Índice de linha fora dos limites!")
        
        current_row = self.rows[row]
        if col < 0 or col >= len(current_row):
            raise IndexError("Índice de coluna fora dos limites!")
        
        return current_row[col]
    
    def get_dimensions(self):
        if not self.rows:
            return (0, 0)
        
        max_cols = max(len(row) for row in self.rows) if self.rows else 0
        return (len(self.rows), max_cols)
    
    def print_matrix(self):
        for row in self.rows:
            print(row)

# Demonstração de uso
def main():
    print("\n=== Demonstração de Alocação Dinâmica ===\n")
    
    # Usando lista dinâmica
    print("--- Lista Dinâmica ---")
    students = DynamicList()
    
    # Adicionando elementos - a lista cresce dinamicamente
    students.add("Alice")
    students.add("Bob")
    print(f"Lista após adicionar 2 estudantes: {students}")
    
    # Adicionando mais elementos
    students.add("Charlie")
    students.add("David")
    students.add("Eve")
    print(f"Lista após adicionar mais 3 estudantes: {students}")
    
    # Removendo elementos
    removed = students.remove(2)  # Remove Charlie
    print(f"Removido: {removed}")
    print(f"Lista após remover: {students}")
    
    # Usando lista encadeada
    print("\n--- Lista Encadeada ---")
    linked_list = LinkedList()
    
    # Adicionando elementos no final
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print(f"Lista encadeada após append: {linked_list}")
    
    # Adicionando elementos no início
    linked_list.prepend(5)
    print(f"Lista encadeada após prepend: {linked_list}")
    
    # Removendo elementos
    linked_list.delete(20)
    print(f"Lista encadeada após delete(20): {linked_list}")
    print(f"Tamanho da lista encadeada: {linked_list.get_size()}")
    
    # Usando matriz dinâmica
    print("\n--- Matriz Dinâmica ---")
    matrix = DynamicMatrix()
    
    # Adicionando dados
    matrix.add_row([1, 2, 3])
    matrix.add_row([4, 5])
    print("Matriz inicial:")
    matrix.print_matrix()
    
    # Expandindo a matriz dinamicamente
    matrix.set_value(2, 3, 99)  # Isso cria a linha 2 e expande até a coluna 3
    print("\nMatriz após expansão:")
    matrix.print_matrix()
    
    # Obtendo dimensões
    rows, cols = matrix.get_dimensions()
    print(f"\nDimensões da matriz: {rows}x{cols}")
    
    # Adicionando em posições dispersas
    matrix.set_value(5, 5, 42)
    print("\nMatriz após adicionar em posição dispersa:")
    matrix.print_matrix()

if __name__ == "__main__":
    main()
