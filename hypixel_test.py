""" This is an example of how you can use this API to create cool things.
    Just run this and you should see cool stuff. c:"""

import hypixel

API_KEYS = ['b3d431cd-5bac-4cc1-87b2-f47cc0c8664a']
# API_KEYS = ['b3d431cd-5bac-4cc1-87b2-f47cc0c7664a']
hypixel.setKeys(API_KEYS)  # This sets the API keys that are going to be used.

auction_manager = hypixel.Auction()
auction_info = auction_manager.getAuctionInfo(0)
print(f"{type(auction_info['auctions']) = }\n\n")
print(
    f"page = {auction_info['page']}\n\ntotalPages = {auction_info['totalPages']}\n\ntotalAuctions = {auction_info['totalAuctions']}\n")
print(list(auction_info['auctions'][0].keys()))
print("\n\n".join([str(i) for i in auction_info['auctions']]))
print(f"{len(auction_info['auctions']) = }")

# bazaar_info = hypixel.getJSON("skyblock/bazaar")
# bazaar_products = bazaar_info['products']
# bazaar_items = list(bazaar_products.keys())
# products = {}
# stat_types = ["sellPrice", "sellVolume", "sellMovingWeek", "sellOrders", "buyPrice", "buyVolume", "buyMovingWeek", "buyOrders"]
# for i in bazaar_items:
#     quick_status = bazaar_products[i]["quick_status"]
#     products[i] = {j: round(quick_status[j], 1) for j in stat_types}

# print(products)
# print(hypixel.getJSON("skyblock/news"))
