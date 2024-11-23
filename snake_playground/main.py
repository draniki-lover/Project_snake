import time
import random
import turtle
import colorsys
import background

score = 0
high_score = 0
sleep = 0.3
width = 666
height = 666
screen = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()
quote = turtle.Turtle()
border = turtle.Turtle()
snake_body = []
number_of_eaten_food = 0
background.settings(screen, head, food, quote)

while True:  # процесс игры
    screen.update()
    if head.distance(food) < 17: # если змейка "поедает" фрукт
        number_of_eaten_food += 1
        new_color = colorsys.hsv_to_rgb(random.random(), 1, 0.5)
        if number_of_eaten_food % 2 == 1:
            width -= 20 # сначала уменьшаемся поле справа-слева
        elif number_of_eaten_food % 2 == 0:
            height -= 20 # уменьшается поле сверху-снизу
        foodX = random.randint(-1 * width / 2 + 30, width / 2 - 30)
        foodY = random.randint(-1 * height / 2 + 30, height / 2 - 30)
        screen.setup(width, height)
        food.goto(foodX, foodY)

        new_snake_part = turtle.Turtle() # вот тут создается доп часть хвоста
        new_snake_part.shape("circle")
        new_snake_part.color(new_color)
        new_snake_part.penup()
        snake_body.append(new_snake_part)

        for segment in snake_body: # при поедании меняем цвет каждого элемента хвоста
            segment.color(new_color)
        sleep -= 0.01 # немного увеличиваем скорость движения змейки (для интерактивности)
        score += 10 
        if score > high_score: 
            high_score = score
        quote.clear() # *обновляем* заголовок игры
        quote.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 12, "normal"))

    if head.xcor() > width / 2 - 15 or head.xcor() < -1 * width / 2 + 15 or head.ycor() > height / 2 - 15 or head.ycor() < -1 * height / 2 + 15:
        # случай, когда змейка ударяется о границы поля
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in snake_body:
            segment.goto(width, height)
        snake_body.clear()
        number_of_eaten_food = 0
        score = 0
        sleep = 0.2
        quote.clear()
        quote.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Courier", 12, "normal"))

    for index in range(len(snake_body) - 1, 0, -1): # цикл следования частей змейки друг за другом
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)
    if len(snake_body) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x, y)

    background.move(head)

    for part in snake_body:
        if part.distance(head) < 20: # случай, когда змейка головой ударяется о собственный хвост
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for part in snake_body:
                part.goto(1000, 1000)
            part.clear()
            number_of_eaten_food = 0
            score = 0
            sleep = 0.2
            quote.clear()
            quote.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 12, "normal"))
    time.sleep(sleep)

screen.mainloop()

