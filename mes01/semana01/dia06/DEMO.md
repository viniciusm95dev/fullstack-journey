# DEMO - Casos de Teste Manuais

Este documento contém 5 casos de teste manuais para validar as funcionalidades principais da calculadora científica.

## 🧪 Casos de Teste

### Caso 1: Operações Básicas e Precedência
**Expressão:** `3 + 4 × 2 ÷ (1 - 5)^2`

**Passos para reproduzir:**
1. Abra a calculadora
2. Digite: `3`, `+`, `4`, `×`, `2`, `÷`, `(`, `1`, `-`, `5`, `)`, `^`, `2`
3. Pressione `=` ou Enter

**Resultado esperado:** `5`

**Cálculo detalhado:**
- `(1 - 5) = -4`
- `(-4)^2 = 16`
- `4 × 2 = 8`
- `8 ÷ 16 = 0.5`
- `3 + 0.5 = 3.5`

---

### Caso 2: Raiz Quadrada Simples
**Expressão:** `√16`

**Passos para reproduzir:**
1. Clique no botão `√` (modo científico deve estar ativo)
2. Digite: `16`
3. Digite: `)`
4. Pressione `=`

**Resultado esperado:** `4`

---

### Caso 3: Expressão Complexa com Potências Aninhadas
**Expressão:** `3+4*2/(1-5)^2^3`

**Passos para reproduzir:**
1. Digite: `3`, `+`, `4`, `*`, `2`, `/`, `(`, `1`, `-`, `5`, `)`, `^`, `2`, `^`, `3`
2. Pressione `=`

**Resultado esperado:** `3.001953125`

**Cálculo detalhado:**
- `(1-5) = -4`
- `(-4)^2 = 16`
- `16^3 = 4096`
- `4*2 = 8`
- `8/4096 = 0.001953125`
- `3 + 0.001953125 = 3.001953125`

---

### Caso 4: Funções Trigonométricas com Constantes
**Expressão:** `sin(π/2) + cos(0)`

**Passos para reproduzir:**
1. Ative o modo científico (se não estiver)
2. Clique em `sin`
3. Clique em `π`
4. Digite: `/`, `2`, `)`
5. Digite: `+`
6. Clique em `cos`
7. Digite: `0`, `)`
8. Pressione `=`

**Resultado esperado:** `2` (aproximadamente, pode haver pequenos erros de ponto flutuante)

**Cálculo detalhado:**
- `π/2 ≈ 1.5708`
- `sin(π/2) = 1`
- `cos(0) = 1`
- `1 + 1 = 2`

---

### Caso 5: Teste de Memória e Logaritmo
**Expressão:** Sequência de operações com memória

**Passos para reproduzir:**
1. Digite: `log`, `(`, `1000`, `)` → Pressione `=`
   - **Resultado esperado:** `3`
2. Clique em `M+` (adicionar à memória)
3. Digite: `5`, `!` (fatorial de 5)
   - **Resultado esperado:** `120`
4. Clique em `M+` (adicionar à memória: 3 + 120 = 123)
5. Clique em `C` (limpar display)
6. Clique em `MR` (recuperar da memória)
   - **Resultado esperado:** `123`

---

## 🎯 Instruções para Reproduzir os Testes

### Pré-requisitos
1. Calculadora executando localmente (`npm run dev`)
2. Navegador moderno aberto na URL da aplicação

### Método de Teste
1. **Teste via Interface (Cliques):**
   - Use o mouse para clicar nos botões
   - Observe o display atualizar em tempo real
   - Verifique se a expressão aparece corretamente

2. **Teste via Teclado:**
   - Digite os números e operadores no teclado
   - Use `Enter` para calcular
   - Use `Esc` para limpar
   - Use `Backspace` para apagar

### Validação dos Resultados

#### ✅ **Resultado Correto:**
- Display mostra o valor esperado
- Expressão é adicionada ao histórico
- Não há mensagens de erro

#### ❌ **Resultado Incorreto:**
- Display mostra "Erro"
- Resultado difere do esperado por mais de 0.001
- Aplicação trava ou não responde

### Testes de Funcionalidades Extras

#### Teste de Histórico:
1. Execute qualquer cálculo dos casos acima
2. Clique no ícone de histórico (📊)
3. Verifique se o cálculo aparece na lista
4. Clique em um item do histórico
5. Verifique se o resultado é carregado no display

#### Teste de Exportação:
1. Execute alguns cálculos
2. Abra o histórico
3. Clique no ícone de download (⬇️)
4. Verifique se o arquivo .txt é baixado
5. Abra o arquivo e verifique o conteúdo

#### Teste de Tema:
1. Clique no ícone de sol/lua (☀️/🌙)
2. Verifique se o tema alterna entre claro e escuro
3. Verifique se a mudança é aplicada em todos os elementos

#### Teste de Responsividade:
1. Redimensione a janela do navegador
2. Verifique se o layout se adapta corretamente
3. Teste em diferentes tamanhos de tela
4. Verifique se todos os botões permanecem acessíveis

### Casos Extremos para Testar

#### Números Muito Grandes:
- `999999999999999999999`
- Resultado deve aparecer em notação científica

#### Divisão por Zero:
- `5 ÷ 0`
- Resultado deve mostrar `Infinity` ou tratar apropriadamente

#### Expressões Inválidas:
- `2++3` ou `sin(` (sem fechar parênteses)
- Resultado deve mostrar "Erro"

#### Memória com Valores Extremos:
- Adicione um número muito grande à memória
- Verifique se `MR` recupera corretamente

## 📊 Critérios de Aceitação

Para cada caso de teste, verifique:

- [ ] **Funcionalidade:** O resultado está correto?
- [ ] **Interface:** O display atualiza corretamente?
- [ ] **Responsividade:** Funciona em diferentes tamanhos de tela?
- [ ] **Acessibilidade:** Funciona apenas com teclado?
- [ ] **Performance:** A calculadora responde rapidamente?
- [ ] **Erro Handling:** Expressões inválidas são tratadas adequadamente?

## 🐛 Relato de Bugs

Se algum teste falhar, documente:

1. **Caso de teste:** Qual teste falhou?
2. **Passos realizados:** O que você fez exatamente?
3. **Resultado obtido:** O que aconteceu?
4. **Resultado esperado:** O que deveria ter acontecido?
5. **Ambiente:** Navegador, versão, sistema operacional
6. **Screenshots:** Se aplicável

## 🎉 Testes Avançados (Opcional)

### Teste de Stress:
1. Execute 50+ cálculos consecutivos
2. Verifique se o histórico comporta adequadamente
3. Verifique se a performance se mantém estável

### Teste de Compatibilidade:
1. Teste em diferentes navegadores (Chrome, Firefox, Safari, Edge)
2. Teste em dispositivos móveis (iOS, Android)
3. Teste com diferentes resoluções de tela

### Teste de Acessibilidade:
1. Navegue apenas com Tab e Enter
2. Teste com screen reader (se disponível)
3. Verifique contraste de cores
4. Verifique se todos os elementos têm labels apropriados

---

**💡 Dica:** Execute estes testes sempre após mudanças no código para garantir que não houve regressões!