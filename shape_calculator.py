class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    return f"{'*'*self.width}\n" * self.height if self.height <= 50 and self.width <= 50 else "Too big for picture."

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.width = height
    self.height = height
