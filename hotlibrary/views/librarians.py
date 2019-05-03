from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import librarian_required
from ..models import LibrarianResource


@method_decorator([login_required, librarian_required], name='dispatch')
class LibrarianUploadView(CreateView):
    model = LibrarianResource
    fields = ('academic_year', 'course_name')
    template_name = 'hotlibrary/librarians/librarianupload.html'

    def form_valid(self, form):
        librarianresource = form.save(commit=False)
        librarianresource.owner = self.request.user
        librarianresource.save()
        messages.success(self.request, 'The Past Papers(s) were upload successfully')
        return redirect('hotlibrary/index.html')
