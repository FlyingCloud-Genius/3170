# -*- coding: utf-8 -*-
from django import forms

class InfoForm(forms.Form):
    reg_id = forms.EmailField(label="Email: ", max_length=30)
    reg_password = forms.CharField(label="Password", max_length=16, widget=forms.PasswordInput)