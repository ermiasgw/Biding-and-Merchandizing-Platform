from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django_countries.serializer_fields import CountryField
from .models import Category

# common fields for a all roles of users
class CommonSerializer(RegisterSerializer):
    username = None
    address = serializers.CharField()
    phone_number = PhoneNumberField()
    country = CountryField()


class IndividualRegistrationSerializer(CommonSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()  

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.user_type = 1
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def custom_signup(self, request, user):
        data = self.get_cleaned_data()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        date_of_birth = data.get("date_of_birth")
        identification_no = data.get("identification_no")

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }
        



class OrganizationRegistrationSerializer(CommonSerializer):
    name = serializers.CharField()
    category = serializers.MultipleChoiceField(choices=Category.objects.all().values_list('name'))
    website = serializers.URLField()
    description = serializers.TextField()

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.user_type = 2
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def custom_signup(self, request, user):
        data = self.get_cleaned_data()
        name = data.get("name")
        category = data.get("category")
        website = data.get("website")
        description = data.get("description")
        tin_no = data.get("tin_no")

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }
