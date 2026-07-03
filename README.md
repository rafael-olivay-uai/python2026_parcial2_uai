# Examen Práctico de Python – Nivel Integrador

**Tiempo estimado:** 90 minutos
**Modalidad:** resolución individual
**Repositorio de entrega:** [https://github.com/cursos-uai/python2026_parcial2_uai](https://github.com/cursos-uai/python2026_parcial2_uai)

## Instrucciones generales
* El examen consta exactamente de 2 ejercicios integradores diseñados para abarcar todos los temas del curso. 
* El **Ejercicio 1** debe resolverse utilizando un paradigma procedimental (estructurado) y funciones, sin utilizar Clases ni Objetos.
* El **Ejercicio 2** debe resolverse estrictamente utilizando el paradigma de Programación Orientada a Objetos (POO) [1]. Este último debe pensarse y esbozarse primero en papel.
* Para realizar la entrega, cada alumno debe crear un directorio con su nombre y apellido, utilizando guion bajo entre ambos (Ejemplo: `Juan_Perez`).
* Cada ejercicio debe estar en un archivo diferente con el formato `ejercicio_1.py` y `ejercicio_2.py`.
* Para entregar el examen, deberán realizar un fork del repositorio original y luego enviar un Pull Request con la resolución.

---

## Ejercicio 1: Analizador Musical de iTunes (Paradigma Procedimental)
En este ejercicio crearás un script que consulte información de una API, la filtre utilizando expresiones regulares, guarde los resultados en un archivo y valide la lógica matemática con pruebas automatizadas.

**Consigna:**
En el archivo `ejercicio_1.py`, implementa un programa que cumpla con los siguientes requisitos:

1. **Línea de comandos (`sys.argv`):** El programa debe esperar exactamente un argumento adicional al ejecutarse (el nombre de una banda o artista) [2, 3]. Si el usuario no lo provee, o provee más de uno, el programa debe cerrarse inmediatamente utilizando `sys.exit("Uso inválido")` [4].
2. **API y Excepciones:** Utilizando la biblioteca `requests`, haz una consulta a la API de iTunes con la URL `https://itunes.apple.com/search?entity=song&limit=50&term=` concatenada al argumento ingresado [5-7]. Envuelve esta petición en un bloque `try...except` para atrapar posibles errores de conexión y mostrar un mensaje amigable [8, 9].
3. **Expresiones Regulares (`re`):** Itera sobre la lista de resultados JSON [10, 11]. Utiliza la función `re.search` para encontrar únicamente aquellas canciones cuyo título (`trackName`) contenga la palabra "Love" aislada, omitiendo diferencias entre mayúsculas y minúsculas con el indicador `re.IGNORECASE` [12, 13].
4. **Escritura de Archivos (`csv`):** Guarda las canciones filtradas en un archivo llamado `canciones.csv`. Utiliza el gestor de contexto `with open(..., "w")` y la herramienta `csv.DictWriter` para escribir dos columnas: `cancion` y `precio` [14, 15].
5. **Condicionales y Pruebas Unitarias (`pytest`):** 
   * En el mismo archivo, crea una función separada llamada `clasificar_precio(precio)` que reciba un número flotante. Si el precio es `0.0`, debe retornar `"Gratis"`. Si es menor a `1.0`, debe retornar `"Barato"`. Si es mayor o igual a `1.0`, debe retornar `"Normal"` utilizando las sentencias `if`, `elif`, `else` [16, 17].
   * Crea una función llamada `test_clasificar_precio()` que incluya al menos tres aserciones (`assert`) para validar los tres casos posibles de la función anterior, lista para ser evaluada por el framework `pytest` [18, 19].

---

## Ejercicio 2: Bóvedas del Banco Mágico (Programación Orientada a Objetos)
En este ejercicio diseñarás un sistema utilizando clases, encapsulamiento, métodos especiales y lectura de archivos estructurados.

**Consigna:**
En el archivo `ejercicio_2.py`, implementa la lógica orientada a objetos para manejar las cuentas (bóvedas) de un banco mágico:

1. **Clase e Inicialización:** Define una clase `Boveda` [20]. Su método constructor `__init__` debe recibir y asignar mediante el parámetro `self` el `propietario` (texto) y la cantidad inicial de `galeones` (entero, por defecto `0`) [21, 22].
2. **Encapsulamiento y Validaciones:** Protege el atributo de las monedas declarándolo como privado (`_galeones`) [23]. 
   * Crea su método *getter* utilizando el decorador `@property` [24, 25].
   * Crea su método *setter* utilizando `@galeones.setter` y, dentro de él, valida mediante un condicional que la cantidad no sea negativa [24, 25]. Si alguien intenta asignar un valor menor a cero, lanza una excepción utilizando `raise ValueError("El saldo no puede ser negativo")` [26, 27].
3. **Comportamiento (Métodos):**
   * Implementa un método `extraer(cantidad)`. Este debe evaluar si la cantidad solicitada es mayor a los galeones actuales; de ser así, debe generar un `raise ValueError("Saldo insuficiente")` [26, 27]. En caso contrario, debe restar la cantidad al saldo.
   * Implementa el método especial `__str__` para que, al imprimir el objeto, devuelva el formato: `"Bóveda de [Propietario]: [Galeones] galeones"` [28, 29].
   * Sobrecarga el operador matemático de suma mediante el método `__add__(self, other)` [30, 31]. Al sumar dos objetos `Boveda`, debe retornar una nueva instancia de `Boveda` llamada `"Bóveda Combinada"` cuyos galeones sean la suma exacta de las dos bóvedas originales [31, 32].
4. **Lectura de Archivos y Bucles:** Fuera de la clase, escribe una función `cargar_bovedas(nombre_archivo)`. Esta función debe usar el gestor de contexto `with open(...)` y `csv.DictReader` para procesar un archivo llamado `bovedas.csv` (asume que contiene las columnas `propietario` y `galeones`) [33, 34]. 
   * Utiliza un bucle `for` para instanciar un objeto `Boveda` por cada fila del archivo y agrégalos a una lista (`list`) [34, 35]. 
   * Envuelve la apertura del archivo en un bloque `try...except FileNotFoundError`
