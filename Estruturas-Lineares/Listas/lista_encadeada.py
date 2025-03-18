'''
Implementação de Lista Encadeada em Python

Este arquivo demonstra a implementação e uso de uma lista encadeada simples,
incluindo as operações básicas de inserção, remoção, busca e percurso.

Autores: Alef Khatab e Kaynã Barbosa de Miranda
'''

class Node:
    '''Classe que representa um nó na lista encadeada'''
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó (inicialmente None)

class LinkedList:
    '''Implementação de uma lista encadeada simples'''
    def __init__(self):
        self.head = None  # Referência para o primeiro nó (inicialmente None)
        self.size = 0     # Contador de elementos
    
    def is_empty(self):
        '''Verifica se a lista está vazia'''
        return self.head is None
    
    def insert_at_beginning(self, data):
        '''Insere um novo nó no início da lista - O(1)'''
        new_node = Node(data)  # Cria um novo nó
        new_node.next = self.head  # O novo nó aponta para o antigo head
        self.head = new_node  # O head agora é o novo nó
        self.size += 1  # Incrementa o contador
    
    def insert_at_end(self, data):
        '''Insere um novo nó no final da lista - O(n)'''
        new_node = Node(data)  # Cria um novo nó
        
        # Se a lista estiver vazia, o novo nó se torna o head
        if self.is_empty():
            self.head = new_node
        else:
            # Percorre a lista até o último nó
            current = self.head
            while current.next:
                current = current.next
            # Faz o último nó apontar para o novo nó
            current.next = new_node
        
        self.size += 1  # Incrementa o contador
    
    def insert_after(self, prev_data, data):
        '''Insere um novo nó após o nó que contém prev_data - O(n)'''
        # Verifica se a lista está vazia
        if self.is_empty():
            print("Lista vazia, não é possível inserir após um elemento")
            return False
        
        # Procura o nó contendo prev_data
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        
        # Se não encontrou o nó
        if not current:
            print(f"Elemento {prev_data} não encontrado na lista")
            return False
        
        # Cria o novo nó e o insere após o nó encontrado
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
        self.size += 1  # Incrementa o contador
        return True
    
    def delete_node(self, key):
        '''Remove o primeiro nó com valor igual a key - O(n)'''
        # Verifica se a lista está vazia
        if self.is_empty():
            print("Lista vazia, não há o que remover")
            return False
        
        # Caso especial: remover o head
        if self.head.data == key:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Procura o nó a ser removido, mantendo referência ao anterior
        previous = self.head
        current = self.head.next
        
        while current and current.data != key:
            previous = current
            current = current.next
        
        # Se não encontrou o nó
        if not current:
            print(f"Elemento {key} não encontrado na lista")
            return False
        
        # Remove o nó (faz o anterior apontar para o próximo do atual)
        previous.next = current.next
        self.size -= 1
        return True
    
    def search(self, key):
        '''Busca um elemento na lista - O(n)'''
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                return position  # Retorna a posição onde o elemento foi encontrado
            current = current.next
            position += 1
        
        return -1  # Retorna -1 se o elemento não foi encontrado
    
    def print_list(self):
        '''Imprime todos os elementos da lista - O(n)'''
        if self.is_empty():
            print("Lista vazia")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def get_size(self):
        '''Retorna o tamanho da lista - O(1)'''
        return self.size

# Demonstração de uso
def main():
    print("\n=== Lista Encadeada - Demonstração ===\n")
    
    # Criando uma lista encadeada
    linked_list = LinkedList()
    
    print("Inserindo elementos no início da lista:")
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(1)
    linked_list.print_list()  # Deve imprimir: 1 -> 2 -> 3
    
    print("\nInserindo elementos no final da lista:")
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.print_list()  # Deve imprimir: 1 -> 2 -> 3 -> 4 -> 5
    
    print("\nInserindo um elemento após o 3:")
    linked_list.insert_after(3, 3.5)
    linked_list.print_list()  # Deve imprimir: 1 -> 2 -> 3 -> 3.5 -> 4 -> 5
    
    print("\nBuscando elementos:")
    print(f"Posição do elemento 3: {linked_list.search(3)}")
    print(f"Posição do elemento 7: {linked_list.search(7)}")
    
    print("\nRemovendo elementos:")
    linked_list.delete_node(1)  # Remove o primeiro elemento
    linked_list.print_list()
    
    linked_list.delete_node(5)  # Remove o último elemento
    linked_list.print_list()
    
    linked_list.delete_node(3)  # Remove um elemento do meio
    linked_list.print_list()
    
    print(f"\nTamanho da lista: {linked_list.get_size()}")
    
    print("\nTentando remover um elemento que não existe:")
    linked_list.delete_node(10)

if __name__ == "__main__":
    main()