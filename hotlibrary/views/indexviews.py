from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from hotlibrary.decorators import admin_required, superuser_required
from hotlibrary.forms import StaffSignupForm


def verify_user_upload(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admins:uploads')
        elif request.user.is_lecturer:
            return redirect('lecturers:lectureruploads')
        elif request.user.is_librarian:
            return redirect('librarians:librarianuploads')
        else:
            return render(request, 'hotlibrary/whoops.html')
    else:
        return render(request, 'hotlibrary/whoopy.html')


# you do not have permissions to view this page, Contact the administrator for approval


class HomeView(TemplateView):
    template_name = 'hotlibrary/index.html'


class AboutView(TemplateView):
    template_name = 'hotlibrary/about.html'


@method_decorator([login_required, admin_required], name='dispatch')
class VerifyUploadView(TemplateView):
    template_name = 'hotlibrary/upload.html'


class AndroidView(TemplateView):
    template_name = 'android.html'


@superuser_required(login_url='login')
def staff_signup_view(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffsignup')
    else:
        form = StaffSignupForm()
    return render(request, 'accounts/staff_signup.html', {'form': form})
