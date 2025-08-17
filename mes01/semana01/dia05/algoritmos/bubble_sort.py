
def bubble_sort(lista):
    """
    Algoritmo Bubble Sort - O(n²)
    
    Melhor uso: Listas muito pequenas ou para fins educacionais
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        lista: Lista ordenada (modifica original)
    """
    n = len(lista)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        trocou = False
        
        for j in range(0, n - i - 1):
            comparacoes += 1
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                trocas += 1
        
        # Otimização: se não houve trocas, lista já está ordenada
        if not trocou:
            break
    
    return {
        'lista': lista,
        'comparacoes': comparacoes,
        'trocas': trocas,
        'algoritmo': 'Bubble Sort'
    }

