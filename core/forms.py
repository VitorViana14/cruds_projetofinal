from django.forms import ModelForm

class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'numero', 'cpf']