coffee_name="coffee"
coffee_price=3.50
coffee_qty=2
coffee_total=coffee_price*coffee_qty

muffin_name="Muffin"
muffin_price=2.10
muffin_qty=3
muffin_total=muffin_price*muffin_qty

water_name="water"
water_price=1.05
water_qty=4
water_total=water_price*water_qty

subtotal=coffee_total+muffin_total+water_total
tax=subtotal*0.06
total=subtotal+tax

print(
    f"========== RECEIPT ==========",
    f"\nItem\tPrice\tqty\tTotal",
    f"\n{coffee_name}\t{coffee_price}\t{coffee_qty}\t{coffee_total}",
    f"\n{muffin_name}\t{muffin_price:.2f}\t{muffin_qty}\t{muffin_total:.2f}",
    f"\n{water_name}\t{water_price}\t{water_qty}\t{water_total}",
    f"\n------------------------------",
    f"\nsubtotal\t{subtotal}",
    f"\ntax (6%)\t{tax}",
    f"\nTotal\t{total}",
    f"\n==============================",
)