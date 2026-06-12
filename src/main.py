"""
    main.py
    -------
    Ponto de entrada da aplicação DiscNote.
    
    Responsabilidade:
        Inicializa o fluxo principal chamando o BotController,
        que orquestra a leitura da nota no console e o envio ao Discord.
    
    Uso:
        Execute diretamente via terminal:
            $ python main.py
"""


from controllers import BotController

if __name__ == "__main__":
    BotController.run_console_to_discord()
