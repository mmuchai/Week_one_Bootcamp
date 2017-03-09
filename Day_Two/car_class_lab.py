class Car(object):

    def __init__(self,car_type,model='GM',name = 'General'):
        self.car_type = str (car_type)
        self.model=str(model)
        self.name=str(name)
        self.num_of_doors = []
        self.num_of_wheels = []
        self.speed = [0]
        self.drive = int(drive)
t
    def car_doors (self):
        for door in self.num_of_doors:
            if (self.name== Porshe or self.name== Koenigsegg):
                self.num_of_doors.append(2)
                return self.num_of_doors
            else:
                self.num_of_doors.append(4)
                return self.num_of_doors
    def car_wheels (self):
        for wheel in self.num_of_wheels:
            if self.car_type=='trailer':
                self.num_of_wheels.append(8)
                return self.num_of_wheels
            else:
                self.num_of_wheels.append(4)
                return self.num_of_wheels

    def car_speed(self):
        if self.car_type == 'trailer':
            self.speed.append ((11 * self.drive))
        else:
            self.speed.append ((10***self.drive))

        if self.speed
toyota = Car('Corolla')
print (toyota.num_of_doors, Porshe.num_of_doors)
print (vars(toyota))