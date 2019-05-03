from django.contrib import admin

from hotlibrary.models import (User, MsuFacultyList, MsuDepartmentList,
                               StudySemester, DeptCourse, DeptUnit,
                               LecturerResource, AdminTutorial, AdminResource,
                               AdminChallenge, AdminHowToRepo, LibrarianResource)


admin.site.register(User)
admin.site.register(MsuFacultyList)
admin.site.register(MsuDepartmentList)
admin.site.register(StudySemester)
admin.site.register(DeptCourse)
admin.site.register(DeptUnit)

admin.site.register(LecturerResource)
admin.site.register(LibrarianResource)
admin.site.register(AdminTutorial)
admin.site.register(AdminResource)
admin.site.register(AdminHowToRepo)
admin.site.register(AdminChallenge)


