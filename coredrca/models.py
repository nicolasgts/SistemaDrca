from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Credito(models.Model):
    diisc_pre = models.IntegerField()
    disc_credito = models.IntegerField()
    aluno_credito_obri = models.IntegerField()
    aluno_credito_let = models.IntegerField()
    
    def __str__(self):
        return self.disc_credito.__str__()

class Departamento(models.Model):
    nome = models.CharField(max_length =30)
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.TextField()
    departamento = models.ForeignKey(Departamento ,null = True)
    
    def __str__(self):
        return self.nome

class Secretaria(models.Model):
    nome = models.CharField(max_length = 30)
    tipo = models.IntegerField() #tipo 0 graduacao tipo 1 posgraduacao
    departamento = models.ForeignKey(Departamento, null = True)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 30)
    secretaria = models.ForeignKey(Departamento, null = True)
    
    def __str__(self):
        return self.nome
        
class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)
    obr_let = models.TextField()
    status = models.TextField()
    credito = models.ForeignKey(Credito)
    disc_pre = models.ManyToManyField('Disciplina')
    curso = models.ForeignKey(Curso, null = True)
    professor = models.ForeignKey(Professor)
    
    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length = 30)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso , null = True)
    credito = models.ForeignKey(Credito)
    disciplinas = models.ManyToManyField(Disciplina , blank = True)
     
    def __str__(self):
        return self.nome
    
