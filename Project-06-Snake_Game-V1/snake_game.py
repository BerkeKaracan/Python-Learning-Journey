import turtle
import random
import time
segments = []
walls = []
bombs = []
score = 0
high_score = 0
delay = 0.1
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

portal_a = turtle.Turtle()
portal_a.shape("circle")
portal_a.color("black")
portal_a.shapesize(stretch_wid=2, stretch_len=2)
portal_a.penup()
portal_a.goto(10000,10000)

portal_b = turtle.Turtle()
portal_b.shape("circle")
portal_b.color("black")
portal_b.shapesize(stretch_wid=2, stretch_len=2)
portal_b.penup()
portal_b.goto(10000,10000)

portals_active = False

pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
def go_up():
    if head.direction != "up":
        head.direction = "up"
def go_down():
    if head.direction != "down":
        head.direction = "down"
def go_left():
    if head.direction != "left":
        head.direction = "left"
def go_right():
    if head.direction != "right":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def update_score():
    pen.clear()
    x_pos = -(wn.window_width() / 2) + 20
    y_pos = (wn.window_height() / 2) - 40
    pen.goto(x_pos, y_pos)
    pen.write(f"Score: {score}  High Score: {high_score}", align="left", font=("Courier", 20, "normal"))

def create_wall():
    w_safe = (wn.window_width() / 2) - 60
    h_safe = (wn.window_height() / 2) - 60

    max_attempts = 50
    for _ in range(max_attempts):
        x = random.randint(int(-w_safe),int(w_safe))
        y = random.randint(int(-h_safe),int(h_safe))
        superposition = False
        for seg in segments:
            if seg.distance(x, y) < 60:
                superposition = True
                break
        for w, d in walls:
            if w.distance((x,y)) < 100:
                superposition = True
                break

        if head.distance(x, y) < 80 or food.distance(x, y) < 80:
            superposition = True
        if not superposition:
            wall = turtle.Turtle()
            wall.speed(0)
            wall.shape("square")
            wall.color("orange")
            wall.penup()
            wall.goto(x, y)

            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                wall.shapesize(stretch_wid=1, stretch_len=6)
            else:
                wall.shapesize(stretch_wid=6, stretch_len=1)
            walls.append((wall,direction))
            break


def create_bomb():
    w_safe = (wn.window_width() / 2) - 50
    h_safe = (wn.window_height() / 2) - 50
    for _ in range(50):
        x = random.randint(int(-w_safe), int(w_safe))
        y = random.randint(int(-h_safe), int(h_safe))
        unsafe = False
        for seg in segments:
            if seg.distance(x, y) < 60:
                unsafe = True
                break
        for w, d in walls:
            if w.distance(x, y) < 60:
                unsafe = True
                break
        for b in bombs:
            if b.distance(x, y) < 50:
                unsafe = True
                break
        if head.distance(x, y) < 100 or food.distance(x, y) < 100:
            unsafe = True
        if not unsafe:
            bomb = turtle.Turtle()
            bomb.speed(0)
            bomb.shape("circle")
            bomb.color("darkred")
            bomb.shapesize(2, 2)
            bomb.penup()
            bomb.goto(x, y)
            bombs.append(bomb)
            break


def reset_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()

    for w, d in walls:
        w.goto(1000, 1000)
    walls.clear()

    for b in bombs:
        b.goto(1000, 1000)
    bombs.clear()

    global score, delay
    score = 0
    delay = 0.1
    wn.setup(width=600, height=600)
    wn.bgcolor("black")
    update_score()
def trigger_explosion(x, y):
    for bomb in bombs:
        if bomb.distance(x, y) < 30:
            bomb.color("yellow")
            bomb.shapesize(stretch_wid=6, stretch_len=6)
            wn.update()
            blast_radius = 120
            for wall_tuple in walls[:]:
                wall_obj = wall_tuple[0]
                if bomb.distance(wall_obj) < blast_radius:
                    wall_obj.goto(1000, 1000)
                    walls.remove(wall_tuple)
            if head.distance(bomb) < blast_radius:
                pen.clear()
                pen.goto(0, 0)
                pen.write("HAHAHAHAHA! ☠️", align="center", font=("Courier", 24, "bold"))
                wn.update()
                time.sleep(2)
                reset_game()

            time.sleep(0.1)
            bomb.goto(1000, 1000)
            bombs.remove(bomb)
            wn.update()
            break
def spawn_portals():
    global portals_active

    if portals_active:
        return

    w_safe = (wn.window_width() / 2) - 100
    h_safe = (wn.window_height() / 2) - 100

    x1 = random.randint(int(-w_safe), int(w_safe))
    y1 = random.randint(int(-h_safe), int(h_safe))
    portal_a.goto(x1, y1)

    x2 = random.randint(int(-w_safe), int(w_safe))
    y2 = random.randint(int(-h_safe), int(h_safe))
    portal_b.goto(x2, y2)
    portals_active= True

    portal_a.color("#333333")
    portal_b.color("#333333")
    wn.update()
    time.sleep(0.2)

    portal_a.color("grey")
    portal_b.color("grey")
    wn.update()
    time.sleep(0.2)

    portal_a.color("cyan")
    portal_b.color("orange")

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onscreenclick(trigger_explosion)
update_score()

while True:
    wn.update()
    w_limit = (wn.window_width() / 2) - 10
    h_limit = (wn.window_height() / 2) - 10
    if head.xcor() > w_limit:
        head.setx(-w_limit)
    elif head.xcor() < -w_limit:
        head.setx(w_limit)
    if head.ycor() > h_limit:
        head.sety(-h_limit)
    elif head.ycor() < -h_limit:
        head.sety(h_limit)

    if head.distance(food) < 20:
        while True:
            x = random.randint(int(-w_limit + 20), int(w_limit - 20))
            y = random.randint(int(-h_limit + 20), int(h_limit - 20))
            superposition = False
            for wall_obj, direction in walls:
                if wall_obj.distance(x, y) < 50:
                    superposition = True
                    break
            for bomb in bombs:
                if bomb.distance(x, y) < 50:
                    superposition = True
                    break
            if not superposition:
                food.goto(x, y)
                break
        score += 1
        if score == 100:
            wn.setup(width=900, height=900)
            wn.bgcolor("navy")
            pen.clear()
            pen.goto(0, 0)
            pen.write("You thought it was over, didn't you? We're just getting started !", align="center", font=("Courier", 30, "bold"))
            wn.update()
            time.sleep(2)
            pen.clear()
            update_score()
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(head.xcor(), head.ycor())
        segments.append(new_segment)
        if score % 3 == 0:
            create_wall()
        if score % 4 == 0:
            create_bomb()
        if score > high_score:
            high_score = score
        update_score()

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    if score > 100 and score % 15 == 0 and not portals_active:
        spawn_portals()

    elif score > 100 and score % 20 == 0 and portals_active:
        portal_a.goto(1000, 1000)
        portal_b.goto(1000, 1000)
        portal_a.color("black")
        portal_b.color("black")
        portals_active = False

    if head.distance(portal_a) < 50:
        head.goto(portal_b.xcor(), portal_b.ycor())
        if head.direction == "up": head.sety(head.ycor() + 40)
        elif head.direction == "down": head.sety(head.ycor() - 40)
        elif head.direction == "right": head.setx(head.xcor() + 40)
        elif head.direction == "left": head.setx(head.xcor() - 40)

    elif head.distance(portal_b) < 50:
        head.goto(portal_a.xcor(), portal_a.ycor())
        if head.direction == "up": head.sety(head.ycor() + 40)
        elif head.direction == "down": head.sety(head.ycor() - 40)
        elif head.direction == "right": head.setx(head.xcor() + 40)
        elif head.direction == "left": head.setx(head.xcor() - 40)

    move()
    for bomb in bombs:
        if head.distance(bomb) < 25:
            bomb.color("yellow")
            bomb.shapesize(stretch_wid=6, stretch_len=6)
            wn.update()
            blast_radius = 150
            for wall_tuple in walls[:]:
                wall_obj = wall_tuple[0]
                if bomb.distance(wall_obj) < blast_radius:
                    wall_obj.goto(1000, 1000)
            pen.clear()
            pen.goto(0, 0)
            pen.write("BOOOM! ☠️", align="center", font=("Courier", 30, "bold"))
            wn.update()
            reset_game()
            break
    time.sleep(delay)

    for wall_obj, direction in walls:
        hx, hy = head.xcor(), head.ycor()
        wx, wy = wall_obj.xcor(), wall_obj.ycor()
        collision = False

        if direction == "horizontal":
            if (wx - 45 < hx < wx +45 ) and (wy - 15 < hy < wy +15):
                collision = True
        else:
            if (wx - 15 < hx < wx +15 ) and (wy - 45 < hy < wy +45):
                collision = True

        if collision:
            pen.clear()
            pen.goto(0, 0)
            pen.write("AHAHAHAHAHAHAHAH!", align="center", font=("Courier", 24, "bold"))
            wn.update()
            reset_game()
            break