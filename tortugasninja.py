import turtle
import random

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("¡Carrera de tortugas!")
ventana.bgcolor("lightgray")
ventana.setup(width=1000, height=600)

# Pista de carreras
pista = turtle.Turtle()
pista.color("black")
pista.width(3)
pista.penup()
pista.goto(-450, 300)
pista.pendown()
pista.goto(-450, -300)
pista.goto(550, -300)
pista.goto(550, 300)
pista.penup()
pista.goto(-150, 300)
pista.right(90)

# Dibujar líneas discontinuas en la pista
pista.penup()
pista.goto(-100, 300)
pista.pendown()
pista.color("white")

posicion_x = 550
while posicion_x > -450:
    pista.penup()
    pista.goto(posicion_x, 300)
    pista.pendown()
    pista.forward(20)
    pista.penup()
    pista.forward(20)
    posicion_x -= 40

# Crear tortugas
tortugas = []
colores = ["red", "orange", "blue", "green", "purple"]
for i in range(5):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(colores[i])
    tortuga.penup()
    tortuga.goto(-440, 200 - i * 120)
    tortuga.pendown()
    tortugas.append(tortuga)

# Función para mover las tortugas aleatoriamente con distancias ajustadas
def mover_tortuga(tortuga):
    distancia = random.randint(5, 15)
    tortuga.forward(distancia)

# Carrera de tortugas
for _ in range(100):
    for tortuga in tortugas:
        mover_tortuga(tortuga)

# Mostrar resultado
ganador = max(tortugas, key=lambda t: t.xcor())
print("¡" + ganador.color()[0].capitalize() + " gana!")

ventana.mainloop()
