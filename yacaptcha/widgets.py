from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from cleanweb import Cleanweb

DEFAULT_WIDGET_TEMPLATE = 'yacaptcha/widget.html'
WIDGET_TEMPLATE = getattr(settings, "YACAPTCHA_WIDGET_TEMPLATE", DEFAULT_WIDGET_TEMPLATE)


class YaCaptcha(forms.widgets.Widget):
    def __init__(self, key=None, *args, **kwargs):
        self.key = key if key else settings.YACAPTCHA_KEY
        super(YaCaptcha, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        client = Cleanweb(key=self.key)
        cap_dict = client.get_captcha()
        return render_to_string(DEFAULT_WIDGET_TEMPLATE,
                                {'yacaptcha_img_url': cap_dict['url'],
                                 'yacaptcha_response_field': cap_dict['captcha']
                                })

    def value_from_datadict(self, data, files, name):
        return [data.get('yacaptcha_challenge_field', None), data.get('yacaptcha_response_field', None)]