from models import Note


class NoteService:
    @staticmethod
    def from_console() -> Note:
        print("Digite a nota: ")
        user_input = input("> ").strip().capitalize()

        while (len(user_input) < 3):
            print("A nota não pode ser menor que 3 digitos!\nDigite a nota: ")
            user_input = input("> ").strip().capitalize()

        return Note(user_input)        

    @staticmethod
    def from_file(filepath: str) -> Note:
        # Lógica de leitura de arquivo -> cria Note
        pass
