from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django import forms

from authentication.forms import Registration
from authentication.tokens import authenticationToken
from authentication.models import Profile

#View for telling verification was successful
@login_required
def emailsuccess(request):
    return render(request, 'emailsuccess.html')


#View for registering new users
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your gamestore account!'
            message = render_to_string('authEmail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': authenticationToken.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('authEmailSent')
    else:
        form = Registration()
    return render(request, 'register.html', {
        'form': form,
        })

#Activating new users using tokens and an email
def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and authenticationToken.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        #Using django console backend
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('emailsuccess')
    else:
        return render(request, 'authInvalid.html')


def authEmailSent(request):
    return render(request, 'authEmailSent.html')

#View to change players to developers
@login_required
def developer(request):
    user = request.user
    user.profile.developer = True
    user.save()
    return render(request, 'statusUpdated.html')
