from django.urls import path

from . import views
app_name = "MIRA"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("health_remarks/", views.health_predict, name="health_predict"),
    path("manage_records/", views.records, name="records"),
    path("edit_view/<int:pk>/", views.edit_view, name="edit_view"),
    path("delete_view/<int:pk>/", views.delete_view, name="delete_view"),


]