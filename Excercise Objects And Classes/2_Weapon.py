class Weapon:
    def __init__(self, bulletAmount):
        self.bullets = int(bulletAmount)

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
