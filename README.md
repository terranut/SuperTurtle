# SuperTurtle
Proyecto de aprendizaje del lenguaje Python a través del módulo gráfico incluído Turtle<br>

La clase Tablero genera una malla con las filas y celdas indicadas en el constructor<br>

El metodo malla almacena las coordenadas a la vez que el objeto turtle dibuja la cuadricula con el metodo celda()

Cada coordenada se corresponde con el punto central  (x,y) de cada celda.

Para obtener las coordenadas se puede llamar a la celda por el numero de fila y numero de columna (f,c)

De esta forma tenemos un sistema de grid primitivo que nos permite elegir la zona de dibujo para nuestra turtle.

El ejemplo de esta pequeña app. Emplea la clase tablero y el evento onclick() para mandar a turtle a dibujar cuadros en las coordenadas indicadas.

Pickel
Se emplea el módulo pickel para serializar la lista de coordenadas y así tener una carga y guardado básico de nuestros dibujos.
