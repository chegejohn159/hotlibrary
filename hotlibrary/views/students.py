# Django
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from hotlibrary.forms import StudentSignupForm


# Project


def student_signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentSignupForm()
    return render(request, 'accounts/student_signup.html', {'form': form})


class StudentView(TemplateView):
    template_name = 'hotlibrary/students/students.html'
