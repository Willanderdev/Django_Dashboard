from django.urls import path, include
from .views import produto, Venda, Vendedores, home, retorna_total_vendido, relatorio_faturamento, relatorio_produtos, relatorio_funcionario

urlpatterns = [
    path('', home, name="home"),
    path('produto', produto.as_view(), name='produto'),
    path('vendedor', Vendedores.as_view(), name='vendedor'),
    path('venda', Venda.as_view(), name='venda'),
    path('retorna_total_vendido', retorna_total_vendido,
         name="retorna_total_vendido"),
    path('relatorio_faturamento', relatorio_faturamento,
         name="relatorio_faturamento"),
    path('relatorio_produtos', relatorio_produtos, name="relatorio_produtos"),
    path('relatorio_funcionario', relatorio_funcionario,
         name="relatorio_funcionario"),
    
]
