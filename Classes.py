from enum import Enum
from datetime import date,datetime,timedelta

class StatusPrescricao(Enum):
    VÁLIDA=1
    INVÁLIDA=2

class PrioridadeTarefa(Enum):
    ALTA=1
    MEDIA=2
    BAIXA=3

class Usuario:
    def __init__(self, nome_usuario, senha):
        self.nome_usuario=nome_usuario
        self.senha=senha
        self.tarefas=[]
    def atualizar_status_tarefas(self):
        hoje = date.today()  

    def adicionar_tarefa(self, titulo, prazo=None, status=StatusTarefa.A_FAZER, prioridade=PrioridadeTarefa.MEDIA):
        tarefa=Tarefa(titulo, prazo, status, prioridade)
        self.tarefas.append(tarefa)
    
    def marcar_como_feito(self, tarefa):
        tarefa.status=StatusTarefa.FEITO

    def marcar_como_fazendo(self, tarefa):
        tarefa.status=StatusTarefa.FAZENDO

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)

    def atualizar_status_tarefas(self):
        hoje=date.today()
        for tarefa in self.tarefas:
            if tarefa.prazo and tarefa.prazo<hoje and tarefa.status != StatusTarefa.FEITO:
                tarefa.status=StatusTarefa.ATRASADO

class Tarefa:
    def __init__(self, titulo, prazo=None, status=StatusTarefa.A_FAZER, prioridade=PrioridadeTarefa.MEDIA):
        self.titulo=titulo
        self.prazo=prazo
        self.status=status
        self.prioridade=prioridade

    def __str__(self):
        prazo_str=self.prazo.strftime("%d/%m/%Y") if self.prazo else "Sem prazo definido."
        return f"Descrição: {self.titulo} \nPrazo: {prazo_str} \nStatus:{self.status.name} \nPrioridade: {self.prioridade.name}"


def main():
    usuario=Usuario("usuario_padrao", "senha_padrao")

    while True:
        print("\nEscolha uma ação:\n 1. Adicionar tarefa\n 2. Listar tarefas\n 3. Marcar tarefa como feita\n 4. Marcar tarefa como fazendo\n 5. Atualizar status das tarefas\n 6. Remover tarefa\n 7. Sair")

        escolha=input("> ")

        if escolha == '1':
            titulo=input("Descrição da tarefa: ")
            while True:
                try:
                    prazo_str=input("Prazo (dd/mm/aaaa - Enter para sem prazo): ")
                    prazo=datetime.strptime(prazo_str, "%d/%m/%Y").date() if prazo_str else None
                except ValueError:
                    print("Data inválida. Veja se digitou correto e use o formato dd/mm/aaaa")
                    continue
                break
            usuario.adicionar_tarefa(titulo, prazo)

        elif escolha=='2':
            usuario.listar_tarefas()

        elif escolha=='3':
            titulo=input("digite o Título da tarefa a ser marcada como feita")
            for tarefa in usuario.tarefas:
                if tarefa.titulo==titulo:
                    usuario.marcar_como_feito(tarefa)
                    break
    
        elif escolha=='4':
            titulo=input("digite o Título da tarefa a ser marcada como fazendo: ")
            for tarefa in usuario.tarefas:
                if tarefa.titulo==titulo:
                    usuario.marcar_como_fazendo(tarefa)
                    break

        elif escolha=='5':
            usuario.atualizar_status_tarefas()
    
        elif escolha=='6':
            titulo=input("digite o Título da tarefa a ser removida: ")
            for tarefa in usuario.tarefas:
                if tarefa.titulo==titulo:
                    usuario.remover_tarefa(tarefa)
                    break
            
        elif escolha=='7':
            break

        else:
            print("Opção inválida.")

if __name__=="__main__":
    main()
