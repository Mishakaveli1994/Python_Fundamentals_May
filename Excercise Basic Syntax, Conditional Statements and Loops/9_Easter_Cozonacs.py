budget = float(input())
flour_price = float(input())
egg_pack_price = 0.75 * flour_price
milk_price = (flour_price + flour_price * 0.25) * 0.25
total_price_for_coz = egg_pack_price + flour_price + milk_price
colored_eggs = 0
cozonacs = 0
while budget >= total_price_for_coz:
    budget -= total_price_for_coz
    colored_eggs += 3
    cozonacs += 1
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2
print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")