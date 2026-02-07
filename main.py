from vector import Vector



# Vector 

v1 = Vector([1,2,3])
v2 = Vector([9,8,7])

print(v1) # Vector(1, 2, 3)
print(v2) # Vector(9, 8, 7)
print(v1 + v2) # Vector(10, 10, 10)
print(v2 - v1) # Vector(8, 6, 4)
print(v1 * 2) # Vector(2, 4, 6)
print(3 * v1) # Vector(3, 6, 9)
print(v1.norm()) # 3.741...



