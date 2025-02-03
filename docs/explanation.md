Esta parte de la documentación del proyecto se enfoca en un alcance de **orientación de comprensión**.

## **Introducción al método de cuadratura Gaussiana**

El método de **cuadratura Gaussiana** se utiliza para evaluación de integrales de forma numérica.

El método está definido por la siguiente expresión:

\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N+1} w_k f(x_k).
\end{align}

donde: <br>
- $w_k$ son los "pesos". <br>
- $x_k$ son los puntos de muestreo. Nótese que usamos $N+1$ puntos (es decir, $N$ subregiones o subintervalos).

Los pesos y puntos de muestreo se eligen tal que: <br>
- $x_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_N(x)$ de orden $N$. <br>
- $\displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}}$, con $x_k$ que cumple $P_N(x_k)=0$

En este caso, el polinomio de Legendre se calcula de forma automática, así que solo es necesario llamar las funciones con los argumentos correctos.

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

## **Evaluación de la integral**

Solo queda evaluar la integral con la función **legendre(x)**, multiplicar el resultado con los pesos y sumar el resultado para cada valor de $x_k$:

```
# Las expresiones ab_NX[0] y ab_NX[1] representan los valores de los puntos de locación ("x") y pesos ("w") escalados, respectivamente.
sum_N2 = np.sum(ab_N2[1] * legendre(ab_N2[0]))
sum_N3 = np.sum(ab_N3[1] * legendre(ab_N3[0]))
sum_N4 = np.sum(ab_N4[1] * legendre(ab_N4[0]))
sum_N7 = np.sum(ab_N7[1] * legendre(ab_N7[0]))
#Los resultados se guardan en las variables sum_NX.
```

De esta forma, se puede aproximar el resultado de la integral.
