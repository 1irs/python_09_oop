class Vehicle:

    def __init__(self, ves_kuzova, car_type, passenger_count, gruzopod):
        self.ves_kuzova = ves_kuzova
        self.car_type = car_type
        self.passenger_count = passenger_count
        self.gruzopod = gruzopod

    def get_total_weight(self):
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod
        if self.car_type == 'car':
            return self.ves_kuzova + self.passenger_count * 80.0
        elif self.car_type == 'truck':
            return self.ves_kuzova + self.gruzopod


car1 = Vehicle(ves_kuzova=1500.0, car_type='car', passenger_count=5, gruzopod=0.0)
tr1 = Vehicle(ves_kuzova=5000.0, car_type='truck', passenger_count=0, gruzopod=7500.0)

print(car1.get_total_weight()+tr1.get_total_weight())
