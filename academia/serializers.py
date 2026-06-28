from rest_framework import serializers
from .models import Unidade, Plano, Aluno, FichaTreino, RegistroAcesso 




class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = '__all__'

# segurança da senha do usuário para não ser exposta na API
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'email', 'nome', 'telefone', 'plano', 'unidade', 'is_ativo', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
       
        password = validated_data.pop('password', None)
        
        aluno = super().create(validated_data)
        
        if password:
            aluno.set_password(password)
            aluno.save()
        return aluno
    
class FichaTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaTreino
        fields = '__all__'



class RegistroAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcesso
        fields = '__all__'