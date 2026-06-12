"""
    bot_controller.py
    -----------------
    Orquestra o fluxo completo de criação e envio de notas ao Discord.
    
    Responsabilidade:
        Atuar como camada de controle (Controller) que conecta os serviços
        de criação de nota (``NoteService``) ao serviço de envio (``WebhookDispatcher``),
        reportando o resultado ao usuário via console.
    
    Fluxos disponíveis:
        - ``run_console_to_discord``: lê nota do terminal e envia ao Discord.
        - ``run_file_to_discord``   : (não implementado) lê nota de arquivo e envia.
"""

from services import NoteService
from services import WebhookDispatcher


class BotController:
    """
        Controlador principal do DiscNote.
    
        Coordena os serviços de nota e webhook, expondo fluxos de alto nível
        que podem ser chamados diretamente pelo ``main.py``.
    
        Todos os métodos são estáticos — a classe não precisa ser instanciada.
    """

    @staticmethod
    def run_console_to_discord():
        """
            Executa o fluxo: leitura no console → envio ao Discord.
    
            Solicita uma nota ao usuário via terminal, cria o objeto ``Note``
            através do ``NoteService`` e o despacha com o ``WebhookDispatcher``.
            Exibe mensagem de sucesso ou falha ao final.
        """
        nova_nota = NoteService.from_console()
        success, status_code = WebhookDispatcher.send(nova_nota)
        
        if success:
            print("Controlador: Nota enviada com sucesso ao Discord!")
        else:
            print(f"Controlador: Falha ao enviar a nota!\nstatus code: {status_code}")

    @staticmethod
    def run_file_to_discord():
        """
            Executa o fluxo: leitura de arquivo → envio ao Discord.
    
            Raises:
                NotImplementedError: Método ainda não implementado.
        """
        raise NotImplementedError
