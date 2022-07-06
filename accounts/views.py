from django.views.generic import CreateView, TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy
from django.core.mail import EmailMessage

from .models import User
from .forms import UserCreationForm
from .tokens import account_activation_token


class UserCreateView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'accounts/user_create.html'
    success_url = reverse_lazy('accounts:user_create_done')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()      
        use_https = self.request.is_secure(),
        current_site = get_current_site(self.request)  
        mail_subject = 'Link to activate your account'  
        message = loader.render_to_string('accounts/account_activate_email.html', {
            "protocol": "https" if use_https else "http",
            'user': user,  
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            'token':account_activation_token.make_token(user),  
            })  
        to_email = form.cleaned_data.get('email')  
        email = EmailMessage(mail_subject, message, to=[to_email])  
        email.send()
              
        return super().form_valid(form)
    
class UserCreateDoneView(TemplateView):
    template_name = 'accounts/user_create_done.html'
    
    
class UserActivateView(TemplateView):
    template_name = 'accounts/user_activate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:  
            uid = urlsafe_base64_decode(kwargs['uidb64']).decode()
            user = User.objects.get(pk=uid)  
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
            user = None  
        if user is not None and account_activation_token.check_token(user, kwargs['token']):  
            user.is_active = True  
            user.save()
            context['result'] = 'Ваш имейл подтвержден, теперь вы можете войти в свой аккаунт'
            context['activation_success'] = True
            return context
        else:
            context['result'] = 'Ссылка для активации недействительна!'
            return context
