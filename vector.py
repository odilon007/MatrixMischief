class Vector:
    def __init__(self, components):
        self.__components = components

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, values):
        self.__components = values

    def __repr__(self):
        result = "Vetor("
        for i in range(len(self.__components)):
            if i == 0:
                result += f"{self.__components[0]}"
            else:
                result += f", {self.__components[i]}"
        result += ")"
        return result

    def __add__(self, other):
        resultant = []
        for a, b in zip(self.__components, other.components):
            resultant.append(a+b)

        resultant = Vector(resultant)
        return f"Resultant Vector = {resultant}"
        


if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([9, 8, 7])
    print(f"Vector 1 = {v1}")
    print(f"Vector 2 = {v2}")
    print("---------------------")
    print(v1 + v2)
