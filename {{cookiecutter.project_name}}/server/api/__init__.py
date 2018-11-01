# -*- coding: utf-8 -*-

from server.api.v1.urls import router as v1_router
from django.conf.urls import url, include
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

urlpatterns = [
    url('auth/login/', obtain_jwt_token),
    url('auth/token_verify/', verify_jwt_token),
    url('auth/token_refresh/', refresh_jwt_token),
    url('v1/', include(v1_router.urls)),
]
