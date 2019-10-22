from abc import ABC, abstractmethod

# 알고리즘의 뼈대를 유지하면서 유연하게 기능을 변경해서 적용할 수 있다.

"""
1. 하나의 추상클래스가 있다.
2. 추상클래스는 template method를 갖는다.
3. template method는 다른 서브클래스에서 호출할 일련의 메소드들을 포함한다.
4. 서브클래스들은 몇몇 메서드들을 오버라이드 할 수 있다.
"""


# 추상클래스
class Pizza(ABC):

    # 템플릿 메서드
    def make_pizza(self):
        self.make_dough()
        self.put_cheese()
        self.put_ingredients()
        self.bake()

        if self.need_delivery():
            self.put_in_a_box()

    def make_dough(self):
        print("반죽을 만든다")

    def put_cheese(self):
        print("치즈를 올린다")

    @abstractmethod
    def put_ingredients(self):
        pass

    def bake(self):
        print("굽는다")

    def need_delivery(self):
        return False

    def put_in_a_box(self):
        pass


class PotatoPizza(Pizza):

    def put_ingredients(self):
        print("감자를 올린다")

    def need_delivery(self):
        return True

    def put_in_a_box(self):
        print("박스에 담는다")


if __name__ == "__main__":
    p = PotatoPizza()
    p.make_pizza()
