from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Pmv:
    den: float
    vol: float
    mass: float
    
    def get_vol(self) -> Decimal:                
        return round(
          Decimal(
              self.mass
          ) /
          Decimal(
              self.den
          ), 2
        )

    def get_den(self) -> Decimal:
        return round(
          Decimal(
              self.mass
          ) *
          Decimal(
              self.vol
          ), 2
        )

    def get_mass(self) -> Decimal:
         return round(
           Decimal(
               self.den
           ) /
           Decimal(
               self.vol
           ), 2
         )
    
vol = Pmv(6.2, 0, 2.1)
print(vol.get_vol())

den = Pmv(0, 3.1, 4.8)
print(den.get_den())

mass = Pmv(8.9, 2.2, 0)
print(mass.get_mass())
