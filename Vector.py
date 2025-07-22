import math

class Vector3D:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return "{}i+{}j+{}k".format(self.i, self.j, self.k)

    def get_X(self):
        return self.i

    def get_Y(self):
        return self.j

    def get_Z(self):
        return self.k

    def getItem(self, dimension):
        if dimension == 'i':
            return self.i
        elif dimension == 'j':
            return self.j
        elif dimension == 'k':
            return self.k
        else:
            raise IndexError("Dimension not found")

    def set_X(self, value):
        self.i = value

    def set_Y(self, value):
        self.j = value

    def set_Z(self, value):
        self.k = value

    def setItem(self, dimension, value):
        if dimension == 'i':
            self.i = value
        elif dimension == 'j':
            self.j = value
        elif dimension == 'k':
            self.k = value
        else:
            raise IndexError("Dimension not found")

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.i + other.i, self.j + other.j, self.k + other.k)
        elif isinstance(other, (list, tuple)):
            result = Vector3D(self.i, self.j, self.k)
            for vec in other:
                if not isinstance(vec, Vector3D):
                    raise TypeError("All operands must be instances of Vector3D")
                result = result + vec
            return result
        else:
            raise TypeError("Operand must be Vector3D or list/tuple of Vector3D")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.i - other.i, self.j - other.j, self.k - other.k)
        elif isinstance(other, (list, tuple)):
            result = Vector3D(self.i, self.j, self.k)
            for vec in other:
                if not isinstance(vec, Vector3D):
                    raise TypeError("All operands must be instances of Vector3D")
                result = result - vec
            return result
        else:
            raise TypeError("Operand must be Vector3D or list/tuple of Vector3D")

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            # Cross product
            return Vector3D(
                self.j * other.k - self.k * other.j,
                self.k * other.i - self.i * other.k,
                self.i * other.j - self.j * other.i
            )
        else:
            raise TypeError("Cross product requires another Vector3D")

    def dot_product(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k

    def __abs__(self):
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)

    def __neg__(self):
        x=-1*self.i
        y=-1*self.j
        z=-1*self.k
        return Vector3D(x,y,z)
    
    def __abs_val(self):  # Internal usage
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)

    def __lt__(self, other):
        return self.__abs_val() < other.__abs_val()

    def __le__(self, other):
        return self.__abs_val() <= other.__abs_val()

    def __ne__(self, other):
        return self.__abs_val() != other.__abs_val()

    def __ge__(self, other):
        return self.__abs_val() >= other.__abs_val()

    def __gt__(self, other):
        return self.__abs_val() > other.__abs_val()

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and self.k == other.k

    def __repr__(self):
        return "3D Vector"
    
    def is_ZeroVector(self):
        return self.i == 0 and self.j == 0 and self.k == 0

    def angle_with(self, other):
        dot = self.dot_product(other)
        mag_product = abs(self) * abs(other)
        if mag_product == 0:
            raise ValueError("Cannot calculate angle with a zero vector")
        return math.acos(dot / mag_product)

    def distance_to(self, other):
        return math.sqrt(
            (self.i - other.i)**2 +
            (self.j - other.j)**2 +
            (self.k - other.k)**2
        )

    def __iter__(self):
        yield self.i
        yield self.j
        yield self.k

    def normalize(self):
        magnitude = abs(self)
        if magnitude == 0:
            raise ValueError("Cannot normalize the zero vector")
        return Vector3D(self.i / magnitude, self.j / magnitude, self.k / magnitude)

    def projection_onto(self, other):
        if other.is_ZeroVector():
            raise ValueError("Cannot project onto a zero vector")
        scale = self.dot_product(other) / (abs(other) ** 2)
        return Vector3D(other.i * scale, other.j * scale, other.k * scale)

    def scalar_multiply(self, scalar):
        return Vector3D(self.i * scalar, self.j * scalar, self.k * scalar)

    def to_tuple(self):
        return (self.i, self.j, self.k)

    def rotate_about_axis(self, axis, angle_deg):
        """
        Rotates the vector about the specified axis ('x', 'y', or 'z') by the given angle in degrees.
        """
        angle = math.radians(angle_deg)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        x, y, z = self.i, self.j, self.k

        if axis == 'x':
            return Vector3D(
                x,
                y * cos_a - z * sin_a,
                y * sin_a + z * cos_a
            )
        elif axis == 'y':
            return Vector3D(
                x * cos_a + z * sin_a,
                y,
                -x * sin_a + z * cos_a
            )
        elif axis == 'z':
            return Vector3D(
                x * cos_a - y * sin_a,
                x * sin_a + y * cos_a,
                z
            )
        else:
            raise ValueError("Invalid axis. Use 'x', 'y', or 'z'.")

    def length(self):
        return abs(self)

    def set_length(self, new_length):
        current = self.length()
        if current == 0:
            raise ValueError("Cannot set length for zero vector")
        scale = new_length / current
        return Vector3D(self.i * scale, self.j * scale, self.k * scale)

    def perpendicular(self):
        """
        Returns a perpendicular vector (not unique in 3D).
        This version returns a simple non-parallel perpendicular vector.
        """
        if self.i != 0 or self.j != 0:
            return Vector3D(-self.j, self.i, 0).normalize()
        else:
            return Vector3D(0, -self.k, self.j).normalize()

    


class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return "{}i+{}j".format(self.i, self.j)
    
    def get_X(self):
        return self.i
    
    def get_Y(self):
        return self.j
    
    def getItem(self, dimension):
        if dimension == 'i':
            return self.i
        elif dimension == 'j':
            return self.j
        else:
            raise IndexError("Dimension not found")

    def set_X(self, value):
        self.i = value
    
    def set_Y(self, value):
        self.j = value
    
    def setItem(self, dimension, value):
        if dimension == 'i':
            self.i = value
        elif dimension == 'j':
            self.j = value
        else:
            raise IndexError("Dimension not found")

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.i + other.i, self.j + other.j)
        elif isinstance(other, (list, tuple)):
            result = Vector2D(self.i, self.j)
            for vec in other:
                if not isinstance(vec, Vector2D):
                    raise TypeError("All operands must be instances of Vector2D")
                result = result + vec
            return result
        else:
            raise TypeError("Operand must be Vector2D or list/tuple of Vector2D")

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.i - other.i, self.j - other.j)
        elif isinstance(other, (list, tuple)):
            result = Vector2D(self.i, self.j)
            for vec in other:
                if not isinstance(vec, Vector2D):
                    raise TypeError("All operands must be instances of Vector2D")
                result = result - vec
            return result
        else:
            raise TypeError("Operand must be Vector2D or list/tuple of Vector2D")

    def __mul__(self, other):
        return self.i * other.j - self.j * other.i
    
    def __neg__(self):
        x=-1*self.i
        y=-1*self.j
        return Vector2D(x,y)
    
    def __abs__(self):
        return (self.i ** 2 + self.j ** 2) ** 0.5

    def __abs(self):
        return (self.i ** 2 + self.j ** 2) ** 0.5

    def __lt__(self, other):
        return self.__abs() < other.__abs()

    def __le__(self, other):
        return self.__abs() <= other.__abs()

    def __ne__(self, other):
        return self.__abs() != other.__abs()

    def __ge__(self, other):
        return self.__abs() >= other.__abs()

    def __gt__(self, other):
        return self.__abs() > other.__abs()

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j
    
    def __repr__(self):
        return "2D Vector"
    
    def dot_product(self, other):
        return self.i * other.i + self.j * other.j

    def is_ZeroVector(self):
        return self.i == 0 and self.j == 0

    def angle_with(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be an instance of Vector2D")
        dot = self.dot_product(other)
        mag_product = self.__abs() * other.__abs()
        if mag_product == 0:
            raise ValueError("Cannot calculate angle with a zero vector")
        return math.acos(dot / mag_product)

    def distance_to(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be an instance of Vector2D")
        return ((self.i - other.i) ** 2 + (self.j - other.j) ** 2) ** 0.5

    def __iter__(self):
        yield self.i
        yield self.j


    def normalize(self):
        magnitude = abs(self)
        if magnitude == 0:
            raise ValueError("Cannot normalize the zero vector")
        return Vector2D(self.i / magnitude, self.j / magnitude)

    def projection_onto(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be an instance of Vector2D")
        if other.is_ZeroVector():
            raise ValueError("Cannot project onto a zero vector")
        scale = self.dot_product(other) / (abs(other) ** 2)
        return Vector2D(other.i * scale, other.j * scale)

    def perpendicular(self):
        return Vector2D(-self.j, self.i)

    def scalar_multiply(self, scalar):
        return Vector2D(self.i * scalar, self.j * scalar)

    def to_tuple(self):
        return (self.i, self.j)


#Rotates a vector (e.g. to turn an object’s direction or coordinate frame).
#(x', y') = (x cosθ - y sinθ, x sinθ + y cosθ)
    def rotate(self, angle):
        angle=math.radians(angle)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return Vector2D(self.i * cos_a - self.j * sin_a,
                    self.i * sin_a + self.j * cos_a)

    def angle(self):
        return math.degrees(math.atan2(self.i, self.j))


    def length(self):
        return math.sqrt(self.i*self.i + self.j*self.j)


    def set_length(self, new_length):
        current = self.length()
        if current == 0:
            raise ValueError("Cannot set length for zero vector")
        scale = new_length / current
        return Vector2D(self.i * scale, self.j * scale)

