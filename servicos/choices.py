from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_OLEO = "TO", "TROCAR ÓLEO"
    TROCAR_PASTILHAS_FREIO = "TPF", "TROCAR PASTILHAS DE FREIO"
    BALANCEAMENTO = "B", "BALENCEAMENTO"
    SUSPENSAO = "S", "SUSPENSAO"