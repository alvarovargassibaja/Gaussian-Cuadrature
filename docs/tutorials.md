Esta parte de la documentación del proyecto se enfoca en un alcance de **orientación de aprendizaje**.

Para este caso, se realizarán ejemplos con valores de N iguales a $2, 3, 4, 7$.

## **Obteniendo los puntos de colocación y pesos**

Se puede llamar la función **gaussxw(N)** de la siguiente forma:

```
#El argumento corresponde al valor de regiones.
xw_N2 = gaussxw(2)
xw_N3 = gaussxw(3)
xw_N4 = gaussxw(4)
xw_N7 = gaussxw(7)
#Los resultados se guardan en las variables xw_NX.
```

El resultado obtenido sería un arreglo de datos con los valores para los $x_k$ y los $w_k$.

## **Escalado de puntos de muestreo y pesos**

Ahora, con los resultados obtenidos, se puede realizar el escalado en el intervalo $[1,3]$. Utilizando la función **gaussxwab(a, b, x, w)**:

```
#Los primeros dos argumentos corresponden a los límites de integración.
#El tercer argumento corresponde a los puntos de colocación.
#El cuarto argumento corresponde a los pesos.
ab_N2 = gaussxwab(1, 3, xw_N2[0], xw_N2[1])
ab_N3 = gaussxwab(1, 3, xw_N3[0], xw_N3[1])
ab_N4 = gaussxwab(1, 3, xw_N4[0], xw_N4[1])
ab_N7 = gaussxwab(1, 3, xw_N7[0], xw_N7[1])
#Los resultados se guardan en las variables ab_NX.
```
El resultado obtenido serían los $x_k$ y los $w_k$ escalados al intervalo deseado.

## **Evaluación de la integral**

Solo queda evaluar la integral con la función **legendre(x)**, multiplicar el resultado con los pesos y sumar el resultado para cada valor de $x_k$:

```
# Las expresiones ab_NX[0] y ab_NX[1] representan los valores de los puntos de locación ("x") y pesos ("w") escalados, respectivamente.
sum_N2 = np.sum(ab_N2[1] * legendre(ab_N2[0])) #598.2404774605827
sum_N3 = np.sum(ab_N3[1] * legendre(ab_N3[0])) #375.4943611830493
sum_N4 = np.sum(ab_N4[1] * legendre(ab_N4[0])) #317.3453903341579
sum_N7 = np.sum(ab_N7[1] * legendre(ab_N7[0])) #317.34424667222606
#Los resultados se guardan en las variables sum_NX.
```
Se puede apreciar que el valor de la integral de forma numérica se aproxima al resultado esperado para un N igual a $7$.

`sum_N7 = 317.34424667222606`

Resolviendo la integral de forma analítica, se obtiene el resultado esperado:

$$
\int_{1}^{3} \left[ x^{6} - x^{2} \sin(2x) \right] \, dx \approx 317.34425
$$
