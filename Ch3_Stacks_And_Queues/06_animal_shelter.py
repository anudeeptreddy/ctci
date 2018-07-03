import Queue


class AnimalShelter:
    def __init__(self):
        self.cats = Queue.Queue()
        self.dogs = Queue.Queue()
        self.counter = 1

    def __str__(self):
        cats = 'Cats: %s' % ' '.join([str(x.timestamp) for x in animals.cats.queue])
        dogs = 'Dogs: %s' % ' '.join([str(x.timestamp) for x in animals.dogs.queue])
        return '\n'.join([cats, dogs])

    def enqueue(self, animal):
        animal.timestamp = self.counter
        if animal.__class__ == Cat:
            self.cats.put(animal)
        else:
            self.dogs.put(animal)
        self.counter += 1

    def dequeue_any(self):
        cats_timestamp = self.cats.queue[0].timestamp if not self.cats.empty() else 0
        dogs_timestamp = self.dogs.queue[0].timestamp if not self.dogs.empty() else 0
        return self.cats.get() if cats_timestamp > dogs_timestamp else self.dogs.get()

    def dequeue_dog(self):
        return self.dogs.get()

    def dequeue_cat(self):
        return self.cats.get()


class Animal:
    def __init__(self, timestamp=None):
        self.timestamp = timestamp


class Cat(Animal):
    pass


class Dog(Animal):
    pass


if __name__ == '__main__':
    animals = AnimalShelter()
    animals.enqueue(Cat())
    animals.enqueue(Cat())
    animals.enqueue(Dog())
    animals.enqueue(Cat())
    print animals
    animals.dequeue_cat()
    print animals
    animals.enqueue(Dog())
    print animals
    animals.dequeue_any()
    print animals
    print animals.dequeue_any()
    print animals


# o/p:
#
# Cats: 1 2 4
# Dogs: 3
# Cats: 2 4
# Dogs: 3
# Cats: 2 4
# Dogs: 3 5
# Cats: 2 4
# Dogs: 5
# Cats: 2 4
# Dogs:
