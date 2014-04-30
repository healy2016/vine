#coding:utf-8

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from django.http import HttpResponse

from social.backends.google import GooglePlusAuth

# XXX 如果oauth redirect此处失效
# 下面的oauth认证过程，都采用了HTTP_REFERER作为返回redirect目标
# 如果失效，应该考虑采用session方式，存储浏览器最后访问的页面
# 具体的可以看看django的session方法

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/comment'))
    #return render_to_response('home.html', {}, RequestContext(request))

def comments(request):
    """Home view, displays login mechanism"""
    #if request.user.is_authenticated():
    return redirect('/comments/best')
    return render_to_response('home.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
    }, RequestContext(request))

@login_required
def done(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)

    #print request
    #return render(request, 'refresh_iframe.html')
    return redirect(request.META.get('HTTP_REFERER', '/comment'))
    return render_to_response('done.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))


def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))
