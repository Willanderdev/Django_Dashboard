from django import forms

from .models import Produto, Vendedor, Vendas


class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormVendedor(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormVendas(forms.ModelForm):
    
    class Meta:
        model = Vendas

        fields = ['nome_produto', 'vendedor', 'total', 'data']

  