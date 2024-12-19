# Reto: Simulador de una Calculadora de "Notas" (Promedio Ponderado)

## Descripción
Este programa calcula el promedio ponderado de las calificaciones de un estudiante. El usuario ingresará las calificaciones y los pesos correspondientes de las asignaturas, y el programa determinará el promedio ponderado total. Si el promedio es menor que 5.0, el estudiante estará "Desaprobado"; de lo contrario, estará "Aprobado".

## Instrucciones
1. El programa pedirá al usuario que ingrese el número de asignaturas.
2. Para cada asignatura, se solicitará:
   - El nombre de la asignatura (texto corto).
   - La calificación obtenida (un número entre 0 y 10).
   - El peso de la asignatura (por ejemplo, 0.2 para el 20% del total).

3. El promedio ponderado se calculará utilizando la fórmula:
   \[
   \text{Promedio ponderado} = \frac{\sum (\text{calificación} \times \text{peso})}{\sum \text{pesos}}
   \]

4. El resultado se mostrará con dos decimales y el programa indicará si el estudiante está aprobado o desaprobado:
   - **"Aprobado"** si el promedio es mayor o igual a 5.0.
   - **"Desaprobado"** si el promedio es menor que 5.0.

## Ejemplo de ejecución:

```plaintext
Ingrese el número de asignaturas: 3
Para la asignatura Matemáticas:
Calificación: 8.5
Peso: 0.3
Para la asignatura Historia:
Calificación: 7.0
Peso: 0.2
Para la asignatura Física:
Calificación: 9.0
Peso: 0.5

Promedio ponderado: 8.15
Aprobado