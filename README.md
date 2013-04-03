=====
Django YaCaptcha
=====

Django YaCaptcha - Yandex Captcha (cleanweb) form field/widget integration app.

Quick start
-----------

1. Add "yacaptcha" to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (
	      'yacaptcha',
      )

2. Get the API key http://api.yandex.ru/cleanweb

3. Add to your project settings:

      YACAPTCHA_KEY = 'your_api_key'

4. Add YaCaptchaField in your form like this::

      from yacaptcha.fields import YaCaptchaField
      class TestForm(forms.Form):
          name = forms.CharField()
          captcha = YaCaptchaField()

5. Add form field widget template

    You may create your own template for field widget. For this add in project settings:
        YACAPTCHA_WIDGET_TEMPLATE = 'path_to_widget.html'

    Or use default widteg.html from package django-yacaptcha/templates/yacaptcha/widget.html

6. If you use django-registration, you may use registartion backend with yacaptcha field like this:
    
    url(r'^accounts/', include('yacaptcha.backends.default.urls')), # yacaptcha backend for registration form
    (r'^accounts/', include('registration.backends.default.urls')),