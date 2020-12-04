from django.db import models

# Aluno (student), Instituicao, Universidade, Disciplina, Pais, Mobilidade
# bonus: Pessoa(superset of Aluno and Empregado, used for administration purposes),
# Empregado (admin purposes as well),

# Pessoa: the superset of our classes
class Pessoa(models.Model):
    nome= models.CharField(max_length=32)
    sobrenome= models.CharField(max_length=32)
    telefone= models.CharField(max_length=16)
    data_nascimento= models.DateField(auto_now=False, auto_now_add=False)
    email= models.EmailField(max_length=128)

class Aluno(models.Model):
    pessoa= models.ForeignKey("Virtual.Pessoa", on_delete=models.CASCADE)
    # numero de matricula/registration number
    matricula= models.IntegerField()
    # let (mobilidade) handle transfers, we just point to it
    # if the field is blank, then the student is from ufop
    mobilidade= models.ForeignKey("Virtual.Mobilidade", on_delete=models.CASCADE, blank=True)

class Empregado(models.Model):
    pessoa= models.ForeignKey("Virtual.Pessoa", on_delete=models.CASCADE)
    # I have no idea if UFOP uses registration numbers for its employees as well,
    # so I'm leaving this here. If it doesn't, we can just ignore then delete it
    matricula: models.IntegerField()
    # Is he a teacher/professor? Is he something else?
    # It IS redundant for this project, it's just to show there's a lot to think about
    trabalho: models.CharField(max_length=32)
    # Are they outsourced? If they are, we define it here.
    # If they're not, we just define it as Universidade Federal de Ouro Preto
    instituicao: models.ForeignKey("Virtual.Instituicao", on_delete=models.CASCADE)

class Instituicao(models.Model):
    nome= models.CharField(max_length=32)
    # insert stuff...
    # this field is generally used for outsourced employees

class Universidade(models.Model):
    # all universities are technically institutes, so...
    # we'll handle their name using their parent (Virtual.Instituicao)
    instituicao= models.ForeignKey("Virtual.Instituicao", on_delete=models.CASCADE)
    pais= models.ForeignKey("Virtual.Pais", on_delete=models.CASCADE)

class Pais(models.Model):
    nome= models.CharField(max_length=32)
    # what else are we even supposed to add here? timezones can be fetched in a script...
    # continents? I didn't add a country list because it would be overkill, but it can be fetched
    # in JSON or something

class Mobilidade(models.Model):
    ESCOLHAS = (
        ('D', 'de'),
        ('P', 'para'),
    )
    pessoa= models.ForeignKey("Virtual.Pessoa", on_delete=models.CASCADE)
    universidade= models.ForeignKey("Virtual.Universidade", on_delete=models.CASCADE)
    periodo_inicio= models.DateField(auto_now=False, auto_now_add=False)
    periodo_fim= models.DateField(auto_now=False, auto_now_add=False)
    # (D) did he come from another university, or...
    # (P) did he transfer from UFOP to it?
    de_para= models.CharField(max_length=1, choices=ESCOLHAS)