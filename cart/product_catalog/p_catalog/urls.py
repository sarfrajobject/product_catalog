from django.urls import path
from django.conf.urls import url
from.import views
urlpatterns = [
    # url(r'^Product/Cart1/(?P<pk>\d+)$', views.Cart1, name='post_edit'),
    path('',views.home,name = 'home'),
    # path('Product_details/pk>',views.P_datails),
    url('product_cart',views.product_cart),
    # path('Registation',views.Registation,name = 'Registation'),
    # # path('Cart/checkOut',views.Buy,name = 'Buy'),
    path('popup',views.popup),
    # path('signup', views.setsession),
    # path('gsession', views.getsession),
    # path('home2',views.home2,name = 'home2'),
    # # url(r'^addtocart/(?P<cart_id>\d+)', views.Cart1
    url(r'^Product_details/(?P<id>\d+)$', views.P_datails),
    # url(r'^list$', views.list, name='list'),
    # # path('edit/<int:id>', views.editFunction, name='edit'),
    # # url(r'^Add/(?P<pk>\d+)$', views.Addcart, name='Addcart'),
    # url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
    # url(r'^Cart1/(?P<id>\d+)$', views.Cart1, name='Cart1'),
    # path('P_datails/<int:pk>', views.P_datails.as_view()),
    

]