from django.shortcuts import render
from .models import StudentInfo
def get_student_info(request,id):
    context = {}
    try:
        student_obj = StudentInfo.objects.get(id = id)
        context["student_obj"] = student_obj
    except Exception:
        context["error"] = "No Student Found with id "+ str(id)
    return render(request,'student-details.html',context)

def search_results(request):
    context = {}
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        if id:
            try:
                student_obj = StudentInfo.objects.get(id = id)
                context["id"] = id
                context["student_obj"] = student_obj
            except Exception:
                context["error"] = "No Student Found with id "+ str(id)
        elif name:
            try:
                student_obj = StudentInfo.objects.get(first_name = name)
                context["name"] = name
                context["student_obj"] = student_obj
            except Exception:
                context["error"] = "No Student Found with First Name "+ name
        else:
            context["error"] = "Don't have Id field or Name Field"
    return render(request,'search-details.html',context)
