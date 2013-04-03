from registration.backends.default import DefaultBackend
from yacaptcha.forms import RegistrationFormCaptcha


class CaptchaDefaultBackend(DefaultBackend):
    def get_form_class(self, request):
        return RegistrationFormCaptcha
