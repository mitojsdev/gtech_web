from django.urls import path
from . import views

urlpatterns = [path('login/',views.login_view, name='login'),
               path('telainicio/', views.tela_inicial,name='telaInicio'),
               path('cadastrar_cliente/', views.cadastrar_cliente,name='cadastrar_cliente'),
               path('pesquisar-cliente/', views.pesquisar_cliente, name='pesquisar_cliente'),               
]