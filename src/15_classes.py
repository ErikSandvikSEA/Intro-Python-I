# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


sample = LatLon(2, 4)
print(sample.lat, sample.lon)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"Waypoint: {self.name}, lat: {self.lat}, lon: {self.lon}"


waypointSample = Waypoint("Tokyo", 22, 33)
print(waypointSample.name, waypointSample.lat, waypointSample.lon)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"Geocache: {self.name}, difficulty: {self.difficulty}, size: {self.size}, lat: {self.lat}, lon: {self.lon}"


Geocache_sample = Geocache("WA", "Hard", "Large", 22, 23)
print(
    Geocache_sample.name,
    Geocache_sample.difficulty,
    Geocache_sample.size,
    Geocache_sample.lat,
    Geocache_sample.lon,
)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
catacombs = Waypoint("Catacombs", 41.70505, -121.51521)
print(catacombs)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)


# Make a new geocache "Newberry Views", dfiff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

newberry_views = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
# print(geocache)
print(newberry_views)
