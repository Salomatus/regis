from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("blog/", include("blog.urls", namespace="blog")),
]
