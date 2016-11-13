class Tarefas():
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

    def validastatus(self, status):
        if self.status not in self.STATUS:
            raise ValueError("%s is not a valid status" % status)

    def addTarefas():
        pass

    def updTarefas():
        pass

    def delTarefas():
        pass

    def listTarefas():
        pass
