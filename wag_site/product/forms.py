from django import forms
from django.shortcuts import render
from django.views.generic import FormView
from .models import Product_Requst_form

# إنشاء نموذج form مرتبط بالنموذج Product_Requst_form
class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = Product_Requst_form
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message', 'agree_to_policy']

# إنشاء view لعرض النموذج
class ProductRequestFormView(FormView):
    template_name = 'product_detail_page.html'  # اذهب إلى القالب المناسب
    form_class = ProductRequestForm
    success_url = '/success/'  # صفحة النجاح بعد إرسال النموذج

    def form_valid(self, form):
        form.save()  # حفظ النموذج بعد إرساله بنجاح
        return super().form_valid(form)

# لا تنسى إضافة URL لهذا الـ View في ملف urls.py