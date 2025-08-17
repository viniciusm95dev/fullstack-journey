def bubble_sort_profissional(lista, reverso=False):

    if not lista:
        return []
    
    arr = lista.copy()
    n = len(arr)
    comparacoes = 0
    trocas = 0  

    for i in range(n):
        trocou = False

        for j in range(0, n-i-1):
            comparacoes += 1
            if (arr[j] > arr[j+1] and not reverso) or (arr[j] < arr[j+1] and reverso):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True
                trocas += 1

        if not trocou:
            break

        print(f"Estatísticas: {comparacoes} comparações, {trocas} trocas.")
        return arr
    

                