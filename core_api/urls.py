from django.contrib import admin
from django.urls import path, include

from user.urls import *  # noqa
from customer.urls import *  # noqa
from machine.urls import *  # noqa

admin.site.site_header = "SMTCMMS Manager"
admin.site.site_title = "SMTCMMS Manager"
admin.site.index_title = "SMTCMMS Manager"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),  # noqa: F405
]
