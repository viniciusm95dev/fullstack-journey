 
import matplotlib.pyplot as plt
import numpy as np

class Visualizador:
    def __init__(self, resultados_benchmark):
        self.resultados = resultados_benchmark
    
    def grafico_comparacao_tempo(self, tipo_dados='random'):
        """Cria gráfico comparando tempos de execução"""
        if tipo_dados not in self.resultados:
            print(f"Tipo de dados '{tipo_dados}' não encontrado.")
            return
        
        dados = self.resultados[tipo_dados]
        tamanhos = list(dados.keys())
        algoritmos = set()
        
        # Descobrir quais algoritmos foram testados
        for tamanho_dados in dados.values():
            algoritmos.update(tamanho_dados.keys())
        
        plt.figure(figsize=(12, 8))
        
        for algoritmo in algoritmos:
            tempos = []
            tamanhos_validos = []
            
            for tamanho in tamanhos:
                if algoritmo in dados[tamanho]:
                    tempos.append(dados[tamanho][algoritmo]['tempo'])
                    tamanhos_validos.append(tamanho)
            
            if tempos:
                plt.plot(tamanhos_validos, tempos, marker='o', label=algoritmo, linewidth=2)
        
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo (segundos)')
        plt.title(f'Comparação de Performance - Dados {tipo_dados.title()}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.yscale('log')  # Escala logarítmica para melhor visualização
        
        plt.tight_layout()
        plt.savefig(f'performance_{tipo_dados}.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def tabela_comparacao(self):
        """Imprime tabela formatada com resultados"""
        print("\n📊 RELATÓRIO DE PERFORMANCE")
        print("=" * 80)
        
        for tipo_dados, dados in self.resultados.items():
            print(f"\n📈 TIPO DE DADOS: {tipo_dados.upper()}")
            print("-" * 40)
            
            # Cabeçalho
            print(f"{'Tamanho':<10}", end="")
            algoritmos = set()
            for tamanho_dados in dados.values():
                algoritmos.update(tamanho_dados.keys())
            
            for algo in sorted(algoritmos):
                print(f"{algo:<15}", end="")
            print()
            
            # Dados
            for tamanho, resultados_tamanho in dados.items():
                print(f"{tamanho:<10}", end="")
                for algo in sorted(algoritmos):
                    if algo in resultados_tamanho:
                        tempo = resultados_tamanho[algo]['tempo']
                        print(f"{tempo:<15.6f}", end="")
                    else:
                        print(f"{'N/A':<15}", end="")
                print()