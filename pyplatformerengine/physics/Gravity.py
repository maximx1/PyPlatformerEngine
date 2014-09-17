class Gravity:
    G = 6.67384e-11
    
    def apply_gravity_to_floor(self, accel, gravitable):
        print("TODO")
        
    def determine_force_between_objects(self, gravitable1, gravitable2, distanceScale):
        r = self.calculate_distance(distanceScale, gravitable1.rect, gravitable2.rect)
        return (self.G * gravitable1.mass * gravitable2.mass) / (r ** 2)
    
    def calculate_distance(self, distanceScale, rect1, rect2):
        distance = ((((rect1.x - rect2.x) ** 2) + ((rect1.y - rect2.y) ** 2)) ** .5)
        # need m/pixel passed in. 
        return distance * distanceScale