 
def merge_sort(lista):
    """
    Algoritmo Merge Sort - O(n log n)
    
    Melhor uso: Listas grandes ou quando performance consistente é necessária
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        dict: Lista ordenada + estatísticas
    """
    stats = {'comparacoes': 0, 'operacoes': 0}
    
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        # Dividir
        meio = len(arr) // 2
        esquerda = merge_sort_recursive(arr[:meio])
        direita = merge_sort_recursive(arr[meio:])
        
        # Conquistar (merge)
        return merge(esquerda, direita)
    
    def merge(esquerda, direita):
        resultado = []
        i = j = 0
        
        # Comparar e mergir
        while i < len(esquerda) and j < len(direita):
            stats['comparacoes'] += 1
            stats['operacoes'] += 1
            
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        # Adicionar elementos restantes
        while i < len(esquerda):
            resultado.append(esquerda[i])
            stats['operacoes'] += 1
            i += 1
        
        while j < len(direita):
            resultado.append(direita[j])
            stats['operacoes'] += 1
            j += 1
        
        return resultado
    
    lista_ordenada = merge_sort_recursive(lista.copy())
    
    return {
        'lista': lista_ordenada,
        'comparacoes': stats['comparacoes'],
        'operacoes': stats['operacoes'],
        'algoritmo': 'Merge Sort'
    }