from django.http.response import JsonResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Produto, Vendas, Vendedor
from datetime import datetime
from django.db.models import Sum
from .forms import FormProduto, FormVendas, FormVendedor

def home(request):
    prod = FormProduto
    vend = FormVendas
    vendedor = FormVendedor
    context = {'prod': prod, 'vend': vend, 'vendedor': vendedor}
    return render(request, 'home.html', context)


class produto(CreateView):
    form_class = FormProduto
    success_url = reverse_lazy('home')
    template_name = 'produto.html'
    

class Venda(CreateView):
    model = Vendas
    form_class = FormVendas
    success_url = reverse_lazy('home')
    template_name = 'vendas.html'
    
    def form_valid(self, form):
        # Adicionar usuário logado como user
        form.instance.user = self.request.user
        
        # Chama o comportamento de validação do formulário da superclasse
        return super(Venda, self).form_valid(form)


class Vendedores(CreateView):
    form_class = FormVendedor
    success_url = reverse_lazy('home')
    template_name = 'vendedor.html'
    

def retorna_total_vendido(request):
    
    # o aggregate transforma os dados em um dicionario e soma todos os dados do dicionario com o metodo Sum, ele soma todos os dados da coluna total
    total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    if request.method == "GET":
        return JsonResponse({'total': total})

def relatorio_faturamento(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)

def relatorio_produtos(request):
    produtos = Produto.objects.all()
    label = []
    data = []
    for produto in produtos:
        vendas = Vendas.objects.filter(nome_produto=produto).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(produto.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def relatorio_funcionario(request):
    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(vendedor.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

