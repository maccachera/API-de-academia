from django.contrib import admin

# Register your models here.



from django.contrib import admin
from .models import Aluno, Unidade, Plano, FichaTreino, RegistroAcesso

admin.site.register(Aluno)
admin.site.register(Unidade)
admin.site.register(Plano)
admin.site.register(FichaTreino)
admin.site.register(RegistroAcesso)