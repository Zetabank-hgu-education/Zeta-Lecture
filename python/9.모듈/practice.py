#1-1 module
import theater_module
theater_module.price(3) #3명에서 영화보러 갔을 때 가격
theater_module.price_morning(4) #4명에서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) #5명의 국인이 영화 보러 갔을 때

import theater_module as mv #theater_module을 mv로 간추려서 호출 가능
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * #theater_module 없이 이 모듈을 모두 사용하겠다
price(3)
price_morning(4)
price_soldier(5)

#1-2 package

import travel.thailand # 맨뒤에 thailand부분에는 모듈이나 패키지만 가능 
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from을 이용하면 class나 함수를 바로 이용 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel1 import * #travel이라는 폴더안에있는 모든 패키지를 사용한다는 것 
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#1-4
import inspect
import random
print(inspect.getfile(random))

# 1-5
from travel1 import * 
import inspect
print(inspect.getfile(thailand))
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 1-6
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 

#/ 실제로는 개발자가 공개범위를 설정해줘야함 / 공개하고싶은것은 import 가능