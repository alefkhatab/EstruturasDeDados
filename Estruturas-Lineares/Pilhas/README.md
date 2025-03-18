# Pilhas (Stacks)

## O que são Pilhas?

Pilha é uma estrutura de dados linear que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento a entrar é o primeiro a sair. As pilhas são semelhantes a uma pilha de pratos, onde só podemos adicionar ou remover pratos do topo.

## Características das Pilhas

1. **Princípio LIFO**: O elemento mais recentemente adicionado é o primeiro a ser removido.

2. **Ponto de Acesso Único**: Elementos só podem ser inseridos e removidos pelo topo da pilha.

3. **Operações Principais**: Push (inserir) e Pop (remover).

4. **Estrutura Ordenada**: Mantém os elementos em ordem cronológica de inserção.

## Operações Básicas

### 1. Push (Empilhar)

Adiciona um elemento ao topo da pilha.

**Complexidade**: O(1) - tempo constante

### 2. Pop (Desempilhar)

Remove e retorna o elemento do topo da pilha.

**Complexidade**: O(1) - tempo constante

### 3. Peek/Top

Retorna o elemento do topo da pilha sem removê-lo.

**Complexidade**: O(1) - tempo constante

### 4. IsEmpty

Verifica se a pilha está vazia.

**Complexidade**: O(1) - tempo constante

### 5. Size

Retorna o número de elementos na pilha.

**Complexidade**: O(1) - tempo constante (se mantido um contador)

## Implementações de Pilhas

### 1. Usando Arrays

**Vantagens**:
- Simples e direta
- Acesso rápido ao elemento do topo
- Boa localidade espacial (desempenho de cache)

**Desvantagens**:
- Tamanho fixo (a menos que seja um array dinâmico)
- Pode desperdiçar espaço se subutilizado

### 2. Usando Listas Encadeadas

**Vantagens**:
- Tamanho dinâmico
- Nunca fica cheia (exceto por limitações de memória)
- Implementação simples de push e pop

**Desvantagens**:
- Uso adicional de memória para ponteiros
- Pior localidade espacial

## Aplicações de Pilhas

### 1. Avaliação e Conversão de Expressões

- Conversão de expressões infixa para pós-fixa (notação polonesa reversa)
- Avaliação de expressões pós-fixas
- Verificação de balanceamento de parênteses, colchetes e chaves

### 2. Backtracking

- Resolução de labirintos e quebra-cabeças
- Algoritmos de busca em profundidade (DFS)
- Implementação de algoritmos recursivos de forma iterativa

### 3. Gerenciamento de Memória

- Pilha de chamadas de função (call stack)
- Alocação de memória em tempo de execução
- Compiladores e interpretadores

### 4. Interface de Usuário

- Histórico de ações (para desfazer/refazer)
- Navegação (botão voltar em navegadores)
- Gerenciamento de janelas/diálogos modais

### 5. Algoritmos e Estruturas de Dados

- Implementação de outras estruturas de dados (como filas usando duas pilhas)
- Ordenação (como quicksort)
- Travessia de árvores não recursiva

## Variações de Pilhas

### 1. Pilha com Tamanho Mínimo e Máximo

Uma pilha que mantém registro do menor e maior valor em tempo constante.

### 2. Pilha com Suporte a Min/Max

Uma pilha que permite obter o elemento mínimo ou máximo em tempo constante.

### 3. Pilha Dupla (Double Stack)

Uma implementação que usa um único array para duas pilhas (crescendo de extremidades opostas).

### 4. Pilha Circular

Similar a uma fila circular, mas mantendo comportamento LIFO.

## Considerações de Implementação

### 1. Tratamento de Erros

- **Pilha Vazia**: Operações de pop e peek devem verificar se a pilha está vazia.
- **Pilha Cheia**: Em implementações com tamanho fixo, push deve verificar se a pilha está cheia.

### 2. Escolha da Implementação

- **Arrays**: Melhor para pilhas de tamanho previsível e quando o desempenho é crítico.
- **Listas Encadeadas**: Melhor para pilhas de tamanho imprevisível ou que podem crescer muito.

### 3. Eficiência Espacial vs. Temporal

- Considere o trade-off entre uso de memória e velocidade de operações.
- Em alguns casos, pode ser apropriado implementar redimensionamento dinâmico para arrays.

## Exemplos de Casos de Uso

### 1. Verificação de Sintaxe

Verificação de sintaxe em linguagens de programação (como correspondência de chaves, parênteses e colchetes).

```python
def verify_brackets(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0
```

### 2. Conversão de Notação Infixa para Pós-fixa

Conversão de expressões matemáticas da forma infixa (usual) para pós-fixa (notação polonesa reversa).

```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    
    for token in expression.split():
        if token in precedence:
            while (stack and stack[-1] != '(' and 
                  precedence.get(stack[-1], 0) >= precedence[token]):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        else:  # Operando
            postfix.append(token)
    
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)
```

## Conclusão

Pilhas são estruturas de dados fundamentais com um princípio simples mas poderoso. Seu comportamento LIFO as torna ideais para problemas que envolvem rastreamento de histórico, avaliação de expressões e implementação de algoritmos recursivos de forma iterativa. A escolha entre implementações baseadas em arrays ou listas encadeadas depende das necessidades específicas da aplicação, considerando fatores como flexibilidade de tamanho, eficiência de memória e desempenho.

Autores: Alef Khatab 
