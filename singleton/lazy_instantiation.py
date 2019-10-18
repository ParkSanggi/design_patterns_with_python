class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created:", self.get__instance())

    @classmethod
    def get__instance(cls):
        # 모듈이 임포트 될 때 바로 객체가 필요하지 않은 경우 객체를 생성하지 않고
        # 객체가 필요해서 클래스가 호출되었을 때 get_instance를 통해 객체를 만든다.
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print("Object created", Singleton.get__instance())
s1 = Singleton()
