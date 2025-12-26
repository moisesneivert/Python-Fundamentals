"""
Agenda de Contatos - Aplicação em Terminal

Este projeto demonstra fundamentos de Python:
- Estruturas de dados (listas e dicionários)
- Funções
- Controle de fluxo
- Boas práticas de legibilidade
"""

# Lista global que armazena os contatos
contatos = []


def mostrar_menu() -> None:
    """
    Exibe o menu principal de opções para o usuário.
    """
    print("\n=== AGENDA DE CONTATOS ===")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")


def criar_contato(nome: str, telefone: str, email: str, favorito: bool) -> dict:
    """
    Cria e retorna um dicionário representando um contato.
    """
    return {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }


def adicionar_contato() -> None:
    """
    Solicita os dados ao usuário e adiciona um novo contato à lista.
    """
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    favorito_input = input("Marcar como favorito? (s/n): ").lower()
    favorito = favorito_input == "s"

    contato = criar_contato(nome, telefone, email, favorito)
    contatos.append(contato)

    print("Contato adicionado com sucesso.")


def listar_contatos(lista_contatos: list) -> None:
    """
    Exibe uma lista de contatos no terminal.
    """
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
        return

    for indice, contato in enumerate(lista_contatos, start=1):
        favorito = "⭐" if contato["favorito"] else ""
        print(
            f"{indice}. {contato['nome']} {favorito} | "
            f"Telefone: {contato['telefone']} | "
            f"Email: {contato['email']}"
        )


def visualizar_contatos() -> None:
    """
    Exibe todos os contatos cadastrados.
    """
    print("\n--- Lista de Contatos ---")
    listar_contatos(contatos)


def encontrar_contato_por_nome(nome: str) -> dict | None:
    """
    Busca um contato pelo nome.
    Retorna o contato se encontrado ou None caso contrário.
    """
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            return contato
    return None


def editar_contato() -> None:
    """
    Permite editar os dados de um contato existente.
    """
    nome_busca = input("Digite o nome do contato a editar: ")
    contato = encontrar_contato_por_nome(nome_busca)

    if not contato:
        print("Contato não encontrado.")
        return

    contato["nome"] = input("Novo nome: ").strip()
    contato["telefone"] = input("Novo telefone: ").strip()
    contato["email"] = input("Novo email: ").strip()

    print("Contato atualizado com sucesso.")


def alternar_favorito() -> None:
    """
    Marca ou desmarca um contato como favorito.
    """
    nome_busca = input("Digite o nome do contato: ")
    contato = encontrar_contato_por_nome(nome_busca)

    if not contato:
        print("Contato não encontrado.")
        return

    contato["favorito"] = not contato["favorito"]
    status = "favorito" if contato["favorito"] else "não favorito"

    print(f"Contato agora está marcado como {status}.")


def ver_contatos_favoritos() -> None:
    """
    Exibe apenas os contatos marcados como favoritos.
    """
    favoritos = [c for c in contatos if c["favorito"]]

    print("\n--- Contatos Favoritos ---")
    listar_contatos(favoritos)


def apagar_contato() -> None:
    """
    Remove um contato da agenda.
    """
    nome_busca = input("Digite o nome do contato a apagar: ")
    contato = encontrar_contato_por_nome(nome_busca)

    if not contato:
        print("Contato não encontrado.")
        return

    contatos.remove(contato)
    print("Contato removido com sucesso.")


def executar_aplicacao() -> None:
    """
    Função principal que controla o fluxo da aplicação.
    """
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            visualizar_contatos()
        elif opcao == "3":
            editar_contato()
        elif opcao == "4":
            alternar_favorito()
        elif opcao == "5":
            ver_contatos_favoritos()
        elif opcao == "6":
            apagar_contato()
        elif opcao == "7":
            print("Encerrando aplicação.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada da aplicação
if __name__ == "__main__":
    executar_aplicacao()
