class Vector:
    def __init__(self, components: list):
        self.__components = components
        self.__dim = len(components)

    @property
    def components(self) -> list:
        return self.__components

    @components.setter
    def components(self, values: list) -> None:
        self.__components = values
    
    @property
    def dim(self) -> int:
        return self.__dim


    def __repr__(self) -> str:
        result = "Vector("
        for i in range(len(self.__components)):
            if i == 0:
                result += f"{self.__components[0]}"
            else:
                result += f", {self.__components[i]}"
        result += ")"
        return result

    def __add__(self, other: "Vector") -> "Vector":
        return Vector([a+b for a, b in zip(self.__components, other.__components)])
    
    def __sub__(self, other: "Vector") -> "Vector":
        return Vector([a-b for a, b in zip(self.__components, other.__components)])
        
    def __mul__(self, value: int | float) -> "Vector":
        return Vector([c * value for c in self.__components]) 
    
    def __rmul__(self, value: int | float) -> "Vector":
        return self.__mul__(value)

    def norm(self) -> float:
        return sum(c*c for c in self.__components) ** 0.5


if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([9, 8, 7])
    print(f"Vector 1 = {v1}")
    print(f"Vector 2 = {v2}")
    print("---------------------")
    print(v1 + v2)
    print(v1.norm())
