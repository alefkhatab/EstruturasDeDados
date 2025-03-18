'''
Comparação de Desempenho - Estruturas de Dados
Este script demonstra como diferentes estruturas de dados podem afetar o desempenho de operações comuns.

Autores: Alef Khatab
'''

import time
import random

def measure_time(func):
    '''
    Decorator para medir o tempo de execução de uma função
    '''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} levou {(end_time - start_time) * 1000:.2f} ms para executar")
        return result
    return wrapper

# Exemplo 1: Busca em Lista vs Dicionário
@measure_time
def find_in_list(item, data_list):
    '''
    Busca um item em uma lista - O(n)
    '''
    for i in data_list:
        if i == item:
            return True
    return False

@measure_time
def find_in_dict(item, data_dict):
    '''
    Busca um item em um dicionário - O(1) em média
    '''
    return item in data_dict

# Exemplo 2: Inserção no meio de uma lista vs no fim
@measure_time
def insert_middle_list(data_list, items):
    '''
    Insere items no meio da lista - O(n) para cada inserção
    '''
    middle = len(data_list) // 2
    for item in items:
        data_list.insert(middle, item)
    return data_list

@measure_time
def insert_end_list(data_list, items):
    '''
    Insere items no fim da lista - O(1) amortizado para cada inserção
    '''
    for item in items:
        data_list.append(item)
    return data_list

# Demonstração
def main():
    print("\n=== Demonstração de Impacto das Estruturas de Dados no Desempenho ===\n")
    
    # Preparando dados
    size = 100000
    search_item = random.randint(0, size - 1)
    items_to_insert = [random.randint(0, size) for _ in range(1000)]
    
    print("\n--- Exemplo 1: Busca em Lista vs Dicionário ---")
    test_list = list(range(size))
    test_dict = {i: i for i in range(size)}
    
    print(f"Buscando o item {search_item} em uma lista de {size} elementos...")
    found_in_list = find_in_list(search_item, test_list)
    
    print(f"Buscando o item {search_item} em um dicionário de {size} elementos...")
    found_in_dict = find_in_dict(search_item, test_dict)
    
    print(f"Resultado da busca: {found_in_list == found_in_dict}")
    
    print("\n--- Exemplo 2: Inserção no meio vs no fim da lista ---")
    test_list_middle = list(range(size))
    test_list_end = list(range(size))
    
    print(f"Inserindo 1000 itens no meio de uma lista de {size} elementos...")
    insert_middle_list(test_list_middle, items_to_insert)
    
    print(f"Inserindo 1000 itens no fim de uma lista de {size} elementos...")
    insert_end_list(test_list_end, items_to_insert)

if __name__ == "__main__":
    main()
