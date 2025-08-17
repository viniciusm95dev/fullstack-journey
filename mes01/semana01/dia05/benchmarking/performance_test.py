 
import time
import random
from algoritmos import bubble_sort, selection_sort, insertion_sort, merge_sort

class PerformanceTest:
    def __init__(self):
        self.algoritmos = {
            'Bubble Sort': bubble_sort,
            'Selection Sort': selection_sort,
            'Insertion Sort': insertion_sort,
            'Merge Sort': merge_sort
        }
    
    def gerar_dados_teste(self, tamanho, tipo='random'):
        """Gera diferentes tipos de dados para teste"""
        if tipo == 'random':
            return [random.randint(1, 1000) for _ in range(tamanho)]
        elif tipo == 'ordenado':
            return list(range(1, tamanho + 1))
        elif tipo == 'reverso':
            return list(range(tamanho, 0, -1))
        elif tipo == 'quase_ordenado':
            lista = list(range(1, tamanho + 1))
            # Trocar 10% dos elementos aleatoriamente
            for _ in range(tamanho // 10):
                i, j = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
                lista[i], lista[j] = lista[j], lista[i]
            return lista
    
    def executar_teste(self, algoritmo_nome, lista):
        """Executa um teste e mede performance"""
        algoritmo = self.algoritmos[algoritmo_nome]
        lista_copia = lista.copy()
        
        inicio = time.time()
        resultado = algoritmo(lista_copia)
        fim = time.time()
        
        return {
            'tempo': fim - inicio,
            'estatisticas': resultado,
            'tamanho': len(lista)
        }
    
    def benchmark_completo(self, tamanhos=[10, 50, 100, 500], tipos=['random']):
        """Executa benchmark completo"""
        resultados = {}
        
        for tipo in tipos:
            resultados[tipo] = {}
            print(f"\n🧪 TESTANDO COM DADOS: {tipo.upper()}")
            print("=" * 50)
            
            for tamanho in tamanhos:
                dados = self.gerar_dados_teste(tamanho, tipo)
                resultados[tipo][tamanho] = {}
                
                print(f"\n📊 Tamanho: {tamanho} elementos")
                
                for nome_algo in self.algoritmos:
                    # Pular bubble sort para listas muito grandes
                    if nome_algo == 'Bubble Sort' and tamanho > 1000:
                        continue
                    
                    teste = self.executar_teste(nome_algo, dados)
                    resultados[tipo][tamanho][nome_algo] = teste
                    
                    print(f"  {nome_algo:15} - {teste['tempo']:.6f}s")
        
        return resultados
    
    def recomendar_algoritmo(self, tamanho, tipo_dados='random'):
        """Recomenda o melhor algoritmo baseado no contexto"""
        if tamanho <= 10:
            return "Insertion Sort - Eficiente para listas pequenas"
        elif tamanho <= 50 and tipo_dados == 'quase_ordenado':
            return "Insertion Sort - Ótimo para dados quase ordenados"
        elif tamanho <= 100:
            return "Selection Sort - Bom equilíbrio para tamanho médio"
        else:
            return "Merge Sort - Melhor performance para listas grandes"