"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import re
from collections import OrderedDict

from django.contrib import admin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, include
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.renderers import ReDocRenderer as BaseReDocRenderer, OpenAPIRenderer
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = 'Mash-Up 관리사이트'


class SchemaGenerator(OpenAPISchemaGenerator):
    PATTERN_ERASE_WORDS = re.compile('|'.join(
        ['list', 'create', 'read', 'update', 'partial_update', 'destroy']))

    def get_paths_object(self, paths: OrderedDict):
        # operation_id에서, PATTERN_ERASE_WORDS에 해당하는 단어를 지운 후 오름차순으로 정렬
        def path_sort_function(path_tuple):
            operation_id = path_tuple[1].operations[0][1]['operationId']
            operation_id = self.PATTERN_ERASE_WORDS.sub('', operation_id)
            return operation_id

        paths = OrderedDict(sorted(paths.items(), key=path_sort_function))
        return super().get_paths_object(paths)


BaseSchemaView = get_schema_view(
    openapi.Info(
        title='Mash-Up API',
        default_version='v1',
        description='Mash-Up API Documentation',
        contact=openapi.Contact(email='dev@lhy.kr'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=SchemaGenerator,
)


class ReDocRenderer(BaseReDocRenderer):
    template = 'docs/redoc.html'


class RedocSchemaView(BaseSchemaView):
    renderer_classes = (ReDocRenderer, OpenAPIRenderer)


urlpatterns_views = [
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns_apis = [
    path('members/', include('members.urls')),
    path('notices/', include('notice.urls')),
]
urlpatterns = [
    re_path(r'^doc/$', RedocSchemaView.as_cached_view(cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('', include(urlpatterns_views)),
    path('api/', include(urlpatterns_apis)),
]

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if SETTINGS_MODULE in ('config.settings', 'config.settings.dev'):
    try:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    except ModuleNotFoundError:
        pass
