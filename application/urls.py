from .views import get_student_info,search_results
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('',TemplateView.as_view(template_name = "index.html")),
    path('student-info/<int:id>',get_student_info),
    path('search/',search_results),
]
