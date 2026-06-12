from services import NoteService
from services import WebhookDispatcher


class BotController:
    @staticmethod
    def run_console_to_discord():
        nova_nota = NoteService.from_console()
        success, status_code = WebhookDispatcher.send(nova_nota)
        
        if success:
            print("Controlador: Nota enviada com sucesso ao Discord!")
        else:
            print(f"Controlador: Falha ao enviar a nota!\nstatus code: {status_code}")

    @staticmethod
    def run_file_to_discord():
        pass
