from turtle import Turtle

X_AXIS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.set_snake()
        self.head = self.segments[0]

    def set_snake(self):
        for x in X_AXIS:
            self.add_segment(x)

    def add_segment(self, pos):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    # This function resets the snake too and moves the snake
    # from the previous game away from the screen, to a location not visible to us
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.set_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The range() method here will allow us get the segments in reverse order (from the last to first segments)
        # e.g. instead of the usual 0,1,2 we will get the order 2,1,0
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Since all segments need to move together, we need to move each segment from the back to
            # the position of the segment before it. E.g. Segment C with the coordinates (-40,0) should change position
            # to the position of the segment B which is (-20,0), etc.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    # For each of these functions, the snake should not be able to go back in the direction it is coming from
    # E.g. if it is coming from the right to the left, it shouldn't be able to go back to the right until
    # another directions is specified first
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

