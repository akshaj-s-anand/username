from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="User Group")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'group')

    def save(self, commit=True):
        # Save the user instance
        user = super(CustomUserCreationForm, self).save(commit=False)
        
        # Add any other logic for additional fields here
        if commit:
            user.save()
            # Add the user to the selected group
            selected_group = self.cleaned_data['group']
            selected_group.user_set.add(user)
        
        return user

