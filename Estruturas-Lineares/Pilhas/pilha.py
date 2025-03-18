'''
Implementação de Pilha em Python

Este arquivo demonstra duas implementações de pilhas: uma baseada em lista Python
e outra baseada em uma lista encadeada.

Autores: Alef Khatab e Kaynã Barbosa de Miranda
'''

# Implementação 1: Pilha usando lista Python
class Stack:
    '''
    Implementação de uma pilha usando lista Python.
    Esta implementação é simples e eficiente para a maioria dos casos.
    '''
    def __init__(self):
        self.items = []  # Lista vazia para armazenar elementos
    
    def is_empty(self):
        '''
        Verifica se a pilha está vazia
        Tempo: O(1)
        '''
        return len(self.items) == 0
    
    def push(self, item):
        '''
        Adiciona um item ao topo da pilha
        Tempo: O(1) amortizado
        '''
        self.items.append(item)  # Adiciona ao final da lista (topo da pilha)
    
    def pop(self):
        '''
        Remove e retorna o item do topo da pilha
        Tempo: O(1) amortizado
        '''
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()  # Remove do final da lista (topo da pilha)
    
    def peek(self):
        '''
        Retorna o item do topo da pilha sem removê-lo
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]  # Retorna o último elemento da lista (topo da pilha)
    
    def size(self):
        '''
        Retorna o número de itens na pilha
        Tempo: O(1)
        '''
        return len(self.items)
    
    def __str__(self):
        '''
        Retorna uma representação em string da pilha
        '''
        return str(self.items)

# Implementação 2: Pilha usando lista encadeada
class Node:
    '''
    Classe que representa um nó na implementação de lista encadeada
    '''
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó

class LinkedStack:
    '''
    Implementação de uma pilha usando lista encadeada.
    Esta implementação é útil quando o tamanho da pilha é imprevisível
    ou quando precisa evitar realocar arrays.
    '''
    def __init__(self):
        self.top = None  # Referência para o topo da pilha
        self.size_count = 0  # Contador de elementos
    
    def is_empty(self):
        '''
        Verifica se a pilha está vazia
        Tempo: O(1)
        '''
        return self.top is None
    
    def push(self, item):
        '''
        Adiciona um item ao topo da pilha
        Tempo: O(1)
        '''
        new_node = Node(item)  # Cria um novo nó
        new_node.next = self.top  # O novo nó aponta para o antigo topo
        self.top = new_node  # O topo agora é o novo nó
        self.size_count += 1  # Incrementa o contador
    
    def pop(self):
        '''
        Remove e retorna o item do topo da pilha
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        
        item = self.top.data  # Armazena o dado do topo
        self.top = self.top.next  # O topo passa a ser o próximo nó
        self.size_count -= 1  # Decrementa o contador
        return item
    
    def peek(self):
        '''
        Retorna o item do topo da pilha sem removê-lo
        Tempo: O(1)
        '''
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data  # Retorna o dado do topo
    
    def size(self):
        '''
        Retorna o número de itens na pilha
        Tempo: O(1)
        '''
        return self.size_count
    
    def __str__(self):
        '''
        Retorna uma representação em string da pilha
        '''
        if self.is_empty():
            return "[]"
        
        current = self.top
        items = []
        
        # Percorre a lista encadeada e adiciona elementos em uma lista
        while current:
            items.append(current.data)
            current = current.next
        
        # Inverte a lista para mostrar o fundo da pilha à esquerda
        items.reverse()  
        return str(items)

# Exemplo de caso de uso: Verificador de parênteses balanceados
def is_balanced(expression):
    '''
    Verifica se os parênteses, colchetes e chaves em uma expressão estão balanceados.
    
    Args:
        expression (str): A expressão a ser verificada
    
    Returns:
        bool: True se os símbolos estão balanceados, False caso contrário
    '''
    stack = Stack()
    opening = "({["
    closing = ")}]"
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()  # A pilha deve estar vazia se todos os símbolos estiverem balanceados

# Exemplo de caso de uso: Conversor de decimal para binário
def decimal_to_binary(decimal_num):
    '''
    Converte um número decimal para binário usando uma pilha.
    
    Args:
        decimal_num (int): O número decimal a ser convertido
    
    Returns:
        str: A representação binária do número
    '''
    if decimal_num == 0:
        return "0"
    
    stack = Stack()
    
    while decimal_num > 0:
        remainder = decimal_num % 2  # Pega o resto da divisão por 2
        stack.push(remainder)        # Empilha o resto
        decimal_num //= 2            # Divide por 2 (divisão inteira)
    
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())  # Desempilha e concatena os dígitos
    
    return binary

# Demonstração de uso
def main():
    print("\n=== Demonstração de Pilhas ===\n")
    
    # Demonstração da pilha baseada em lista
    print("--- Pilha baseada em Lista ---")
    stack = Stack()
    
    print("Empilhando elementos: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print(f"Pilha: {stack}")
    print(f"Tamanho da pilha: {stack.size()}")
    print(f"Elemento do topo: {stack.peek()}")
    
    print("\nDesempilhando elementos:")
    print(f"Removido: {stack.pop()}")
    print(f"Removido: {stack.pop()}")
    print(f"Pilha após remoções: {stack}")
    
    # Demonstração da pilha baseada em lista encadeada
    print("\n--- Pilha baseada em Lista Encadeada ---")
    linked_stack = LinkedStack()
    
    print("Empilhando elementos: 'A', 'B', 'C', 'D'")
    linked_stack.push('A')
    linked_stack.push('B')
    linked_stack.push('C')
    linked_stack.push('D')
    
    print(f"Pilha: {linked_stack}")
    print(f"Tamanho da pilha: {linked_stack.size()}")
    print(f"Elemento do topo: {linked_stack.peek()}")
    
    print("\nDesempilhando elementos:")
    print(f"Removido: {linked_stack.pop()}")
    print(f"Removido: {linked_stack.pop()}")
    print(f"Pilha após remoções: {linked_stack}")
    
    # Demonstração do verificador de parênteses balanceados
    print("\n--- Verificador de Parênteses Balanceados ---")
    expressions = [
        "(a + b) * (c - d)",
        "[{(a + b) * (c - d)}]",
        "(a + b) * (c - d])",
        "{[}]"
    ]
    
    for expr in expressions:
        result = is_balanced(expr)
        print(f"'{expr}' está balanceado? {result}")
    
    # Demonstração do conversor decimal para binário
    print("\n--- Conversor Decimal para Binário ---")
    decimals = [10, 42, 255, 128, 0]
    
    for num in decimals:
        binary = decimal_to_binary(num)
        print(f"Decimal {num} em binário: {binary}")

if __name__ == "__main__":
    main()