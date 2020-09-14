from django.db import models


class CourtSnippet(models.Model):
    numeracao_unica = models.CharField(max_length=20, null=True, blank=False)
    recorte = models.TextField(null=False, blank=False)
    codigo_diario = models.CharField(max_length=200, null=False, blank=False)
    data_publicacao = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return str(self.numeracao_unica)

    class Meta:
        managed = False
        db_table = 'recortes_recorte'
