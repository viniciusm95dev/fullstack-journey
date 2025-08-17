 
import sys
from algoritmos import bubble_sort, selection_sort, insertion_sort, merge_sort
from benchmarking.performance_test import PerformanceTest
from benchmarking.visualizer import Visualizador

class SistemaOrdenacao:
    def __init__(self):
        self.algoritmos = {
            '1': ('Bubble Sort', bubble_sort),
            '2': ('Selection Sort', selection_sort),
            '3': ('Insertion Sort', insertion_sort),
            '4': ('Merge Sort', merge_sort)
        }
        self.teste_performance = PerformanceTest()
    
    def mostrar_menu(self):
        print("\n🔧 SISTEMA DE ORDENAÇÃO INTELIGENTE")
        print("=" * 40)
        print("1. Bubble Sort")
        print("2. Selection Sort") 
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Comparar Algoritmos")
        print("6. Benchmark Completo")
        print("7. Recomendação Automática")
        print("0. Sair")
        print("-" * 40)
    
    def obter_lista_usuario(self):
        """Obtém lista de números do usuário"""
        print("\nEscolha uma opção:")
        print("1. Digitar números manualmente")
        print("2. Gerar lista aleatória")
        
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            entrada = input("Digite números separados por espaço: ")
            try:
                return [int(x) for x in entrada.split()]
            except ValueError:
                print("❌ Erro: Digite apenas números válidos!")
                return []
        
        elif opcao == '2':
            try:
                tamanho = int(input("Tamanho da lista (max 1000): "))
                tamanho = min(tamanho, 1000)
                return self.teste_performance.gerar_dados_teste(tamanho, 'random')
            except ValueError:
                print("❌ Erro: Digite um número válido!")
                return []
        
        return []
    
    def executar_algoritmo(self, opcao):
        """Executa algoritmo específico"""
        if opcao not in self.algoritmos:
            print("❌ Opção inválida!")
            return
        
        nome, algoritmo = self.algoritmos[opcao]
        lista = self.obter_lista_usuario()
        
        if not lista:
            return
        
        print(f"\n📝 Lista original: {lista}")
        
        import time
        inicio = time.time()
        resultado = algoritmo(lista.copy())
        fim = time.time()
        
        print(f"\n✅ Resultado do {nome}:")
        print(f"   Lista ordenada: {resultado['lista']}")
        print(f"   Tempo: {fim - inicio:.6f} segundos")
        
        if 'comparacoes' in resultado:
            print(f"   Comparações: {resultado['comparacoes']}")
        if 'trocas' in resultado:
            print(f"   Trocas: {resultado['trocas']}")
        if 'movimentos' in resultado:
            print(f"   Movimentos: {resultado['movimentos']}")
    
    def comparar_algoritmos(self):
        """Compara todos os algoritmos com a mesma lista"""
        lista = self.obter_lista_usuario()
        
        if not lista:
            return
        
        print(f"\n📊 COMPARAÇÃO DE ALGORITMOS")
        print(f"Lista original: {lista}")
        print("=" * 60)
        
        resultados = []
        
        for opcao, (nome, algoritmo) in self.algoritmos.items():
            # Pular bubble sort para listas muito grandes
            if nome == 'Bubble Sort' and len(lista) > 1000:
                continue
            
            import time
            lista_copia = lista.copy()
            
            inicio = time.time()
            resultado = algoritmo(lista_copia)
            fim = time.time()
            
            tempo = fim - inicio
            resultados.append((nome, tempo, resultado))
            
            print(f"{nome:15} - {tempo:.6f}s")
        
        # Mostrar o mais eficiente
        if resultados:
            melhor = min(resultados, key=lambda x: x[1])
            print(f"\n🏆 Mais eficiente: {melhor[0]} ({melhor[1]:.6f}s)")
    
    def benchmark_completo(self):
        """Executa benchmark completo"""
        print("\n⚡ EXECUTANDO BENCHMARK COMPLETO...")
        print("Isso pode levar alguns segundos...\n")
        
        tamanhos = [10, 50, 100, 500]
        tipos = ['random', 'ordenado', 'reverso', 'quase_ordenado']
        
        resultados = self.teste_performance.benchmark_completo(tamanhos, tipos)
        
        # Mostrar visualizações
        visualizador = Visualizador(resultados)
        visualizador.tabela_comparacao()
        
        # Opcional: gráficos (requer matplotlib)
        try:
            visualizador.grafico_comparacao_tempo('random')
        except ImportError:
            print("\n💡 Instale matplotlib para ver gráficos: pip install matplotlib")
    
    def recomendacao_automatica(self):
        """Recomenda algoritmo baseado no contexto"""
        try:
            tamanho = int(input("Tamanho da lista: "))
            
            print("\nTipo de dados:")
            print("1. Aleatórios")
            print("2. Quase ordenados")
            print("3. Totalmente desordenados")
            
            tipo_opcao = input("Opção (1-3): ").strip()
            tipos = {'1': 'random', '2': 'quase_ordenado', '3': 'random'}
            tipo = tipos.get(tipo_opcao, 'random')
            
            recomendacao = self.teste_performance.recomendar_algoritmo(tamanho, tipo)
            print(f"\n💡 RECOMENDAÇÃO: {recomendacao}")
            
        except ValueError:
            print("❌ Digite um número válido!")
    
    def executar(self):
        """Loop principal do programa"""
        print("🚀 Bem-vindo ao Sistema de Ordenação Inteligente!")
        
        while True:
            self.mostrar_menu()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '0':
                print("👋 Até mais!")
                break
            elif opcao in ['1', '2', '3', '4']:
                self.executar_algoritmo(opcao)
            elif opcao == '5':
                self.comparar_algoritmos()
            elif opcao == '6':
                self.benchmark_completo()
            elif opcao == '7':
                self.recomendacao_automatica()
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    sistema = SistemaOrdenacao()
    sistema.executar()