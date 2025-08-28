import turtle
import random

# Set up the screen with a beautiful gradient backround
screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("#ffffff")
screen.title("Beautiful Turtle Graphic Artist")

# Creat a turtle object with enhanced styling
t = turtle.Turtle()
t.shape("turtle")
t.speed(4)
t.pensize(2)

# Beautifu color palette 
colors =[ "#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57",
    "#ff9ff3", "#54a0ff", "#5f27cd", "#00d2d3", "#ff9f43",
    "#10ac84", "#ee5a24", "#0abde3", "#ff3838", "#ff6348"]

def get_random_color():
    """Get a random beautiful color"""
    return random.choice(colors)

def setup_turtle_color():
    """Set turtle to a random beautiful color"""
    color = get_random_color()
    t.pencolor(color)
    t.fillcolor(color)
    return color

def draw_square(size):
    """Draw a beautiful filled squar with gradient effect"""
    color = setup_turtle_color()
    t.begin_fill()
    for i in range(4): 
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_triangle(size):
    """Draw a beautiul filled triangle"""
    color = setup_turtle_color()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_circle(radius):
    """Draw a beautiful filled circle"""
    color = setup_turtle_color()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_polygon(sides, size):
    """Draw a beautiful filled polygon"""
    color = setup_turtle_color()
    angle = 360 / sides
    t.begin_fll()
    for i in range(sides):
        t.forwards(size)
        t.left(angle)
    t.end_fill()

def draw_star(size):
    """Draw a beautiful star"""
    color = setup_turtle_color()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def draw_spiral():
    """Draw a beautiful spiral"""
    color = setup_turtle_color()
    for i in range(100):
        t.pencolor(colors[i % len(colors)])
        t.forward(i * 2)
        t.right(121)

def draw_rainbow():
    """Draw a beautiful rainbow"""
    rainbow_colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#9400d3"]
    for i, color in enumerate(rainbow_colors):
        t.pencolor(color)
        t.pensize(5)
        t.circle(100 - i * 10, 180)
        t.pensize(3)

def draw_flower():
    """Draw a beautiful flower with petals"""
    color = setup_turtle_color()
    t.begin_fill()
    for _ in range(36):
        t.circle(50, 60)
        t.left(120)
        t.circle(50, 60)
        t.left(120)
        t.left(10)
    t.end_fill()
    
    # Add center
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pencolor("#ffd700")
    t.fillcolor("#ffd700")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def draw_spiral():
    """Draw a beautiful spiral"""
    color = setup_turtle_color()
    for i in range(100):
        t.pencolor(colors[i % len(colors)])
        t.forward(i * 2)
        t.right(121)

def draw_rainbow():
    """Draw a beautiful rainbow"""
    rainbow_colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#9400d3"]
    for i, color in enumerate(rainbow_colors):
        t.pencolor(color)
        t.pensize(5)
        t.circle(100 - i * 10, 180)
        t.pensize(3)

def main_menu():
    """Display a beautiful main menu"""
    print("\n" + "="*60)
    print(" BEAUTIFUL TURTLE GRAPHICS ARTIST  ")
    print("="*60)
    print("Available shapes:")
    print("1. Square     ")
    print("2. Triangle   ")
    print("3. Circle     ")
    print("4. Polygon    ")
    print("5. Star       ")
    print("6. Flower     ")
    print("7. Spiral     ")
    print("8. Rainbow    ")
    print("9. Random     ")
    print("0. Exit       ")
    print("="*60)

def draw_shape():
    """Enhanced main function with beautiful menu"""
    while True:
        main_menu()
        choice = input("Enter your choice (0-9): ").strip()
        
        if choice == "0":
            print(" Goodbye! Thanks for creating beautiful art!")
            break
        elif choice == "1":
            size = int(input("Enter the size of the square: "))
            draw_square(size)
        elif choice == "2":
            size = int(input("Enter the size of the triangle: "))
            draw_triangle(size)
        elif choice == "3":
            radius = int(input("Enter the radius of the circle: "))
            draw_circle(radius)
        elif choice == "4":
            sides = int(input("Enter the number of sides of the polygon: "))
            size = int(input("Enter the size of the polygon: "))
            draw_polygon(sides, size)
        elif choice == "5":
            size = int(input("Enter the size of the star: "))
            draw_star(size)
        elif choice == "6":
            draw_flower()
        elif choice == "7":
            draw_spiral()
        elif choice == "8":
            draw_rainbow()
        elif choice == "9":
            # Random shape
            shapes = [draw_square, draw_triangle, draw_circle, draw_polygon, draw_star, draw_flower, draw_spiral, draw_rainbow]
            random_shape = random.choice(shapes)
            if random_shape in [draw_square, draw_triangle, draw_polygon, draw_star]:
                size = random.randint(50, 150)
                random_shape(size)
            elif random_shape == draw_circle:
                radius = random.randint(30, 100)
                random_shape(radius)
            else:
                random_shape()
        else:
            print(" Invalid choice! Please try again.")
        
        # Reset turtle position for next drawing
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(0)

# Run the enhanced shape drawing function
if __name__ == "__main__":
    print(" Welcome to the Beautiful Turtle Graphics Artist! ")
    draw_shape()
    
    # Keep the window open
    print(" Click on the graphics window to close it!")
    turtle.done()