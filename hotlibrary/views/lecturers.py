from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from ..decorators import lecturer_required
from ..models import LecturerResource


@method_decorator([login_required, lecturer_required], name='dispatch')
class LecturerUploadView(CreateView):
    model = LecturerResource
    fields = ('course', 'unit_code', 'semester', 'resource_type')
    template_name = 'hotlibrary/lecturers/lecturerupload.html'

    def form_valid(self, form):
        lecturerresource = form.save(commit=False)
        lecturerresource.owner = self.request.user
        lecturerresource.save()
        messages.success(self.request, 'The Resources(s) were upload successfully')
        return redirect('home')


class UploadTest(TemplateView):
    template_name = 'hotlibrary/lecturers/apitest.html'
