class EventManagr(object):

    def __init__(self):
        print("Event Manager :: Let me talk to the folks\n")

    def arrange(self):
        self.hotelir = Hotelier()
        self.hotelir.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def is_available(self):
        print("Is the hotel free for the event on given day?")
        return True

    def book_hotel(self):
        if self.is_available():
            print("Registed the Booking\n\n")


class Florist(object):

    def __init__(self):
        print("Flower Decorations for teh Event? --")

    def set_flower_requirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations \n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def set_cuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def set_music_type(self):
        print("Jazz and Classical will b playd\n\n")


class You(object):
    def __init__(self):
        print("You ::  Whoa! Marriage Arrangements??!!")

    def ask_event_manager(self):
        print("You:: Let's Contact the vent Manager\n\n")
        em = EventManagr()
        em.arrange()

    def __del__(self):
        print("You :: Thanks to Event Manager, all preparations done!")


if __name__ == "__main__":
    you = You()
    you.ask_event_manager()
