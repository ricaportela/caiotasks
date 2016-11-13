import datetime


class Tarefa(object):
    """
    docstring for Tarefas.
    """
    STATUS = ('pra fazer', 'fazendo', 'feita')

    def __init__(self, description, status, responsable, date_create, date_update):
        # self representa a instancia do object
        self.description = description
        self.status = status
        self.responsable = responsable
        self.date_create = date_create
        self.date_update = date_update

    def validastatus(txtstatus):
        if txtstatus not in self.STATUS:
            raise ValueError("%s is not a valid status" % txtstatus)

hoje = datetime.date.today().strftime('%x')
tf1 = Tarefas("tarefa1", "feita", "ricardo", hoje, "01/05/2016")
print("Descrição.....: %s" % tf1.description)
print("Responsavel...: %s" % tf1.responsable)
print("Data Criacao..: %s" % tf1.date_create)
print("Status........: %s" % tf1.status)