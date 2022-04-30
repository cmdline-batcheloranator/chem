from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Pmv:
    den: Decimal
    vol: Decimal
    mass: Decimal
    
    @property
    def get_vol(self) -> Decimal:                
	    return round(
		   Decimal(
              self.mass
          ) /
          Decimal(
              self.den
          ), 3
        )

    @property
    def get_den(self) -> Decimal:
        return round(
		   Decimal(
              self.mass
          ) *
          Decimal(
              self.vol
          ), 3
        )

    @property
    def get_mass(self) -> Decimal:
         return round(
		    Decimal(
               self.den
           ) /
           Decimal(
               self.vol
			), 3
         )
	
vol = Pmv(6, 0, 2)
print(vol.get_vol)

den = Pmv(0, 3, 4)
print(den.get_den)

mass = Pmv(5, 2, 0)
print(mass.get_mass)
