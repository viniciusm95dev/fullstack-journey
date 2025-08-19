
# Importa o módulo json para manipular arquivos JSON
import json
# Importa o módulo os para verificar existência de arquivos
import os

# Nome do arquivo JSON que armazenará os dados da biblioteca
ARQUIVO_DADOS = 'biblioteca.json'

def carregar_dados():
    """
    Carrega os dados dos livros do arquivo JSON.
    Retorna uma lista vazia se o arquivo não existir ou for inválido.
    """
    # Verifica se o arquivo existe no sistema
    if not os.path.exists(ARQUIVO_DADOS):
        print(f"Arquivo {ARQUIVO_DADOS} não encontrado. Iniciando com biblioteca vazia.")
        # Retorna lista vazia se arquivo não existe
        return []
    
    try:
        # Abre o arquivo em modo leitura com codificação UTF-8
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            # Carrega o conteúdo JSON e retorna como lista Python
            dados = json.load(arquivo)
            print(f"Dados carregados com sucesso! {len(dados)} livros encontrados.")
            return dados
    except json.JSONDecodeError:
        # Captura erro se o JSON estiver malformado
        print(f"Erro: Arquivo {ARQUIVO_DADOS} contém JSON inválido. Iniciando com biblioteca vazia.")
        return []
    except Exception as e:
        # Captura qualquer outro erro de leitura
        print(f"Erro ao carregar dados: {e}")
        return []

def salvar_dados(livros):
    """
    Salva a lista de livros no arquivo JSON.
    Parâmetro: livros (list) - lista de dicionários representando os livros
    """
    try:
        # Abre o arquivo em modo escrita com codificação UTF-8
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
            # Salva os dados em formato JSON com indentação para melhor legibilidade
            # ensure_ascii=False permite caracteres acentuados
            json.dump(livros, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        # Captura e exibe qualquer erro de escrita
        print(f"Erro ao salvar dados: {e}")

def gerar_novo_id(livros):
    """
    Gera um novo ID único para um livro.
    Parâmetro: livros (list) - lista atual de livros
    Retorna: int - próximo ID disponível
    """
    # Se a lista está vazia, retorna 1 como primeiro ID
    if not livros:
        return 1
    
    # Encontra o maior ID existente na lista de livros
    # Usa max() com key para extrair o campo 'id' de cada livro
    maior_id = max(livros, key=lambda livro: livro['id'])['id']
    # Retorna o próximo ID (maior + 1)
    return maior_id + 1

def validar_entrada_numerica(prompt, tipo=int, minimo=0):
    """
    Valida entrada numérica do usuário.
    Parâmetros:
    - prompt (str): mensagem para solicitar entrada
    - tipo (type): tipo de dado esperado (int ou float)
    - minimo: valor mínimo aceito
    Retorna: valor validado no tipo especificado
    """
    while True:
        try:
            # Solicita entrada do usuário
            valor = input(prompt).strip()
            # Converte para o tipo especificado
            valor_convertido = tipo(valor)
            # Verifica se o valor é maior ou igual ao mínimo
            if valor_convertido < minimo:
                print(f"Erro: O valor deve ser maior ou igual a {minimo}.")
                continue
            return valor_convertido
        except ValueError:
            # Captura erro de conversão de tipo
            print(f"Erro: Por favor, digite um valor numérico válido.")

def adicionar_livro(livros):
    """
    Adiciona um novo livro à biblioteca.
    Parâmetro: livros (list) - lista atual de livros (modificada por referência)
    """
    print("\n=== ADICIONAR NOVO LIVRO ===")
    
    # Solicita título do livro (campo obrigatório)
    titulo = input("Digite o título do livro: ").strip()
    # Verifica se o título não está vazio
    if not titulo:
        print("Erro: O título não pode estar vazio.")
        return
    
    # Solicita nome do autor (campo obrigatório)
    autor = input("Digite o nome do autor: ").strip()
    # Verifica se o autor não está vazio
    if not autor:
        print("Erro: O nome do autor não pode estar vazio.")
        return
    
    # Solicita ano de publicação com validação
    ano = validar_entrada_numerica("Digite o ano de publicação: ", int, 0)
    
    # Solicita número total de exemplares
    exemplares = validar_entrada_numerica("Digite o número total de exemplares: ", int, 1)
    
    # Solicita número de exemplares disponíveis
    while True:
        disponiveis = validar_entrada_numerica("Digite o número de exemplares disponíveis: ", int, 0)
        # Valida se disponíveis não é maior que o total
        if disponiveis > exemplares:
            print(f"Erro: Exemplares disponíveis ({disponiveis}) não pode ser maior que o total ({exemplares}).")
        else:
            break
    
    # Gera um novo ID único para o livro
    novo_id = gerar_novo_id(livros)
    
    # Cria um dicionário representando o novo livro
    novo_livro = {
        'id': novo_id,
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'exemplares': exemplares,
        'disponiveis': disponiveis
    }
    
    # Adiciona o novo livro à lista
    livros.append(novo_livro)
    # Salva os dados atualizados no arquivo
    salvar_dados(livros)
    
    print(f"\nLivro adicionado com sucesso! ID: {novo_id}")

def listar_livros(livros):
    """
    Lista todos os livros da biblioteca.
    Parâmetro: livros (list) - lista de livros para exibir
    """
    print("\n=== LISTA DE LIVROS ===")
    
    # Verifica se a biblioteca está vazia
    if not livros:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    # Exibe cabeçalho da tabela
    print(f"{'ID':<5} {'Título':<30} {'Autor':<25} {'Ano':<6} {'Total':<7} {'Disp.':<6}")
    print("-" * 85)  # Linha separadora
    
    # Itera sobre cada livro na lista
    for livro in livros:
        # Formata e exibe os dados de cada livro em colunas alinhadas
        print(f"{livro['id']:<5} "
              f"{livro['titulo'][:29]:<30} "
              f"{livro['autor'][:24]:<25} "
              f"{livro['ano']:<6} "
              f"{livro['exemplares']:<7} "
              f"{livro['disponiveis']:<6}")
    
    print(f"\nTotal de livros cadastrados: {len(livros)}")

def buscar_livro_por_id(livros):
    """
    Busca e exibe um livro específico pelo ID.
    Parâmetro: livros (list) - lista de livros para buscar
    """
    print("\n=== BUSCAR LIVRO POR ID ===")
    
    # Solicita o ID do livro a ser buscado
    id_busca = validar_entrada_numerica("Digite o ID do livro: ", int, 1)
    
    # Procura o livro na lista usando uma função lambda
    livro_encontrado = None
    for livro in livros:
        # Compara o ID do livro atual com o ID buscado
        if livro['id'] == id_busca:
            livro_encontrado = livro
            break  # Para a busca quando encontra o livro
    
    # Verifica se o livro foi encontrado
    if livro_encontrado:
        print("\n=== LIVRO ENCONTRADO ===")
        # Exibe todos os detalhes do livro encontrado
        print(f"ID: {livro_encontrado['id']}")
        print(f"Título: {livro_encontrado['titulo']}")
        print(f"Autor: {livro_encontrado['autor']}")
        print(f"Ano: {livro_encontrado['ano']}")
        print(f"Exemplares totais: {livro_encontrado['exemplares']}")
        print(f"Exemplares disponíveis: {livro_encontrado['disponiveis']}")
        print(f"Exemplares emprestados: {livro_encontrado['exemplares'] - livro_encontrado['disponiveis']}")
    else:
        print(f"Livro com ID {id_busca} não encontrado.")

def atualizar_livro(livros):
    """
    Atualiza os dados de um livro existente.
    Parâmetro: livros (list) - lista de livros (modificada por referência)
    """
    print("\n=== ATUALIZAR LIVRO ===")
    
    # Solicita o ID do livro a ser atualizado
    id_busca = validar_entrada_numerica("Digite o ID do livro a ser atualizado: ", int, 1)
    
    # Procura o livro na lista e guarda sua posição
    indice_livro = -1
    for i, livro in enumerate(livros):
        if livro['id'] == id_busca:
            indice_livro = i
            break
    
    # Verifica se o livro foi encontrado
    if indice_livro == -1:
        print(f"Livro com ID {id_busca} não encontrado.")
        return
    
    # Guarda referência ao livro encontrado
    livro_atual = livros[indice_livro]
    
    print("\n=== DADOS ATUAIS ===")
    print(f"Título: {livro_atual['titulo']}")
    print(f"Autor: {livro_atual['autor']}")
    print(f"Ano: {livro_atual['ano']}")
    print(f"Exemplares totais: {livro_atual['exemplares']}")
    print(f"Exemplares disponíveis: {livro_atual['disponiveis']}")
    
    print("\n=== NOVOS DADOS (pressione Enter para manter o valor atual) ===")
    
    # Atualização do título
    novo_titulo = input(f"Novo título [{livro_atual['titulo']}]: ").strip()
    # Se não digitou nada, mantém o valor atual
    if novo_titulo:
        livro_atual['titulo'] = novo_titulo
    
    # Atualização do autor
    novo_autor = input(f"Novo autor [{livro_atual['autor']}]: ").strip()
    if novo_autor:
        livro_atual['autor'] = novo_autor
    
    # Atualização do ano
    entrada_ano = input(f"Novo ano [{livro_atual['ano']}]: ").strip()
    if entrada_ano:
        try:
            novo_ano = int(entrada_ano)
            if novo_ano >= 0:
                livro_atual['ano'] = novo_ano
            else:
                print("Ano inválido. Mantendo valor atual.")
        except ValueError:
            print("Ano inválido. Mantendo valor atual.")
    
    # Atualização do número de exemplares
    entrada_exemplares = input(f"Novo número de exemplares [{livro_atual['exemplares']}]: ").strip()
    if entrada_exemplares:
        try:
            novos_exemplares = int(entrada_exemplares)
            if novos_exemplares >= 1:
                # Verifica se o novo total não é menor que os disponíveis
                if novos_exemplares >= livro_atual['disponiveis']:
                    livro_atual['exemplares'] = novos_exemplares
                else:
                    print(f"Erro: Total de exemplares não pode ser menor que os disponíveis ({livro_atual['disponiveis']}).")
                    print("Mantendo valor atual.")
            else:
                print("Número de exemplares inválido. Mantendo valor atual.")
        except ValueError:
            print("Número de exemplares inválido. Mantendo valor atual.")
    
    # Atualização dos exemplares disponíveis
    entrada_disponiveis = input(f"Novo número de disponíveis [{livro_atual['disponiveis']}]: ").strip()
    if entrada_disponiveis:
        try:
            novos_disponiveis = int(entrada_disponiveis)
            if 0 <= novos_disponiveis <= livro_atual['exemplares']:
                livro_atual['disponiveis'] = novos_disponiveis
            else:
                print(f"Número de disponíveis deve estar entre 0 e {livro_atual['exemplares']}.")
                print("Mantendo valor atual.")
        except ValueError:
            print("Número de disponíveis inválido. Mantendo valor atual.")
    
    # Salva as alterações no arquivo
    salvar_dados(livros)
    print(f"\nLivro ID {id_busca} atualizado com sucesso!")

def remover_livro(livros):
    """
    Remove um livro da biblioteca.
    Parâmetro: livros (list) - lista de livros (modificada por referência)
    """
    print("\n=== REMOVER LIVRO ===")
    
    # Solicita o ID do livro a ser removido
    id_busca = validar_entrada_numerica("Digite o ID do livro a ser removido: ", int, 1)
    
    # Procura o livro na lista e guarda sua posição
    indice_livro = -1
    for i, livro in enumerate(livros):
        if livro['id'] == id_busca:
            indice_livro = i
            break
    
    # Verifica se o livro foi encontrado
    if indice_livro == -1:
        print(f"Livro com ID {id_busca} não encontrado.")
        return
    
    # Mostra os dados do livro que será removido
    livro_remover = livros[indice_livro]
    print("\n=== LIVRO A SER REMOVIDO ===")
    print(f"ID: {livro_remover['id']}")
    print(f"Título: {livro_remover['titulo']}")
    print(f"Autor: {livro_remover['autor']}")
    
    # Solicita confirmação do usuário
    confirmacao = input("\nDeseja realmente remover este livro? (s/N): ").strip().lower()
    
    # Verifica se o usuário confirmou a remoção
    if confirmacao in ['s', 'sim', 'y', 'yes']:
        # Remove o livro da lista usando pop() com o índice
        livros.pop(indice_livro)
        # Salva as alterações no arquivo
        salvar_dados(livros)
        print(f"Livro removido com sucesso!")
    else:
        print("Operação cancelada.")

def menu():
    """
    Exibe o menu principal e controla o fluxo do programa.
    """
    # Carrega os dados dos livros no início do programa
    livros = carregar_dados()
    
    # Loop principal do programa
    while True:
        # Exibe o menu de opções
        print("\n" + "="*50)
        print("         SISTEMA DE BIBLIOTECA")
        print("="*50)
        print("1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por ID")
        print("4. Atualizar livro")
        print("5. Remover livro")
        print("0. Sair")
        print("-"*50)
        
        # Solicita a opção do usuário
        opcao = input("Escolha uma opção: ").strip()
        
        # Executa a ação correspondente à opção escolhida
        if opcao == '1':
            adicionar_livro(livros)
        elif opcao == '2':
            listar_livros(livros)
        elif opcao == '3':
            buscar_livro_por_id(livros)
        elif opcao == '4':
            atualizar_livro(livros)
        elif opcao == '5':
            remover_livro(livros)
        elif opcao == '0':
            # Opção para sair do programa
            print("\nObrigado por usar o Sistema de Biblioteca!")
            print("Até logo!")
            break  # Sai do loop principal
        else:
            # Opção inválida
            print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 5.")

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Inicia o programa chamando a função menu
    menu()        