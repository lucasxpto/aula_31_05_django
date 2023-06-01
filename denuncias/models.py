# from django.contrib.auth.models import User
# from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth import get_user_model


class Denuncia(models.Model):
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Descrição', max_length=500)
    criado = models.DateTimeField('Criado em', auto_now_add=True)

    # Primeira forma de utilização do UserModel
    # autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor_denuncia')

    # Segunda forma de utilização do UserModel
    # autor = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='autor_denuncia')

    # Terceira forma de utilização do UserModel
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='autor_denuncia')

    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'

    def __str__(self):
        return self.titulo


