import turtle as t

# Configurações iniciais
t.speed(0)
t.bgcolor("white")
t.title("Desenho do Naruto")

# Desenhar o cabelo
t.penup()
t.goto(0, -200)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(200)
t.end_fill()

# Desenhar a face
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("peachpuff")
t.begin_fill()
t.circle(150)
t.end_fill()

# Desenhar os olhos
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

draw_eye(-70, 100)  # Olho esquerdo
draw_eye(70, 100)   # Olho direito

# Desenhar as pupilas
def draw_pupil(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

draw_pupil(-70, 120)  # Pupila esquerda
draw_pupil(70, 120)   # Pupila direita

# Desenhar a boca
t.penup()
t.goto(0, 40)
t.pendown()
t.width(10)
t.goto(40, -10)
t.goto(-40, -10)

# Esconder a tartaruga
t.penup()
t.hideturtle()

# Manter a janela aberta até que seja fechada pelo usuário
t.done()
