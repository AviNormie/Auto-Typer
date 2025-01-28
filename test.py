import turtle

pen = turtle.Turtle()
pen.shape("turtle")  # Change turtle shape to 'turtle'
pen.color("green")   # Set turtle color
for _ in range(3):
    pen.forward(150)  # Move forward
    pen.right(120)      # Turn left
    # pen.forward(100)   # Move forward

turtle.done()
