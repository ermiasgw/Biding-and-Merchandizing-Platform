from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email,user_field


# adapter class for basic user registration
class CustomAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        address = data.get("address")
        phone_number = data.get("phone_number")
        country = data.get("country")
        email = data.get("email")
        user_email(user, email)
        if address:
            user_field(user, "address", address)
        if phone_number:
            user_field(user, "phone_number", phone_number)
        if country:
            user_field(user, "country", country)
        
        if "password1" in data:
            user.set_password(data["password1"])

        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user


