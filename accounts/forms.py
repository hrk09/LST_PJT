from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model # 현재 활성화(active)된 user model 을 return 한다. 
from django import forms
from .models import Guild
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class GuildForm(forms.ModelForm):

    class Meta:
        model = Guild
        fields = ['name', ]


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text='<a href=\"password/\">여기서 변경</a>.'
    )

    class Meta:
        model = get_user_model() # accounts.User
        fields = ['nickname', ]


# 커스터마이징한 유저모데을 인식하지 못해서 직접 get_user_model 함수로 
# 유저 모델 정보를 넣어줌 
class CustomUserCreationForm(UserCreationForm):
    error_messages = {
         'password_mismatch':'틀렸어!',
    }
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='성공?',
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='??',
    )

    class Meta:
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        # fields = ['username', 'nickname', 'age', 'password1', 'password2', ]
        fields = ['username', 'nickname', 'age', ]
        help_texts = {
            'username': 'test',
            'age': '안녕',
            # 'password1': '입력',    
            # 'password2': '확인'
        }
        