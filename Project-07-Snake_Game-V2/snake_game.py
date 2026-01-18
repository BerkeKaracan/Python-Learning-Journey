import turtle
import random
import time

segments = []
walls = []
bombs = []
powerups = []
active_powerups = {
    "immortal_end": 0,
    "slow_end": 0,
    "has_hammer": False,
    "has_fireball": False
}
score = 0
high_score = 0
delay = 0.1

try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

wn = turtle.Screen()
wn.title("Snake Game V2")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

portal_a = turtle.Turtle()
portal_a.shape("circle")
portal_a.color("black")
portal_a.shapesize(stretch_wid=3, stretch_len=3)
portal_a.penup()
portal_a.goto(10000, 10000)

portal_b = turtle.Turtle()
portal_b.shape("circle")
portal_b.color("black")
portal_b.shapesize(stretch_wid=3, stretch_len=3)
portal_b.penup()
portal_b.goto(10000, 10000)

portals_active = False

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("triangle")
bullet.color("red")
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet.goto(1000, 1000)
bullet.state = "ready"
bullet.direction = "stop"

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


def go_up():
    global delay
    if head.direction != "up":
        delay = 0.1
        head.direction = "up"
    elif head.direction == "up":
        delay = 0.05


def go_down():
    global delay
    if head.direction != "down":
        delay = 0.1
        head.direction = "down"
    elif head.direction == "down":
        delay = 0.05


def go_left():
    global delay
    if head.direction != "left":
        delay = 0.1
        head.direction = "left"
    elif head.direction == "left":
        delay = 0.05


def go_right():
    global delay
    if head.direction != "right":
        delay = 0.1
        head.direction = "right"
    elif head.direction == "right":
        delay = 0.05


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
    with open("highscore.txt", "w") as f:
        f.write(str(high_score))


def create_wall():
    w_safe = (wn.window_width() / 2) - 60
    h_safe = (wn.window_height() / 2) - 60
    max_attempts = 50
    for _ in range(max_attempts):
        x = random.randint(int(-w_safe), int(w_safe))
        y = random.randint(int(-h_safe), int(h_safe))
        superposition = False
        for seg in segments:
            if seg.distance(x, y) < 80:
                superposition = True
                break
        for w, d in walls:
            if w.distance(x, y) < 100:
                superposition = True
                break
        for b in bombs:
            if b.distance(x, y) < 80:
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
            walls.append((wall, direction))
            break


def fire_bullet():
    global active_powerups
    if active_powerups["has_fireball"] and bullet.state == "ready":
        bullet.state = "firing"
        bullet.goto(head.xcor(), head.ycor())
        bullet.showturtle()
        bullet.direction = head.direction
        if head.direction == "up":
            bullet.setheading(90)
        elif head.direction == "down":
            bullet.setheading(270)
        elif head.direction == "left":
            bullet.setheading(180)
        elif head.direction == "right":
            bullet.setheading(0)
        active_powerups["has_fireball"] = False
        update_score()


def move_bullet():
    if bullet.state == "firing":
        speed = 40
        if bullet.direction == "up":
            bullet.sety(bullet.ycor() + speed)
        elif bullet.direction == "down":
            bullet.sety(bullet.ycor() - speed)
        elif bullet.direction == "left":
            bullet.setx(bullet.xcor() - speed)
        elif bullet.direction == "right":
            bullet.setx(bullet.xcor() + speed)

        if not (-350 < bullet.xcor() < 350 and -350 < bullet.ycor() < 350):
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(1000, 1000)
            return

        for wall_tuple in walls[:]:
            wall_obj = wall_tuple[0]
            w_dir = wall_tuple[1]
            hit = False
            if w_dir == "horizontal":
                if (wall_obj.xcor() - 65 < bullet.xcor() < wall_obj.xcor() + 65) and \
                        (wall_obj.ycor() - 25 < bullet.ycor() < wall_obj.ycor() + 25):
                    hit = True
            else:
                if (wall_obj.xcor() - 25 < bullet.xcor() < wall_obj.xcor() + 25) and \
                        (wall_obj.ycor() - 65 < bullet.ycor() < wall_obj.ycor() + 65):
                    hit = True

            if hit:
                wall_obj.goto(1000, 1000)
                walls.remove(wall_tuple)
                bullet.hideturtle()
                bullet.state = "ready"
                bullet.goto(1000, 1000)
                return

        for bomb in bombs[:]:
            if bullet.distance(bomb) < 30:
                bomb.hideturtle()
                bomb.goto(1000, 1000)
                bombs.remove(bomb)
                bullet.hideturtle()
                bullet.state = "ready"
                bullet.goto(1000, 1000)
                return


def create_bomb():
    w_safe = (wn.window_width() / 2) - 50
    h_safe = (wn.window_height() / 2) - 50
    for _ in range(50):
        x = random.randint(int(-w_safe), int(w_safe))
        y = random.randint(int(-h_safe), int(h_safe))
        unsafe = False
        for seg in segments:
            if seg.distance(x, y) < 100:
                unsafe = True
                break
        for w, d in walls:
            if w.distance(x, y) < 80:
                unsafe = True
                break
        for b in bombs:
            if b.distance(x, y) < 60:
                unsafe = True
                break
        if head.distance(x, y) < 120 or food.distance(x, y) < 120:
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
        b.hideturtle()
        b.goto(1000, 1000)
    bombs.clear()
    global portals_active
    portal_a.goto(1000, 1000)
    portal_b.goto(1000, 1000)
    portals_active = False
    global score, delay
    score = 0
    delay = 0.1
    wn.setup(width=600, height=600)
    wn.bgcolor("black")
    update_score()


def trigger_explosion(x, y):
    global active_powerups
    if active_powerups["has_hammer"]:
        hammer_effect = turtle.Turtle()
        hammer_effect.speed(0)
        hammer_effect.shape("circle")
        hammer_effect.color("white")
        hammer_effect.shapesize(8, 8)
        hammer_effect.penup()
        hammer_effect.goto(x, y)
        wn.update()
        blast_radius = 200
        for wall_tuple in walls[:]:
            if wall_tuple[0].distance(x, y) < blast_radius:
                wall_tuple[0].goto(1000, 1000)
                walls.remove(wall_tuple)
        for bomb in bombs[:]:
            if bomb.distance(x, y) < blast_radius:
                bomb.hideturtle()
                bomb.goto(1000, 1000)
                bombs.remove(bomb)
        time.sleep(0.2)
        hammer_effect.clear()
        hammer_effect.hideturtle()
        active_powerups["has_hammer"] = False
        update_score()
        return

    for bomb in bombs:
        if bomb.distance(x, y) < 30:
            bomb.color("yellow")
            bomb.shapesize(stretch_wid=6, stretch_len=6)
            wn.update()
            blast_radius = 120
            for wall_tuple in walls[:]:
                if bomb.distance(wall_tuple[0]) < blast_radius:
                    wall_tuple[0].goto(1000, 1000)
                    walls.remove(wall_tuple)
            if head.distance(bomb) < blast_radius and time.time() > active_powerups["immortal_end"]:
                pen.clear()
                pen.goto(0, 0)
                pen.write("BOOM!", align="center", font=("Courier", 30, "bold"))
                wn.update()
                time.sleep(2)
                reset_game()
                return
            time.sleep(0.1)
            bomb.hideturtle()
            bomb.goto(1000, 1000)
            bombs.remove(bomb)
            wn.update()
            break


def spawn_portals():
    global portals_active
    if portals_active: return
    w_safe = (wn.window_width() / 2) - 100
    h_safe = (wn.window_height() / 2) - 100
    x1 = random.randint(int(-w_safe), int(w_safe))
    y1 = random.randint(int(-h_safe), int(h_safe))
    portal_a.goto(x1, y1)
    x2 = random.randint(int(-w_safe), int(w_safe))
    y2 = random.randint(int(-h_safe), int(h_safe))
    portal_b.goto(x2, y2)
    portals_active = True
    portal_a.color("#333333")
    portal_b.color("#333333")
    wn.update()
    time.sleep(0.1)
    portal_a.color("grey")
    portal_b.color("grey")
    wn.update()
    time.sleep(0.1)
    portal_a.color("cyan")
    portal_b.color("orange")


def create_powerup():
    if len(powerups) >= 3: return
    w_safe = (wn.window_width() / 2) - 50
    h_safe = (wn.window_height() / 2) - 50
    zar = random.randint(1, 100)
    p_type = ""
    if zar <= 40:
        p_type = "growth"
    elif zar <= 60:
        p_type = "slow"
    elif zar <= 65:
        p_type = "hammer"
    elif zar <= 70:
        p_type = "immortal"
    elif zar <= 75:
        p_type = "fireball"
    else:
        return
    for _ in range(20):
        x = random.randint(int(-w_safe), int(w_safe))
        y = random.randint(int(-h_safe), int(h_safe))
        superposition = False
        for w, d in walls:
            if w.distance(x, y) < 50: superposition = True
        for b in bombs:
            if b.distance(x, y) < 50: superposition = True
        if head.distance(x, y) < 50: superposition = True
        if not superposition:
            pup = turtle.Turtle()
            pup.speed(0)
            pup.penup()
            pup.goto(x, y)
            if p_type == "immortal":
                pup.shape("circle")
                pup.color("gold")
            elif p_type == "hammer":
                pup.shape("circle")
                pup.color("white")
            elif p_type == "growth":
                pup.shape("square")
                pup.color("lime")
            elif p_type == "slow":
                pup.shape("square")
                pup.color("cyan")
            elif p_type == "fireball":
                pup.shape("triangle")
                pup.color("red")
            powerups.append((pup, p_type))
            break


wn.listen()
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onscreenclick(trigger_explosion)

update_score()

while True:
    wn.update()
    move_bullet()
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
                    superposition = True;
                    break
            for bomb in bombs:
                if bomb.distance(x, y) < 50:
                    superposition = True;
                    break
            if not superposition:
                food.goto(x, y);
                break

        score += 1
        if score == 100:
            wn.setup(width=900, height=900)
            wn.bgcolor("navy")
            pen.clear()
            pen.goto(0, 0)
            pen.write("UNIVERSE EXPANDING!", align="center", font=("Courier", 30, "bold"))
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

        if score % 3 == 0: create_wall()
        if score % 4 == 0: create_bomb()
        if score > high_score: high_score = score
        update_score()

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    if score > 100 and score % 20 == 0 and not portals_active:
        spawn_portals()
    elif score > 100 and score % 20 == 5 and portals_active:
        portal_a.goto(10000, 10000)
        portal_b.goto(10000, 10000)
        portal_a.color("black")
        portal_b.color("black")
        portals_active = False

    if portals_active:
        if head.distance(portal_a) < 50:
            head.goto(portal_b.xcor(), portal_b.ycor())
            if head.direction == "up":
                head.sety(head.ycor() + 40)
            elif head.direction == "down":
                head.sety(head.ycor() - 40)
            elif head.direction == "right":
                head.setx(head.xcor() + 40)
            elif head.direction == "left":
                head.setx(head.xcor() - 40)
        elif head.distance(portal_b) < 50:
            head.goto(portal_a.xcor(), portal_a.ycor())
            if head.direction == "up":
                head.sety(head.ycor() + 40)
            elif head.direction == "down":
                head.sety(head.ycor() - 40)
            elif head.direction == "right":
                head.setx(head.xcor() + 40)
            elif head.direction == "left":
                head.setx(head.xcor() - 40)

    if score > 80 and random.randint(1, 200) == 1:
        create_powerup()

    for p_tuple in powerups[:]:
        pup_obj, p_type = p_tuple
        if head.distance(pup_obj) < 20:
            pup_obj.goto(1000, 1000)
            powerups.remove(p_tuple)

            if p_type == "immortal":
                active_powerups["immortal_end"] = time.time() + 30
                head.color("gold")
            elif p_type == "slow":
                active_powerups["slow_end"] = time.time() + 60
            elif p_type == "hammer":
                active_powerups["has_hammer"] = True
                update_score()
            elif p_type == "fireball":
                active_powerups["has_fireball"] = True
                update_score()
            elif p_type == "growth":
                score += 5
                for _ in range(5):
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("yellow")
                    new_segment.penup()
                    new_segment.goto(head.xcor(), head.ycor())
                    segments.append(new_segment)
                update_score()

    current_time = time.time()

    if current_time < active_powerups["immortal_end"]:
        head.color("gold")
    else:
        head.color("green")

    if current_time < active_powerups["slow_end"]:
        if delay != 0.05:
            delay = 0.15
    else:
        if delay != 0.05:
            delay = 0.1

    move()

    for bomb in bombs:
        if head.distance(bomb) < 25:
            if time.time() < active_powerups["immortal_end"]:
                bomb.hideturtle()
                bomb.goto(1000, 1000)
                bombs.remove(bomb)
                break

            bomb.color("yellow")
            bomb.shapesize(stretch_wid=6, stretch_len=6)
            wn.update()

            blast_radius = 150
            for wall_tuple in walls[:]:
                if bomb.distance(wall_tuple[0]) < blast_radius:
                    wall_tuple[0].goto(1000, 1000)
                    walls.remove(wall_tuple)

            pen.clear()
            pen.goto(0, 0)
            pen.write("BOOM!", align="center", font=("Courier", 30, "bold"))
            wn.update()
            time.sleep(1)
            reset_game()
            break

    if time.time() > active_powerups["immortal_end"]:
        for wall_obj, direction in walls:
            hx, hy = head.xcor(), head.ycor()
            wx, wy = wall_obj.xcor(), wall_obj.ycor()
            collision = False

            if direction == "horizontal":
                if (wx - 45 < hx < wx + 45) and (wy - 15 < hy < wy + 15):
                    collision = True
            else:
                if (wx - 15 < hx < wx + 15) and (wy - 45 < hy < wy + 45):
                    collision = True

            if collision:
                pen.clear()
                pen.goto(0, 0)
                pen.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
                wn.update()
                time.sleep(1)
                reset_game()
                break

    time.sleep(delay)