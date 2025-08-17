 
def selection_sort(lista):
    """
    Algoritmo Selection Sort - O(n²)
    
    Melhor uso: Quando o custo de escrita é caro (poucos swaps)
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        dict: Lista ordenada + estatísticas
    """
    n = len(lista)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        min_idx = i
        
        # Encontrar o menor elemento no resto da lista
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        # Trocar apenas se necessário
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            trocas += 1
    
    return {
        'lista': lista,
        'comparacoes': comparacoes,
        'trocas': trocas,
        'algoritmo': 'Selection Sort'
    }