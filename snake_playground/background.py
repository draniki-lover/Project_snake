import random
import colorsys

# from main import width, height


def settings(window, he, fruit, phrase):
    """
    Функция отвечает за внешний вид и начаьные настройки работы игры.
    """
    window.title("Snake game") #наделяем свойствами окно, в котором будет происходить процесс игры"
    window.bgcolor("black")
    window.setup()
    window.tracer(0)


    he.shape("circle") #создаем голову змейки
    he.color("white")
    he.penup()
    he.goto(0, 0)
    he.direction = "Stop"

    colors = colorsys.hsv_to_rgb(random.random(), 0.5, 0.5) #блок, отвечающий за свойства фруктов для змейки
    shapes = random.choice(['square', 'triangle', 'circle'])
    fruit.speed(0)
    fruit.shape(shapes)
    fruit.color(colors)
    fruit.penup()
    fruit.goto(0, 100)

    phrase.color("white") #заголовок окна
    phrase.penup()
    phrase.hideturtle()
    phrase.goto(0, 250)
    phrase.write("Score : 0  High Score : 0", align="center", font=("Courier", 12, "normal"))

    def gohigher():
        if he.direction != "dowind":
            he.direction = "up"

    def godown():
        if he.direction != "up":
                he.direction = "dowind"

    def goleft():
        if he.direction != "right":
                he.direction = "left"

    def goright():
        if he.direction != "left":
                he.direction = "right"

    window.listen()
    window.onkeypress(gohigher, "w")
    window.onkeypress(godown, "s")
    window.onkeypress(goleft, "a")
    window.onkeypress(goright, "d")

def move(he):
    """
    Функция связывает нажатие клавиши с координатами поля для перемещения головы змеи
    """
    if he.direction == "up":
        y = he.ycor()
        he.sety(y + 20)
    if he.direction == "dowind":
        y = he.ycor()
        he.sety(y - 20)
    if he.direction == "left":
        x = he.xcor()
        he.setx(x - 20)
    if he.direction == "right":
        x = he.xcor()
        he.setx(x + 20)

# def frame_change(line, count):
#     if count % 2 == 1:
#         line.hideturtle()
#         line.penup()
#         line.goto(-1 * width + 10/ 2, height / 2)
#         line.pendown()
#         line.goto(width / 2 - 10, height / 2)
#         line.goto(width / 2 - 10, -1 * height / 2)
#         line.goto(-1 * width / 2 + 10, -1 * height / 2)
#         line.goto(-1 * width / 2 + 10, height / 2)
    # elif count % 2 == 0:
    #     line.hideturtle()
    #     line.penup()
    #     line.goto(-1 * width / 2 + 10, height / 2)
    #     line.pendown()
    #     line.goto(width / 2 - 10, height / 2)
    #     line.goto(width / 2 - 10, -1 * height / 2)
    #     line.goto(-1 * width / 2 + 10, -1 * height / 2)
    #     line.goto(-1 * width / 2 + 10, height / 2)
