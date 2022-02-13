# 스택과 힙(메모리 안에서 존재)
# 변수 전달, 값에 의한 호출(call by value), 값에 의한 전달(pass by value)
# 해시코드 : 객체를 힙이라는 영역에다가 만들때, 16진수의 형태로 메모리의 주소가 0xabc190 -> 10진수 형태의 정수값(유니크) 
# 즉, 해시코드는 객체를 구분할 수 있는 유니크한 정수값을 의미

# 리스트 = [ ], 변경이 가능한 객체(mutable object), 오브젝트(객체)에 각각의 주소를 가지고 있음.
# 리스트의 경우에 리스트의 참조(주소)값이 전달.
# 함수에서 참조값을 이용하여 리스트를 변경하면 리스트는 변경 가능하기 때문에,
# 새로운 객체를 생성하지 않고 기존의 객체가 변경된다. (Call by reference=Call by objective)


#-------------------------------------#
# 값에 의한 호출(Call by Value), 값에 의한 전달(Pass by value)
# 은 동일한 개념이다.
# 함수를 호출할 떄, 값이 복사가 되어진다.(중요)
# 호출한 곳에 영향을 끼치지 않는다.
# 숫자 객체는 변경될 수 없는 immutable object 이다.

def change(num):
    print("change()내 연산 전의 num값 : ", num)
    print("change()내 연산 전의 num의 주소(id) : ", id(num))
    num = num + 10
    print("change()내 연산 후의 num값 : ", num)
    print("change()내 연산 후의 num의 주소(id) : ", id(num))
    return num
# 파이썬에서는 모든 값들이 객체로 이루어져 있다.
n = 100
# id() 함수는 매개변수 값으로 객체를 받아서,
# 그 객체의 고유한 주소값을 반환해주는 함수이다.
print("호출 전 n의 주소(id) : ", id(n))
print("호출 전 n의 값 : ", n)
x = change(n)
print("호출 후 x의 값 : ", x)
print("호출 후 x의 주소(id) : ", id(x))
print("호출 후 n의 값 : ", n)
print("호출 후 n의 주소(id) : ", id(n))