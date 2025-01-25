name = "Musa"
lastName = "Hassuna"
s = f"Hello {name} {lastName}!"
# print(s)
# prints: Hello Alex!
date = "2011-03-02"
username = "root"
ip = "10.0.0.3"
# print(f"(Last login at {date} by {username} from {ip})")

department = "Sales"
# print(f"| {date:>25} | Name: {name:20} | Department: {department:15} |")
print(f"| {date}     | Name: {name:20} | Department: {department:15} |")
print(f"Each player should pay: {10 / 3:.2f} NIS.")
print(f"Each player should pay: {10 / 3:.3f} NIS.")
x = 7738.22928
print(f"Result: {x:010.3f}")
print(f"Result: {x:011.3f}")

speed = 299792458
print(f"The speed of light is {speed:,} m/s.")
