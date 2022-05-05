from django.urls import path

from .views import (
    ShopList,
    ShopDetail,
    ShopCreate,
    ShopUpdate,
    ShopDelete,
    PetList,
    PetDetail,
    PetCreate,
    PetUpdate,
    PetDelete,
    PetSearch,
    CustomerList,
    CustomerDetail,
    CustomerCreate,
    CustomerUpdate,
    CustomerDelete,
    ItemList,
    ItemDetail,
    ItemCreate,
    ItemUpdate,
    ItemDelete,
    ItemSearch,
    POrderList,
    POrderDetail,
    POrderCreate,
    POrderUpdate,
    POrderDelete,
    ContainsList,
    ContainsDetail,
    ContainsCreate,
    ContainsUpdate,
    ContainsDelete,
    query1,
    query2,
    sp,
)


urlpatterns = [

    path(
        'shop/',
        ShopList.as_view(),
        name='petshop_shop_list_url'
    ),

    path(
        'shop/<int:pk>/',
        ShopDetail.as_view(),
        name='petshop_shop_detail_url'
    ),

    path(
        'shop/create/',
        ShopCreate.as_view(),
        name='petshop_shop_create_url'
    ),

    path(
        'shop/<int:pk>/update/',
        ShopUpdate.as_view(),
        name='petshop_shop_update_url'
    ),

    path(
        'shop/<int:pk>/delete/',
        ShopDelete.as_view(),
        name='petshop_shop_delete_url'
    ),

    path(
        'pet/',
        PetList.as_view(),
        name='petshop_pet_list_url'
    ),

    path(
        'pet/<int:pk>/',
        PetDetail.as_view(),
        name='petshop_pet_detail_url'
    ),

    path(
        'pet/create/',
        PetCreate.as_view(),
        name='petshop_pet_create_url'
    ),

    path(
        'pet/<int:pk>/update/',
        PetUpdate.as_view(),
        name='petshop_pet_update_url'
    ),

    path(
        'pet/<int:pk>/delete/',
        PetDelete.as_view(),
        name='petshop_pet_delete_url'
    ),

    path(
        'pet/search/',
        PetSearch.as_view(),
        name='petshop_pet_search_url'
    ),

    path(
        'customer/',
        CustomerList.as_view(),
        name='petshop_customer_list_url'
    ),

    path(
        'customer/<int:pk>/',
        CustomerDetail.as_view(),
        name='petshop_customer_detail_url'
    ),

    path(
        'customer/create/',
        CustomerCreate.as_view(),
        name='petshop_customer_create_url'
    ),

    path(
        'customer/<int:pk>/update/',
        CustomerUpdate.as_view(),
        name='petshop_customer_update_url'
    ),

    path(
        'customer/<int:pk>/delete/',
        CustomerDelete.as_view(),
        name='petshop_customer_delete_url'
    ),

    path(
        'item/',
        ItemList.as_view(),
        name='petshop_item_list_url'
    ),

    path(
        'item/<int:pk>/',
        ItemDetail.as_view(),
        name='petshop_item_detail_url'
    ),

    path(
        'item/create/',
        ItemCreate.as_view(),
        name='petshop_item_create_url'
    ),

    path(
        'item/<int:pk>/update/',
        ItemUpdate.as_view(),
        name='petshop_item_update_url'
    ),

    path(
        'item/<int:pk>/delete/',
        ItemDelete.as_view(),
        name='petshop_item_delete_url'
    ),

    path(
        'item/search/',
        ItemSearch.as_view(),
        name='petshop_item_search_url'
    ),

    path(
        'order/',
        POrderList.as_view(),
        name='petshop_order_list_url'
    ),

    path(
        'order/<int:pk>/',
        POrderDetail.as_view(),
        name='petshop_order_detail_url'
    ),

    path(
        'order/create/',
        POrderCreate.as_view(),
        name='petshop_order_create_url'
    ),

    path(
        'order/<int:pk>/update/',
        POrderUpdate.as_view(),
        name='petshop_order_update_url'
    ),

    path(
        'order/<int:pk>/delete/',
        POrderDelete.as_view(),
        name='petshop_order_delete_url'
    ),

    path(
        'contains/',
        ContainsList.as_view(),
        name='petshop_contains_list_url'
    ),

    path(
        'contains/<int:pk>/',
        ContainsDetail.as_view(),
        name='petshop_contains_detail_url'
    ),

    path(
        'contains/create/',
        ContainsCreate.as_view(),
        name='petshop_contains_create_url'
    ),

    path(
        'contains/<int:pk>/update/',
        ContainsUpdate.as_view(),
        name='petshop_contains_update_url'
    ),

    path(
        'contains/<int:pk>/delete/',
        ContainsDelete.as_view(),
        name='petshop_contains_delete_url'
    ),

    path(
        'sp/',
        sp,
        name='sp'
    ),

    path(
        'query1/',
        query1,
        name='query1'
    ),

    path(
        'query2/',
        query2,
        name='query2'
    ),

]
