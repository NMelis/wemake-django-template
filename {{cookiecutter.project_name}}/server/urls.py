# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from server.api import urlpatterns as api_urlpatterns
from server.settings.components import config

schema_view = get_schema_view(
    openapi.Info(
        title='Документация API',
        default_version='v1',
        description='{{ cookiecutter.project_verbose_name }}',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='admin@exemple.com'),
        license=openapi.License(name='BSD License'),
    ),
    validators=['flex', 'ssv'],
    public=True,
    url=config('SERVER_HOST', 'http://127.0.0.1:8000'),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url('admin/', admin.site.urls),
] + api_urlpatterns


if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    from django.views.static import serve

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        url(r'^__debug__/', include(debug_toolbar.urls)),

        # Serving media files in development only:
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + urlpatterns
