# EstruturasDeDados

Repositório para estudo de listas encadeadas, listas ordenadas e árvores binárias em Python.

## Problema Prático Escolhido: Sistema de Gerenciamento de Processos

### Descrição do Problema

O problema escolhido é a implementação de um sistema simplificado de gerenciamento de processos em um sistema operacional, similar ao que os sistemas operacionais modernos utilizam. Neste sistema, cada processo tem um ID único, um nome, uma prioridade e um estado (novo, pronto, executando, bloqueado, terminado).

O sistema precisa:
1. Gerenciar processos em diferentes estados
2. Permitir a criação, execução, bloqueio e terminação de processos
3. Implementar um escalonador que selecione processos baseado em diferentes critérios

### Estrutura de Dados Escolhida

Para este problema, escolhemos utilizar **Filas** como a principal estrutura de dados. Mais especificamente, utilizaremos:

- **Fila de Prioridade**: Para gerenciar processos prontos, onde os processos com maior prioridade serão executados primeiro
- **Fila Regular (FIFO)**: Para gerenciar processos bloqueados, que serão desbloqueados na ordem em que foram bloqueados

### Justificativa da Escolha

As filas são ideais para este problema porque:

1. **Fila de Prioridade para Processos Prontos**:
   - Permite selecionar rapidamente o processo de maior prioridade para execução
   - Operações de inserção e remoção eficientes
   - Modela naturalmente o comportamento de um escalonador baseado em prioridade

2. **Fila Regular para Processos Bloqueados**:
   - Segue o princípio FIFO (First In, First Out), que é adequado para desbloquear processos na ordem em que foram bloqueados
   - Simples de implementar e entender
   - Garante que processos não fiquem bloqueados indefinidamente (starvation)

### Implementação

A implementação deste sistema de gerenciamento de processos está no arquivo `solucao_problema_pratico.py` na raiz deste repositório. O código implementa as classes necessárias e demonstra o funcionamento do sistema com um exemplo que cria processos, os executa e simula diferentes transições de estado.

### Organização do Repositório

Este repositório está organizado da seguinte forma:

1. **Introdução**: Conceitos básicos sobre estruturas de dados e exemplos de aplicação no mundo real
2. **Definição-Importância**: Explicação sobre o impacto das estruturas de dados no desempenho de programas
3. **Conceitos-Fundamentais**: Detalhes sobre variáveis, tipos de dados e alocação de memória (estática e dinâmica)
4. **Estruturas-Lineares**: Implementações e explicações sobre listas, filas e pilhas
5. **Raiz**: Solução do problema prático utilizando filas

Cada diretório contém arquivos README.md explicativos e implementações práticas em Python para demonstrar os conceitos abordados.

## Autores

- Alef Khatab
- Kaynã Barbosa de Miranda

## Disciplina

Estrutura de Dados I