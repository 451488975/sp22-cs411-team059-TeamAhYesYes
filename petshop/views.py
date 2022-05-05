from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomerForm, ShopForm, PetForm, ItemForm, POrderForm, ContainsForm
from .models import Customer, Shop, Pet, Item, POrder, Contains
from .utils import PageLinksMixin


class ShopList(ListView):
    model = Shop


class ShopDetail(DetailView):
    model = Shop

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        shop = self.get_object()
        pet_list = shop.pets.all()
        item_list = shop.items.all()
        context['pet_list'] = pet_list
        context['item_list'] = item_list
        return context


class ShopCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ShopForm
    model = Shop
    permission_required = 'petshop.add_shop'


class ShopUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ShopForm
    model = Shop
    template_name = 'petshop/shop_form_update.html'
    permission_required = 'petshop.change_shop'


class ShopDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Shop
    success_url = reverse_lazy('petshop_shop_list_url')
    permission_required = 'petshop.delete_shop'

    def get(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)
        pets = shop.pets.all()
        items = shop.items.all()
        if pets.count() > 0:
            return render(
                request,
                'petshop/shop_refuse_delete.html',
                {
                    'shop': shop,
                    'left': 1,
                }
            )
        elif items.count() > 0:
            return render(
                request,
                'petshop/shop_refuse_delete.html',
                {
                    'shop': shop,
                    'left': 2,
                }
            )
        else:
            return render(
                request,
                'petshop/shop_confirm_delete.html',
                {'shop': shop}
            )


class PetList(PageLinksMixin, ListView):
    model = Pet
    paginate_by = 25


class PetDetail(DetailView):
    model = Pet

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        pet = self.get_object()
        shop = pet.shop
        customer = pet.customer
        context['shop'] = shop
        context['customer'] = customer
        return context


class PetCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PetForm
    model = Pet
    permission_required = 'petshop.add_pet'


class PetUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PetForm
    model = Pet
    template_name = 'petshop/pet_form_update.html'
    permission_required = 'petshop.change_pet'


class PetDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Pet
    success_url = reverse_lazy('petshop_pet_list_url')
    permission_required = 'petshop.delete_pet'


class PetSearch(View):
    page_kwarg = 'page'
    paginate_by = 25
    template_name = 'petshop/pet_search_result.html'

    def get(self, request):
        keyword = request.GET.get('pet_search')
        pet_list = Pet.objects.filter(
            Q(color__icontains=keyword) |
            Q(breed__icontains=keyword) |
            Q(type__icontains=keyword)
        ).distinct()
        paginator = Paginator(
            pet_list,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?pet_search={kwd}&{pkw}={n}".format(
                kwd=keyword,
                pkw=self.page_kwarg,
                n=page.previous_page_number()
            )
        else:
            prev_url = None
        if page.has_next():
            next_url = "?pet_search={kwd}&{pkw}={n}".format(
                kwd=keyword,
                pkw=self.page_kwarg,
                n=page.next_page_number()
            )
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'pet_list': page,
        }
        return render(
            request, self.template_name, context
        )


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Customer
    paginate_by = 25
    permission_required = 'petshop.view_customer'


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = 'petshop.view_customer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        customer = self.get_object()
        pet_list = customer.pets.all()
        order_list = customer.orders.all()
        context['pet_list'] = pet_list
        context['order_list'] = order_list
        return context


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    model = Customer
    permission_required = 'petshop.add_customer'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'petshop/customer_form_update.html'
    permission_required = 'petshop.change_customer'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('petshop_customer_list_url')
    permission_required = 'petshop.delete_customer'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        pets = customer.pets.all()
        orders = customer.orders.all()
        if pets.count() > 0:
            return render(
                request,
                'petshop/customer_refuse_delete.html',
                {
                    'customer': customer,
                    'pets': pets,
                }
            )
        elif orders.count() > 0:
            return render(
                request,
                'petshop/customer_refuse_delete.html',
                {
                    'customer': customer,
                    'orders': orders,
                }
            )
        else:
            return render(
                request,
                'petshop/customer_confirm_delete.html',
                {'customer': customer}
            )


class ItemList(PageLinksMixin, ListView):
    model = Item
    paginate_by = 25


class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = self.get_object()
        contains_list = item.contains.all()
        shop = item.shop
        context['contains_list'] = contains_list
        context['shop'] = shop
        return context


class ItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ItemForm
    model = Item
    permission_required = 'petshop.add_item'


class ItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ItemForm
    model = Item
    template_name = 'petshop/item_form_update.html'
    permission_required = 'petshop.change_item'


class ItemDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('petshop_item_list_url')
    permission_required = 'petshop.delete_item'

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        contains = item.contains.all()
        if contains.count() > 0:
            return render(
                request,
                'petshop/item_refuse_delete.html',
                {
                    'item': item,
                    'contains': contains,
                }
            )
        else:
            return render(
                request,
                'petshop/item_confirm_delete.html',
                {'item': item}
            )


class ItemSearch(View):
    page_kwarg = 'page'
    paginate_by = 25
    template_name = 'petshop/item_search_result.html'

    def get(self, request):
        keyword = request.GET.get('item_search')
        item_list = Item.objects.filter(
            Q(item_name__icontains=keyword) |
            Q(type__icontains=keyword) |
            Q(shop__shop_name__icontains=keyword)
        ).distinct()
        paginator = Paginator(
            item_list,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?item_search={kwd}&{pkw}={n}".format(
                kwd=keyword,
                pkw=self.page_kwarg,
                n=page.previous_page_number()
            )
        else:
            prev_url = None
        if page.has_next():
            next_url = "?item_search={kwd}&{pkw}={n}".format(
                kwd=keyword,
                pkw=self.page_kwarg,
                n=page.next_page_number()
            )
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'item_list': page,
        }
        return render(
            request, self.template_name, context
        )


class POrderList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = POrder
    template_name = 'petshop/order_list.html'
    permission_required = 'petshop.view_porder'
    paginate_by = 25


class POrderDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = POrder
    template_name = 'petshop/order_detail.html'
    permission_required = 'petshop.view_porder'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        porder = self.get_object()
        contains_list = porder.contains.all()
        customer = porder.customer
        context['contains_list'] = contains_list
        context['customer'] = customer
        return context


class POrderCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = POrderForm
    model = POrder
    template_name = 'petshop/order_form.html'
    permission_required = 'petshop.add_porder'


class POrderUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = POrderForm
    model = POrder
    template_name = 'petshop/order_form_update.html'
    permission_required = 'petshop.change_porder'


class POrderDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = POrder
    success_url = reverse_lazy('petshop_order_list_url')
    permission_required = 'petshop.delete_porder'

    def get(self, request, pk):
        porder = get_object_or_404(POrder, pk=pk)
        contains = porder.contains.all()
        if contains.count() > 0:
            return render(
                request,
                'petshop/order_refuse_delete.html',
                {
                    'porder': porder,
                    'contains': contains,
                }
            )
        else:
            return render(
                request,
                'petshop/order_confirm_delete.html',
                {'porder': porder}
            )


class ContainsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contains
    permission_required = 'petshop.view_contains'


class ContainsDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contains
    permission_required = 'petshop.view_contains'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        contains = self.get_object()
        item = contains.item
        order = contains.order
        context['item'] = item
        context['order'] = order
        return context


class ContainsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ContainsForm
    model = Contains
    permission_required = 'petshop.add_contains'

    def get_success_url(self):
        order = self.object.order
        return reverse_lazy('petshop_order_detail_url', kwargs={'pk': order.pk})


class ContainsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ContainsForm
    model = Contains
    template_name = 'petshop/contains_form_update.html'
    permission_required = 'petshop.change_contains'

    def get_success_url(self):
        order = self.object.order
        return reverse_lazy('petshop_order_detail_url', kwargs={'pk': order.pk})


class ContainsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contains
    permission_required = 'petshop.delete_contains'

    def get_success_url(self):
        order = self.object.order
        return reverse_lazy('petshop_order_detail_url', kwargs={'pk': order.pk})


def sp(request):
    cursor = connection.cursor()
    cursor.callproc('update_discount')

    return render(request, 'petshop/about.html')


def query1(request):
    sql = '''
        (SELECT 
            i.item_id, s.shop_name, i.price
        FROM
            item i
                JOIN
            shop s USING (shop_id)
        WHERE
            i.type = 'Toys'
                AND i.price > (SELECT 
                    AVG(price)
                FROM
                    item
                WHERE
                    shop_id = 1
                GROUP BY shop_id)
        ORDER BY i.price) 
        UNION 
        (SELECT 
            i.item_id, s.shop_name, i.price
        FROM
            item i
                JOIN
            shop s USING (shop_id)
        WHERE
            i.type = 'Food'
                AND i.price > (SELECT 
                    AVG(price)
                FROM
                    item
                WHERE
                    shop_id = 2
                GROUP BY shop_id)
        ORDER BY i.price) 
        LIMIT 15'''
    posts = Item.objects.raw(sql)

    return render(request, 'petshop/output.html', {'data': posts})


def query2(request):
    sql = '''
        SELECT distinct cus.customer_id, 1 as item_id, username, p.order_id
        FROM
            p_order p
                JOIN
            customer cus USING (customer_id)
                JOIN
            contains c ON p.order_id = c.order_id
                JOIN
            item i USING (item_id)
        WHERE
            (transaction_time BETWEEN '2022-02-01' AND '2022-03-31')
                AND item_id IN (SELECT 
                    item_id
                FROM
                    item
                WHERE
                    price > 100)
        order by customer_id
        LIMIT 15'''
    posts = Item.objects.raw(sql)

    return render(request, 'petshop/output2.html', {'data': posts})
