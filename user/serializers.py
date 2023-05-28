from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django_countries.serializer_fields import CountryField
from .models import Category, Individual, Organization
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class IndividualRegistrationSerializer(RegisterSerializer):
    username = None
    address = serializers.CharField()
    country = CountryField()
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
        individual = Individual.objects.create(user=user, first_name=first_name, last_name=last_name,date_of_birth=date_of_birth)

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'address': self.validated_data.get('adress', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'country': self.validated_data.get('country', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'date_of_birth': self.validated_data.get('date_of_birth', ''),
        }
        



class OrganizationRegistrationSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    address = serializers.CharField()
    phone_number = PhoneNumberField()
    country = CountryField()
    name = serializers.CharField()
    category = serializers.MultipleChoiceField(choices=Category.objects.all().values_list('name'))
    website = serializers.URLField()
    description = serializers.CharField()

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
        user.is_active = False
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
        org = Organization.objects.create(user=user, name=name, category=category,website=website, description=description, tin_no=tin_no)


    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'address': self.validated_data.get('adress', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'country': self.validated_data.get('country', ''),
            'name': self.validated_data.get('name', ''),
            'category': self.validated_data.get('category', ''),
            'website': self.validated_data.get('website', ''),
            'description': self.validated_data.get('description', ''),
            'tin_no': self.validated_data.get('tin_no', ''),
        }

class CustomLoginSerializer(LoginSerializer):
    username = None
    
