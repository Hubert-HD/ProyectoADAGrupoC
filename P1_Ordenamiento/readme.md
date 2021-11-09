### P1: Algoritmos de ordenamiento
---
#### Comando para ejecutar el proyecto
~~~
$ python main.py
~~~
---
#### InsertionSort
El arreglo se divide lógicamente en una parte ordenada y una no ordenada. El algoritmo selecciona los valores de la parte sin ordenar y lo coloca en la parte ordenada en la posición correcta, y asi se realiza varias iteraciones hasta llegar a obtener el arrelgo ordenado.
Complejidad:
| Peor caso | Caso medio | Mejor caso |
|-|-|-|
| O($n^2$) | O($n^2$)| O(n) |

Ejemplo:
![insertionsort-example](gif/insertionsort-example.gif)
#### HeapSort
Los elementos del arreglo son almacenados en un montículo, para luego extraer el elemento mayor que será el nodo raíz del montículo, luego lo intercambiamos con el ultimo elemento arreglo decrementado la cantidad de elementos del montículo y reacomodandolo para que siga siendo un montículo, realizando varias iteraciones de este proceso se obteniene el arreglo ordenado.
Complejidad:
| Peor caso | Caso medio | Mejor caso |
|-|-|-|
| O($nlogn$) | O($nlogn$)| O($nlogn$) |

Ejemplo:
![heapsort-example](gif/heapsort-example.gif)
#### QuickSort
Se divide el arreglo en dos partes alrededor de un elemento de pivote seleccionado, luego se mueve elementos menores al pivote al lado izquierdo del pivote y los elementos mayores al lado derecho. Después de esto a las subpartes izquierda y derecha se les aplica el mismo proceso de forma recursiva hasta obtener el arreglo ordenado. 
Complejidad:
| Peor caso | Caso medio | Mejor caso |
|-|-|-|
| O($n^2$) | O($nlogn$)| O($nlogn$) |

Ejemplo:
![quicksort-example](gif/quicksort-example.gif)
###### Nota: 
* Se puede optimizar el algoritmo quicksort seleccioando un pivote de forma aletatoria 
* Además otra optimización sugerida por Sedgewick para asegurarse de que se use como máximo un espacio $O(log n)$, es seleccionar un umbral, que cuando el número de elementos del arreglo este por debajo de este, se cambie a un algoritmo de ordenación no recursivo, como el insertionsort. El umbral va a depender de los detalles de la implementacion aunque generalmente es 10.
---
