import json

from .models import *


def get_info():
    queryset_seller = Seller.objects.all()
    queryset_deal = Deal.objects.all()
    result = []
    for seller in queryset_seller:
        deals = queryset_deal.filter(seller=seller)
        customers = [deal.customer.name for deal in deals]
        purchase_sum = sum([deal.get_sum_deal() for deal in deals])
        result.append([seller.name, customers, purchase_sum])
        
    return json.dumps(result, indent=4, default=str)
