class Robot:
    def __init__(self, name):
        self.name = name
        self.is_healthy = True

    def get_cold(self):
        print(f"{self.name} catches a virtual cold!")
        self.is_healthy = False

    def display_health_status(self):
        if self.is_healthy:
            print(f"{self.name} is in optimal condition.")
        else:
            print(f"{self.name} is under the weather. Time to apply some virtual antivirus!")

# Example usage:
robot1 = Robot("RoboFriend")
robot1.display_health_status()

robot1.get_cold()
robot1.display_health_status()