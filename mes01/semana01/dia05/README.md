 
"""
# 🔧 Sistema de Ordenação Inteligente

Um sistema completo para estudo e comparação de algoritmos de ordenação.

## 🎯 Características

- **4 Algoritmos Implementados:**
  - Bubble Sort (O(n²))
  - Selection Sort (O(n²))
  - Insertion Sort (O(n²) pior caso, O(n) melhor caso)
  - Merge Sort (O(n log n))

- **Funcionalidades:**
  - Comparação de performance
  - Benchmark automático
  - Visualizações gráficas
  - Recomendação inteligente
  - Interface CLI amigável

## 🚀 Como Usar

### Instalação
```bash
git clone <seu-repo>
cd sorting_system
pip install matplotlib  # Para gráficos (opcional)
python main.py
```

### Estrutura do Projeto
```
sorting_system/
├── algorithms/          # Implementações dos algoritmos
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   └── merge_sort.py
├── benchmarking/        # Sistema de testes e visualização
│   ├── performance_test.py
│   └── visualizer.py
├── main.py             # Interface principal
└── README.md
```

## 📊 Complexidades

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso | Espaço |
|-----------|-------------|------------|-----------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

## 🎯 Quando Usar Cada Algoritmo

- **Bubble Sort:** Apenas para fins educacionais
- **Selection Sort:** Quando o custo de escrita é alto
- **Insertion Sort:** Listas pequenas ou quase ordenadas
- **Merge Sort:** Listas grandes ou performance consistente necessária

## 🧪 Exemplos de Uso

```python
from algorithms import merge_sort, insertion_sort

# Para listas pequenas
pequena = [3, 1, 4, 1, 5]
resultado = insertion_sort(pequena.copy())

# Para listas grandes
grande = list(range(1000, 0, -1))
resultado = merge_sort(grande)
```

## 📈 Benchmark

O sistema inclui benchmark automático que testa todos os algoritmos com:
- Dados aleatórios
- Dados ordenados
- Dados em ordem reversa
- Dados quase ordenados

## 🎨 Visualizações

- Gráficos de comparação de tempo
- Tabelas de performance
- Análise de complexidade
- Recomendações automáticas

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua feature branch
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📚 Referências

- [Algorithms, 4th Edition](http://algs4.cs.princeton.edu/)
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)
- [Visualizing Algorithms](https://www.toptal.com/developers/sorting-algorithms)
"""