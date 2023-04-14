class Dog():
    name: None;
    age: None;
    isHungry: None;

    #construction
    def __init__(self, name, age, isHungry):
        self.name = name;
        self.age = age;
        self.isHungry = isHungry;
        self.owner = owner; 

    def display(self):
        print("***DOG***");
        print("name", self.name);
        print("age", self.age);
        print("is Hungry?", self.isHungry);

    def sound(self):
        print("Woof!");


#Child class   
class DomestiCat(Dog):
    owner: None;


Dog1 = Cat("Alice", 5, True);
Dog2 = Cat("Penny", 5, False);

    
# cat1 = Cat();
# cat1.name = "Peter";
# cat1.age = 5;
# cat1.isHappy = True;
# cat1.display()

# cat2 = Cat();
# cat2.name = "Luna";
# cat2.age = 5;
# cat2.isHappy = False;

cat2.display()
cat2.sound()
