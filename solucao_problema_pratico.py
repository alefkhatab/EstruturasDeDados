'''
Sistema de Gerenciamento de Processos

Este arquivo implementa um sistema simplificado de gerenciamento de processos,
similar ao utilizado em sistemas operacionais. Demonstra a aplicação prática de
filas e filas de prioridade como estruturas de dados para gerenciamento eficiente.

Autores: Alef Khatab e Kaynã Barbosa de Miranda
'''

import heapq
from enum import Enum
import time

# Definição dos estados de um processo
class ProcessState(Enum):
    NEW = "Novo"
    READY = "Pronto"
    RUNNING = "Executando"
    BLOCKED = "Bloqueado"
    TERMINATED = "Terminado"

# Classe que representa um processo
class Process:
    next_pid = 1  # ID do próximo processo a ser criado
    
    def __init__(self, name, priority=0):
        self.pid = Process.next_pid  # ID único do processo
        Process.next_pid += 1
        self.name = name  # Nome do processo
        self.priority = priority  # Prioridade (maior número = maior prioridade)
        self.state = ProcessState.NEW  # Estado inicial: NEW
        self.creation_time = time.time()  # Momento de criação
        self.execution_time = 0  # Tempo total de execução
        self.block_reason = None  # Razão do bloqueio (se estiver bloqueado)
    
    def __lt__(self, other):
        # Define a ordenação para a fila de prioridade (maior prioridade vem primeiro)
        return self.priority > other.priority
    
    def __repr__(self):
        return f"Processo[{self.pid}, {self.name}, Prioridade={self.priority}, Estado={self.state.value}]"

# Gerenciador de processos usando filas
class ProcessManager:
    def __init__(self):
        self.all_processes = {}  # Dicionário de todos os processos por PID
        self.ready_queue = []  # Fila de prioridade para processos prontos
        self.blocked_queue = []  # Fila FIFO para processos bloqueados
        self.running_process = None  # Processo atualmente em execução
    
    def create_process(self, name, priority=0):
        '''
        Cria um novo processo e o coloca na fila de processos prontos.
        '''
        process = Process(name, priority)
        self.all_processes[process.pid] = process
        print(f"Processo criado: {process}")
        self.set_process_ready(process)
        return process
    
    def set_process_ready(self, process):
        '''
        Define o estado de um processo como READY e o adiciona à fila de prontos.
        '''
        process.state = ProcessState.READY
        print(f"Processo {process.pid} está pronto para execução.")
        # Adiciona à fila de prioridade
        heapq.heappush(self.ready_queue, process)
    
    def schedule_next_process(self):
        '''
        Seleciona o próximo processo a ser executado da fila de prontos.
        Retorna o processo selecionado ou None se a fila estiver vazia.
        '''
        if not self.ready_queue:
            print("Nenhum processo pronto para execução.")
            return None
        
        # Remove e retorna o processo de maior prioridade
        process = heapq.heappop(self.ready_queue)
        self.running_process = process
        process.state = ProcessState.RUNNING
        print(f"Processo {process.pid} ({process.name}) iniciou execução.")
        return process
    
    def block_process(self, pid, reason="I/O Operation"):
        '''
        Bloqueia um processo em execução e o move para a fila de bloqueados.
        '''
        if self.running_process and self.running_process.pid == pid:
            process = self.running_process
            process.state = ProcessState.BLOCKED
            process.block_reason = reason
            self.blocked_queue.append(process)  # Adiciona à fila FIFO de bloqueados
            print(f"Processo {process.pid} bloqueado: {reason}")
            self.running_process = None
            return True
        else:
            print(f"Erro: Não há processo com PID {pid} em execução.")
            return False
    
    def unblock_process(self):
        '''
        Desbloqueia o processo que está há mais tempo na fila de bloqueados (FIFO).
        '''
        if not self.blocked_queue:
            print("Nenhum processo bloqueado.")
            return None
        
        # Remove o primeiro processo da fila de bloqueados (FIFO)
        process = self.blocked_queue.pop(0)
        print(f"Processo {process.pid} desbloqueado.")
        self.set_process_ready(process)
        return process
    
    def terminate_process(self, pid=None):
        '''
        Termina um processo. Se pid for None, termina o processo em execução.
        '''
        process = None
        
        if pid is None and self.running_process:
            # Termina o processo em execução
            process = self.running_process
            self.running_process = None
        elif pid in self.all_processes:
            # Termina o processo específico
            process = self.all_processes[pid]
            
            # Se o processo estiver executando, limpa a referência
            if self.running_process and self.running_process.pid == pid:
                self.running_process = None
            
            # Remove o processo da fila de prontos, se estiver nela
            self.ready_queue = [p for p in self.ready_queue if p.pid != pid]
            heapq.heapify(self.ready_queue)
            
            # Remove o processo da fila de bloqueados, se estiver nela
            self.blocked_queue = [p for p in self.blocked_queue if p.pid != pid]
        
        if process:
            process.state = ProcessState.TERMINATED
            print(f"Processo {process.pid} ({process.name}) terminado.")
            return True
        else:
            print(f"Erro: Processo com PID {pid} não encontrado.")
            return False
    
    def get_process_info(self, pid):
        '''
        Retorna informações sobre um processo específico.
        '''
        if pid in self.all_processes:
            return self.all_processes[pid]
        return None
    
    def list_all_processes(self):
        '''
        Lista todos os processos registrados no sistema.
        '''
        for pid, process in self.all_processes.items():
            print(f"PID: {pid}, Nome: {process.name}, Estado: {process.state.value}, Prioridade: {process.priority}")
    
    def list_ready_processes(self):
        '''
        Lista todos os processos na fila de prontos.
        '''
        if not self.ready_queue:
            print("Fila de processos prontos vazia.")
            return
        
        # Cria uma cópia da fila para não afetar a original
        ready_copy = self.ready_queue.copy()
        print("Processos prontos (ordenados por prioridade):")
        while ready_copy:
            process = heapq.heappop(ready_copy)
            print(f"  PID: {process.pid}, Nome: {process.name}, Prioridade: {process.priority}")
    
    def list_blocked_processes(self):
        '''
        Lista todos os processos na fila de bloqueados.
        '''
        if not self.blocked_queue:
            print("Fila de processos bloqueados vazia.")
            return
        
        print("Processos bloqueados (ordenados por tempo de bloqueio):")
        for i, process in enumerate(self.blocked_queue):
            print(f"  {i+1}. PID: {process.pid}, Nome: {process.name}, Razão: {process.block_reason}")

# Demonstração do uso do sistema de gerenciamento de processos
def main():
    print("\n=== Sistema de Gerenciamento de Processos ===\n")
    
    # Criar o gerenciador de processos
    process_manager = ProcessManager()
    
    # Criar alguns processos com diferentes prioridades
    print("--- Criando processos ---")
    process_manager.create_process("Editor de Texto", priority=2)
    process_manager.create_process("Navegador Web", priority=3)
    process_manager.create_process("Reprodutor de Música", priority=1)
    process_manager.create_process("Antivírus", priority=5)
    process_manager.create_process("Gerenciador de Downloads", priority=2)
    print()
    
    # Listar processos prontos
    process_manager.list_ready_processes()
    print()
    
    # Executar o próximo processo (deve ser o Antivírus, devido à prioridade mais alta)
    print("--- Escalonando o próximo processo ---")
    next_process = process_manager.schedule_next_process()
    print()
    
    # Bloquear o processo em execução
    print("--- Bloqueando o processo em execução ---")
    process_manager.block_process(next_process.pid, "Aguardando atualização de definições")
    print()
    
    # Listar processos bloqueados
    process_manager.list_blocked_processes()
    print()
    
    # Executar o próximo processo (deve ser o Navegador Web, devido à próxima prioridade mais alta)
    print("--- Escalonando o próximo processo ---")
    next_process = process_manager.schedule_next_process()
    print()
    
    # Terminar o processo em execução
    print("--- Terminando o processo em execução ---")
    process_manager.terminate_process()
    print()
    
    # Desbloquear um processo
    print("--- Desbloqueando processo ---")
    process_manager.unblock_process()
    print()
    
    # Listar processos prontos novamente
    process_manager.list_ready_processes()
    print()
    
    # Listar todos os processos e seus estados
    print("--- Estado de todos os processos ---")
    process_manager.list_all_processes()
    print()
    
    # Executar mais alguns processos
    print("--- Executando ciclo de processos restantes ---")
    while process_manager.ready_queue:
        process = process_manager.schedule_next_process()
        print(f"Processo {process.pid} executando...")
        # Simular término natural dos processos
        process_manager.terminate_process()
    
    print("\nTodos os processos foram executados e terminados.")

if __name__ == "__main__":
    main()