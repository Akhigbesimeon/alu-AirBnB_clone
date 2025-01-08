class City:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        return f"City: {self.name}, Description: {self.description}"

    def update_description(self, new_description):
        self.description = new_description

# Test the functionality with a simple print
if __name__ == "__main__":
    city = City("Free WiFi", "High-speed internet access")
    print(City.display_info())
