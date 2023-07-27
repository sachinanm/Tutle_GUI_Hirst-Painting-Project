import random
import turtle
import colorgram


# Function to extract colors from an image and return a list of RGB tuples
def extract_colors_from_image(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    return rgb_colors


# Replace 'image.jpg' with the path of your desired image
image_colors = extract_colors_from_image('image.jpg', 30)

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("white")

tim = turtle.Turtle()
tim.speed(0)
tim.hideturtle()

# Set the pen color to a random color from the extracted image colors
center_x = 0
center_y = 0


# Move the turtle to the center position
tim.penup()
tim.goto(center_x, center_y)

current_position_y = 0

# Get input from the user for the number of rows in the pattern
num_rows = int(turtle.numinput("Number of Rows", "Enter the number of rows (even number recommended):", default=10))

# Draw a dot grid using the extracted image colors
for i in range(num_rows):
    for j in range(num_rows):
        tim.dot(10, random.choice(image_colors))
        tim.forward(25)

    current_position_y += 15
    tim.goto(0, current_position_y)

# Keep the window open until manually closed
screen.mainloop()
