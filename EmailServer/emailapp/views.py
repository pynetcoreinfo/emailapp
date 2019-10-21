from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from .forms import EmailForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from emailapp.models import EMailCompose
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class EmailListView(ListView):
    model = EMailCompose
    template_name = 'emailapp/mail_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'email'
    ordering = ['-date_sented']



class UserEmailList(LoginRequiredMixin,ListView):
    model = EMailCompose
    template_name = 'emailapp/user_eamil.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'email'




@login_required()
def send_email(request):    #Mail Create View
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            cc = form.cleaned_data['cc']
            bcc = form.cleaned_data['bcc']
            attach = request.FILES['attach']
            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email,cc,bcc])
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            messages.success(request, f'Mail Sent Successfully !')
            return HttpResponseRedirect(reverse('mail-list'))
            #return redirect(request,'mail-list' )
        form = EmailForm()
        return render(request,'emailapp/email_form.html', {'email_form': form})
       # return render(request,{'message': 'Unable to send email. Please try again later'})

class EmailDetail(LoginRequiredMixin,DetailView):
    model = EMailCompose
    template_name = 'emailapp/emailcompose_detail.html'

"""
class EmailCreat(LoginRequiredMixin, CreateView):
    model = EMailCompose
    fields = ['title','content']

# form_valid() function overriding
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
        messages.success(request, f'Account created for {username}!'
'emailapp/user_eamil.html'
"""







