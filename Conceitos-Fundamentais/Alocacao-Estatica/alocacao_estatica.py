'''
Demonstração de Alocação Estática de Memória em Python

Observação: Python gerencia automaticamente a alocação de memória, mas este exemplo
ilustará o conceito de alocação estática através de estruturas de tamanho fixo.

Autores: Alef Khatab 
'''

# 1. Variáveis globais (alocação estática)
MAX_STUDENTS = 30
COURSE_NAME = "Estruturas de Dados"

# 2. Lista de tamanho fixo (semelhante a um array estático)
class FixedSizeArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size  # Aloca espaço para 'size' elementos
        self.count = 0
    
    def add(self, item):
        if self.count >= self.size:
            raise IndexError("Array está cheio - memória estática esgotada!")
        self.array[self.count] = item
        self.count += 1
    
    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Índice fora dos limites!")
        return self.array[index]
    
    def remove(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Índice fora dos limites!")
        
        # Desloca todos os elementos após o índice removido
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.count - 1] = None
        self.count -= 1
    
    def __str__(self):
        return str([self.array[i] for i in range(self.count)])

# 3. Matriz estática (bidimensional)
class StaticMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Cria uma matriz rows x cols preenchida com zeros
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def set_value(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Índice fora dos limites da matriz!")
        self.matrix[row][col] = value
    
    def get_value(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Índice fora dos limites da matriz!")
        return self.matrix[row][col]
    
    def print_matrix(self):
        for row in self.matrix:
            print(row)

# Demonstração de uso
def main():
    print("\n=== Demonstração de Alocação Estática ===\n")
    
    # Usando variáveis globais
    print(f"Curso: {COURSE_NAME} | Capacidade: {MAX_STUDENTS} alunos")
    
    # Usando array de tamanho fixo
    print("\n--- Array de tamanho fixo ---")
    students = FixedSizeArray(5)  # Aloca espaço para 5 estudantes
    
    try:
        students.add("Alice")
        students.add("Bob")
        students.add("Charlie")
        print(f"Estudantes atuais: {students}")
        
        students.remove(1)  # Remove Bob
        print(f"Após remover o segundo estudante: {students}")
        
        students.add("David")
        students.add("Eve")
        students.add("Frank")
        print(f"Após adicionar mais estudantes: {students}")
        
        # Tenta adicionar além da capacidade
        students.add("Grace")
    except IndexError as e:
        print(f"Erro: {e}")
    
    # Usando matriz estática
    print("\n--- Matriz Estática ---")
    grades = StaticMatrix(3, 4)  # Matriz 3x4 para notas
    
    # Preenchendo algumas notas
    grades.set_value(0, 0, 85)
    grades.set_value(0, 1, 90)
    grades.set_value(0, 2, 78)
    grades.set_value(0, 3, 92)
    
    grades.set_value(1, 0, 76)
    grades.set_value(1, 1, 88)
    grades.set_value(1, 2, 95)
    grades.set_value(1, 3, 80)
    
    grades.set_value(2, 0, 91)
    grades.set_value(2, 1, 83)
    grades.set_value(2, 2, 89)
    grades.set_value(2, 3, 94)
    
    print("Matriz de notas (3 alunos x 4 avaliações):")
    grades.print_matrix()
    
    try:
        # Tenta acessar fora dos limites
        value = grades.get_value(3, 2)
    except IndexError as e:
        print(f"\nErro: {e}")

if __name__ == "__main__":
    main()
