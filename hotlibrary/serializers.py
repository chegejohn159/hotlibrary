from rest_framework import serializers
from hotlibrary.models import LecturerResource, LibrarianResource


class LecturerResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerResource
        fields = ('course', 'unit_code', 'semester', 'resource_type')


class LibrarianResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrarianResource
        fields = ('academic_year', 'course_name')
