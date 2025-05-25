from django.urls import path
from . import views

urlpatterns = [
    path('',                                    views.home,             name='home'),
    path('loja/<int:loja_id>/',                 views.loja_view,        name='loja'),
    path('loja/<int:loja_id>/editar/',          views.editar_loja,      name='editar_loja'),
    path('criar-loja/',                         views.criar_loja,       name='criar_loja'),
    
    path('login/',                              views.login_view,       name='login'),
    path('logout/',                             views.logout_view,      name='logout'),
    path('signup/',                             views.signup_view,      name='signup'),
    path('loja/<int:loja_id>/produto/criar/',   views.criar_produto,    name='criar_produto'),
    
    path(
        'loja/<int:loja_id>/produto/<int:produto_id>/editar/',
        views.editar_produto,
        name='editar_produto'
    ),
]