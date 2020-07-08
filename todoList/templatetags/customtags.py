from django import template
from todoList.models import noteModel
register = template.Library()

# Buyer Order List Fetching
# @register.filter(name='starNotes')
# def starNotes(orderID):
#     basketOrderItems = buyerBasket.objects.filter(buyerBasketOrderID=orderID)
#     return basketOrderItem