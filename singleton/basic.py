class Singleton(type):
    def __new__(cls):

        # instance 라는 클래스 변수가 존재하는지 확인한다.
        if not hasattr(cls, 'instance'):

            # 없다면 Singletone의 object를 생성해서 클래스 변수에 할당한다.
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
