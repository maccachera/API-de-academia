from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class AlunoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        aluno = self.model(email=email, **extra_fields)
        aluno.set_password(password) # Isso criptografa a senha no banco!
        aluno.save(using=self._db)
        return aluno

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)





class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valorMensal = models.DecimalField(max_digits=10, decimal_places=2)
    mesesFidelidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Aluno(AbstractUser):
    username = None  # Removendo o campo username
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, null=True, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True)
    is_ativo = models.BooleanField(default=True)

    # Configurações de Login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome'] # Campos obrigatórios ao criar superusuário

    objects = AlunoManager() # Conecta com o gerenciador que criamos

    def __str__(self):
        return self.nome


class FichaTreino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()


    def __str__(self):
        return f"Ficha de treino de {self.aluno.nome}: {self.titulo}"

class RegistroAcesso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"Acesso de {self.aluno.nome} em {self.data_hora}"