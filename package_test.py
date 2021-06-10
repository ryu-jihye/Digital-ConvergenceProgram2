from travel import Thailand
import travel.Thailand
trip_to = travel.Thailand.ThailandPackage()
trip_to.detail()

from travel.Thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import Vietnam
trip_to = Vietnam.VietnamPackage()
trip_to.detail()

from travel import *
# trip_to = Vietnam.VietnamPackage()
trip_to = Thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(Thailand))