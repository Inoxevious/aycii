from django.conf.urls import url
from django.urls import path, include
from .views import index , blog, product, cart, contact, blog_detail, product_detail, about, faq
# SET THE NAMESPACE!
app_name = 'mush_store'
# Be careful setting the name to just /blog use userblog instead!
urlpatterns=[

    path('blog/', blog, name='blog'),
    path('index/', index, name='index'),
    path('product/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('blog_detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('blog_detail/', blog_detail, name='blog_detail'),
    path('product_detail/', product_detail, name='product_detail'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
   
]