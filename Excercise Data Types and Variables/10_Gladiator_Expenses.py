lostFightCount = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

trashedHelmet = int(lostFightCount / 2)
trashedSword = int(lostFightCount / 3)
trashedShield = int(lostFightCount / 6)
trashedArmor = int(lostFightCount / 12)
totalRepairCosts = trashedHelmet * helmetPrice + trashedSword * swordPrice + trashedShield * shieldPrice + trashedArmor * armorPrice
print(f"Gladiator expenses: {totalRepairCosts:.2f} aureus")
