class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            message = 'shooting...'
        else:
            message = 'no bullets left'
        return message

    def __repr__(self):
        return f'Remaining bullets: {self.bullets}'


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)