 Physics Class
You are a physics teacher preparing for the upcoming semester. 
You want to provide your students with some functions that will help them calculate some fundamental physical properties.

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)
#check it
print(f100_in_celsius)


def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies",  + train_force, "Newtons of force")

def get_energy(mass, c):
