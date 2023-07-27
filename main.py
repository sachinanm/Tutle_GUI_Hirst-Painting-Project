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
center_x = -150
center_y = -100

# Move the turtle to the center position
tim.penup()
tim.goto(center_x, center_y)
tim.pendown()

current_position_y = -100

# Draw a dot grid using the extracted image colors
for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(image_colors))
        tim.penup()
        tim.forward(35)
        tim.pendown()

    tim.penup()
    current_position_y += 30
    tim.goto(-150, current_position_y)
    tim.pendown()

# Keep the window open until manually closed
screen.mainloop()
