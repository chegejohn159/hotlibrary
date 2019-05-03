from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import admin_required
from ..models import AdminChallenge, AdminResource, AdminTutorial, AdminHowToRepo


@method_decorator([login_required, admin_required], name='dispatch')
class TutorialUploadView(CreateView):
    model = AdminTutorial
    fields = ('tutorial_type', 'tutorial_name', 'tutorial_description')
    template_name = 'hotlibrary/admins/tutorialupload.html'

    def form_valid(self, form):
        admintutorial = form.save(commit=False)
        admintutorial.owner = self.request.user
        admintutorial.save()
        messages.success(self.request, 'The Tutorial(s) were upload successfully')
        return redirect('admins:uploads')


@method_decorator([login_required, admin_required], name='dispatch')
class ResourceUploadView(CreateView):
    model = AdminResource
    fields = ('resource_type', 'resource_name', 'resource_description')
    template_name = 'hotlibrary/admins/resourceupload.html'

    def form_valid(self, form):
        adminresource = form.save(commit=False)
        adminresource.owner = self.request.user
        adminresource.save()
        messages.success(self.request, 'The Resource(s) were upload successfully')
        return redirect('admins:uploads')


@method_decorator([login_required, admin_required], name='dispatch')
class ChallengeUploadView(CreateView):
    model = AdminChallenge
    fields = ('challenge_category', 'challenge_name', 'challenge_level', 'challenge_description')
    template_name = 'hotlibrary/admins/challengeupload.html'

    def form_valid(self, form):
        adminchallenge = form.save(commit=False)
        adminchallenge.owner = self.request.user
        adminchallenge.save()
        messages.success(self.request, 'The Challenge(s) were upload successfully')
        return redirect('admins:uploads')


@method_decorator([login_required, admin_required], name='dispatch')
class HowUploadView(CreateView):
    model = AdminHowToRepo
    fields = ('howto_description',)
    template_name = 'hotlibrary/admins/howtoupload.html'

    def form_valid(self, form):
        adminhowto = form.save(commit=False)
        adminhowto.owner = self.request.user
        adminhowto.save()
        messages.success(self.request, 'The How Packs were upload successfully')
        return redirect('admins:uploads')
