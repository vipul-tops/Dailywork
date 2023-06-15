#Ability to take one name having different form

class Bird:

    def intro(self):
        print("There are many types of Birds")

    def flight(self):
        print("Most Of bird can fly but some cannot fly")

class Sparrow(Bird):

    def flight(self):
        print("Sparrow can fly")

class Pegovin(Bird):

    def flight(self):
        print("Pegovin cannot fly")

obj_bird=Bird()
obj_spr=Sparrow()
obj_pgv=Pegovin()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_pgv.intro()
obj_pgv.flight()
