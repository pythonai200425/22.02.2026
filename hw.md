# Python OOP Exercise – Space Mission Control 🚀

<img src="space.png" />

Create a class called `SpaceShip`

The level of this exercise should match the WeatherReport example you saw — including:

* `__init__`
* private attribute
* property + setter
* static method
* class method
* regular instance method
* class members
* creating a few instances

## Part 1 – Class Structure

Create the class `SpaceShip` with the following:

### Class Members (class variables) [static]

* `MAX_FUEL = 1000`
* `MIN_FUEL = 0`
* `launch_count = 0`  (counts how many ships launched)

## Part 2 – Constructor

`__init__(self, name, fuel)`

* `name` – spaceship name
* `fuel` – initial fuel amount
* Store fuel as a **private attribute**
* If fuel is above MAX_FUEL → set it to MAX_FUEL
* If fuel is below MIN_FUEL → set it to MIN_FUEL

## Part 3 – Property + Setter

Create a property `fuel`:

* Getter returns the current fuel
* Setter prevents fuel from going below 0 or above MAX_FUEL

## Part 4 – Static Method

Create a static method:

`is_valid_mission(distance)`

Rules:

* If distance < 50 → return False
* If distance > 10000 → return False
* Otherwise → return True

This method should NOT use self or cls.

## Part 5 – Class Method

Create a class method:

`from_emergency_mode(cls, name)`

This should:

* Create a spaceship with fuel = 100
* Return the new instance

## Part 6 – Instance Methods

### 1. `launch(self)`

* If fuel < 100 → print "Not enough fuel to launch"
* Otherwise:

  * Reduce fuel by 100
  * Increase `launch_count`
  * Print "{name} has launched!"

### 2. `refuel(self, amount)`

* Add fuel using the setter logic

### 3. `display_status(self)`

Print:

"Ship: {name} | Fuel: {fuel} | Total Launches: {launch_count}"

## Part 7 – Create Instances

In your main code:

* Create 2 normal ships
* Create 1 ship using `from_emergency_mode`
* Try launching them
* Try invalid fuel values
* Test `is_valid_mission()` with different distances

Good luck 🚀

Submit email: **[pythonai200425+oopclass@gmail.com](mailto:pythonai200425+oopclass@gmail.com)**

