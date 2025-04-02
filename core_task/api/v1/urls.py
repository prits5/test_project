from django.urls import path, include

urlpatterns = [
    path("credit_app/", include("api.v1.credit_application.urls")),
]
