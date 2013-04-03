from yacaptcha.fields import YaCaptchaField

from registration.forms import RegistrationForm, RegistrationFormUniqueEmail


# class RegistrationFormCaptcha(RegistrationForm):
#     captcha = ReCaptchaField(attrs={'theme': 'white'})

class RegistrationFormCaptcha(RegistrationFormUniqueEmail):
    captcha = YaCaptchaField()
