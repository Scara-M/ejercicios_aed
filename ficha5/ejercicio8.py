"""
--Juego del Punto--
La idea general del Juego del Punto, es lograr el máximo puntaje en 4(cuatro) vueltas de lanzamiento de 3 dados,
y a continuación enumeramos las reglas en base a las cuales se obtiene puntaje:
1.) Cada jugador dispone de 4(cuatro) tiradas o lanzamientos para lograr su objetivo, el programa solo deberá
simular de a una tirada por vez.
2.) En cada tirada se lanzan 3(tres) dados. Sólo suman puntaje los dados que salgan con un punto en el centro
(esto es: el 1, el 3 y el 5) (y de allí el nombre del juego). El puntaje de la tirada se calcula sumando el aporte de
cada dado, de acuerdo a las siguientes pautas:
Si sale el 1, se suma 1(un) punto (el único que muestra el dado).
Si sale el 3, se suman 2(dos) puntos (porque a los costados del punto central hay dos puntos).
Si sale el 5, se suman 4(cuatro) puntos (porque en este caso, hay cuatro puntos a los costados del central).
Si sale un número par (2, 4 o 6) no se suma ningún punto (porque ese dado no tiene punto central).
3.) Si en alguna de las tiradas el jugador saca tres números pares iguales, entonces el jugador duplicará los puntos
finales que haya sumado al terminar sus cuatro lanzamientos.
Se pide: que en base a todo lo indicado, se genere un programa que simule 1 tirada de los 3 dados y luego
habiendo solicitado al usuario que cargue su puntaje previo, informe su puntaje acumulado en el caso de haber
obtenido puntos, su puntaje previo y el mensaje de que duplica puntos si salieron los 3 pares o simplemente su
puntaje previo si no sumó ningún punto.
"""