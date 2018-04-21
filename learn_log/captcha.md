[django-simple-captcha](http://django-simple-captcha.readthedocs.io/en/latest/usage.html)

## install
Install django-simple-captcha via pip: 

```
pip install  django-simple-captcha
```

Add **captcha** to the **INSTALLED_APPS** in your settings.py

Run python manage.py migrate

Add an entry to your urls.py:
```
urlpatterns += [
    url(r'^captcha/', include('captcha.urls')),
]
```

## Define the Form

```
from django import forms
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    myfield = AnyOtherField()
    captcha = CaptchaField()
```

## Init the Captcha-Form

```
def some_view(request):
    form = CaptchaTestForm()
    return render_to_response('template.html',locals())

```

## Amend Template

see the **captcha_test/templates/polls/detail.html**
```
    {{ form.captcha.errors }}
    {{ form.captcha }}
```

## Validate the Form

```
def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('template.html',locals())
```

## Ajax refresh 

Add to the template,
see the **captcha_test/templates/polls/detail.html**
```
<script src="{% static 'polls/jquery-3.3.1.min.js' %}" type="application/javascript"></script>
<script type="application/javascript">
    $('.captcha').click(function () {
        console.log('click');
        $.getJSON("/captcha/refresh/", function (result) {
            $('.captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['key'])
        });


    });
</script>
```
