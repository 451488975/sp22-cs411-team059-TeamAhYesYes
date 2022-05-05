from django import forms

from .models import Customer, Shop, Pet, Item, POrder, Contains


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'discount': forms.HiddenInput(),
        }

    def clean_username(self):
        return self.cleaned_data['username'].strip()

    def clean_password(self):
        return self.cleaned_data['password'].strip()

    def clean_email(self):
        return self.cleaned_data['email'].strip()

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_phone_number(self):
        return self.cleaned_data['phone_number'].strip()

    def clean_recommender_name(self):
        return self.cleaned_data['recommender_name'].strip()


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'

    def clean_shop_name(self):
        return self.cleaned_data['shop_name'].strip()

    def clean_shop_address(self):
        return self.cleaned_data['shop_address'].strip()


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

    def clean_color(self):
        return self.cleaned_data['color'].strip()

    def clean_type(self):
        return self.cleaned_data['type'].strip()

    def clean_breed(self):
        return self.cleaned_data['breed'].strip()


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def clean_item_name(self):
        return self.cleaned_data['item_name'].strip()

    def clean_type(self):
        return self.cleaned_data['type'].strip()


class POrderForm(forms.ModelForm):
    class Meta:
        model = POrder
        fields = '__all__'
        widgets = {
            'transaction_time': forms.HiddenInput(),
            'total_price': forms.HiddenInput(),
        }


class ContainsForm(forms.ModelForm):
    class Meta:
        model = Contains
        fields = '__all__'
