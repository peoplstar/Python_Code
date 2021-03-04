import travel_package.thailand # class나 함수를 직접 import 할수 없다.

trip_to = travel_package.thailand.ThailandPackage()
trip_to.detail()

from travel_package.vietnam import VietnamPackage # from import 구문은 사용 가능
trip_to = VietnamPackage()
trip_to.detail()

from travel_package import vietnam # from import 구문은 사용 가능
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel_package import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_2 = thailand.ThailandPackage()
trip_2.detail()
