from django.urls import include, path


from hotlibrary.views import APIviews, students
from hotlibrary.views.APIviews import LecturerResourceUploadCompleteHandler
from hotlibrary.views.indexviews import AboutView, AndroidView, verify_user_upload, staff_signup_view
from hotlibrary.views.students import student_signup_view
from .views import admins, lecturers, librarians, indexviews

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('android/', AndroidView.as_view(), name='android'),
    path('verify/', verify_user_upload, name='verify',),
    path('staffs/accounts/signup/', staff_signup_view, name='staffsignup'),

    path('admins/', include(([
        path('uploads/', indexviews.VerifyUploadView.as_view(), name='uploads'),
        path('uploads/tutorials/', admins.TutorialUploadView.as_view(), name='tutorials'),
        path('uploads/resources/', admins.ResourceUploadView.as_view(), name='resources'),
        path('uploads/challenges/', admins.ChallengeUploadView.as_view(), name='challenges'),
        path('uploads/howto/', admins.HowUploadView.as_view(), name='howtos'),
    ], 'hotlibrary'), namespace='admins')),

    path('lecturers/', include(([
        path('lectureruploads/', lecturers.LecturerUploadView.as_view(), name='lectureruploads'),
        path('test/', lecturers.UploadTest.as_view(), name='upload-home'),
        path('api/files/policy/', APIviews.LecturerUploadAPI.as_view(), name='upload-policy'),
        path('api/files/complete/', LecturerResourceUploadCompleteHandler.as_view(), name='upload-complete'),
    ], 'hotlibrary'), namespace='lecturers')),

    path('librarian/', include(([
        path('librarianuploads/', librarians.LibrarianUploadView.as_view(), name='librarianuploads'),
        path('api/files/policy/', APIviews.LibrarianUploadAPI.as_view(), name='upload-policy'),
    ], 'hotlibrary'), namespace='librarians')),

    path('students/', include(([
        path('downloads/', students.StudentView.as_view(), name='download'),
        path('accounts/signup/', student_signup_view, name='stdsignup'),
    ], 'hotlibrary'), namespace='students')),



]

