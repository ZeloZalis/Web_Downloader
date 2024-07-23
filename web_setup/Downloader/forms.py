from django import forms

class FormularioContacto(forms.Form):
    # Por defecto el formulario se formatea como una tabla.
    # Por defecto todos los campos son requeridos.
    web = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()

    # Para cambiar el formato en el shell se haría un print de la siguiente manera:
    # >>> print(variable.as_p())
    # Siendo <p> un párrafo.
    # Con el método is_valid() podemos ver si los datos ingresados son válidos
    # con .cleaned_data podemos ver la información del formulario