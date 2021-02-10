from django import forms
from django.core import validators

class FormCourse(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Put a name',
                'class': 'titulo_form_articulo'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El título tiene caracteres inválidos','titulo_invalido')
        ]
    )

    contenido = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(500,'Superaste el límite de caracteres')
        ]        
    )
    contenido.widget.attrs.update({
        'placeholder': 'Ingrese el contenido del artículo',
        'class': 'contenido_form_articulo',
        'id':'contenido_form'
    })

    opciones_publicado = [
        (1,'Si'),
        (0,'No'),
    ]