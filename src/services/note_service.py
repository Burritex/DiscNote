"""
    note_service.py
    ---------------
    Contém a lógica de criação de objetos ``Note`` a partir de diferentes origens.
    
    Responsabilidade:
        Abstrair como uma nota é obtida (console, arquivo, futuramente API),
        validando a entrada e retornando um objeto ``Note`` pronto para uso.
    
    Origens suportadas:
        - ``from_console``: lê a nota digitada pelo usuário no terminal.
        - ``from_file``   : (não implementado) lê a nota a partir de um arquivo.
"""

from models import Note


class NoteService:
    """
        Serviço responsável por criar instâncias de ``Note`` a partir de entradas do usuário.
    
        Todos os métodos são estáticos — a classe não precisa ser instanciada.
    """

    @staticmethod
    def from_console() -> Note:
        """
            Lê uma nota digitada pelo usuário no terminal e retorna um objeto ``Note``.
    
            O texto é normalizado (strip + capitalize) e validado: deve ter ao menos
            3 caracteres. O usuário é solicitado novamente caso a entrada seja inválida.
    
            Returns:
                Note: Objeto Note com o conteúdo digitado e cor padrão (YELLOW).
        """
        print("Digite a nota: ")
        user_input = input("> ").strip().capitalize()

        while (len(user_input) < 3):
            print("A nota não pode ser menor que 3 digitos!\nDigite a nota: ")
            user_input = input("> ").strip().capitalize()

        return Note(user_input)        

    @staticmethod
    def from_file(filepath: str) -> Note:
        """
            Cria uma ``Note`` a partir do conteúdo de um arquivo de texto.
    
            Args:
                filepath (str): Caminho absoluto ou relativo para o arquivo.
    
            Returns:
                Note: Objeto Note com o conteúdo do arquivo.
    
            Raises:
                NotImplementedError: Método ainda não implementado.
        """
        raise NotImplementedError
