 
def insertion_sort(lista):
    """
    Algoritmo Insertion Sort - O(n²) pior caso, O(n) melhor caso
    
    Melhor uso: Listas pequenas ou quase ordenadas
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        dict: Lista ordenada + estatísticas
    """
    comparacoes = 0
    movimentos = 0
    
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        
        # Mover elementos maiores que key para a direita
        while j >= 0:
            comparacoes += 1
            if lista[j] > key:
                lista[j + 1] = lista[j]
                movimentos += 1
                j -= 1
            else:
                break
        
        # Inserir key na posição correta
        lista[j + 1] = key
        if j + 1 != i:
            movimentos += 1
    
    return {
        'lista': lista,
        'comparacoes': comparacoes,
        'movimentos': movimentos,
        'algoritmo': 'Insertion Sort'
    }

