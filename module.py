import module_test
module_test.price(3) # 3명의 영화 가격
module_test.price_morning(4) # 4명의 조조 할인 가격
module_test.price_soldier(7) # 7명의 군인 할인 가격

print("")

import module_test as movie
movie.price(3) # 3명의 영화 가격
movie.price_morning(4) # 4명의 조조 할인 가격
movie.price_soldier(7) # 7명의 군인 할인 가격

print("")

from module_test import *
price(3) # 3명의 영화 가격
price_morning(4) # 4명의 조조 할인 가격
price_soldier(7) # 7명의 군인 할인 가격

print("")

from module_test import price, price_morning
price(3)
price_morning(4)
# price_soldier(7) 사용불가 