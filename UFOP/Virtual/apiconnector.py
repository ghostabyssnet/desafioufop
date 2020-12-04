# This file handles all sorts of datababase management.
# I know it isn't as organized as it could be, more so if we consider bigger projects.
# However, this isn't one of those, so it should do the trick.
# Also, let's be honest: Python is terrible at handling files.

from .models import Pessoa

# creates a new Pessoa in the database
def CreatePerson(*payload):
    person= Pessoa(
        nome= payload[0],
        sobrenome= payload[1],
        telefone= payload[2],
        data_nascimento= payload[3],
        email= payload[4]
    )
    person.save()