from rest_framework import serializers

from .models import Pessoa


class PessoaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(required=False,allow_blank=True, max_length=30)
    sobrenome = serializers.CharField(required=False,allow_blank=True, max_length=30)
    email = serializers.CharField(required=False, allow_blank=True, max_length=30)
    senha = serializers.CharField(required=False, allow_blank=True, max_length=30)

    def create(self,validated_data):
        return Pessoa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        instance.email = validated_data.get('email', instance.email)
        instance.senha = validated_data.get('Senha', instance.senha)
        instance.save()
        return instance