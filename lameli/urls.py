from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls', namespace='order')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('about_us/', TemplateView.as_view(template_name='shop/about_us.html'),
            name='about_us'),
    path('contacts/', TemplateView.as_view(template_name='shop/contacts.html'),
         name='contacts'),
    path('', include('shop.urls', namespace='shop')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
