"""Analizador Musical de iTunes (paradigma procedimental)."""
import csv
import re
import sys

import requests

API_URL = "https://itunes.apple.com/search?entity=song&limit=50&term="


def buscar_canciones(termino):
    """Consulta la API de iTunes y devuelve la lista de resultados (o [] si falla)."""
    try:
        respuesta = requests.get(API_URL + termino, timeout=10)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"No se pudo conectar con la API de iTunes: {error}")
        return []
    return respuesta.json().get("results", [])


def filtrar_por_love(resultados):
    """Devuelve las canciones cuyo trackName contiene la palabra 'Love' aislada."""
    filtradas = []
    for cancion in resultados:
        nombre = cancion.get("trackName", "")
        if re.search(r"\bLove\b", nombre, re.IGNORECASE):
            filtradas.append(cancion)
    return filtradas


def guardar_csv(canciones, nombre_archivo="canciones.csv"):
    """Escribe cancion y precio de cada resultado en un CSV."""
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["cancion", "precio"])
        escritor.writeheader()
        for cancion in canciones:
            escritor.writerow({
                "cancion": cancion.get("trackName", ""),
                "precio": cancion.get("trackPrice", 0.0),
            })


def clasificar_precio(precio):
    """Clasifica un precio en 'Gratis', 'Barato' o 'Normal'."""
    if precio == 0.0:
        return "Gratis"
    elif precio < 1.0:
        return "Barato"
    else:
        return "Normal"


def test_clasificar_precio():
    assert clasificar_precio(0.0) == "Gratis"
    assert clasificar_precio(0.5) == "Barato"
    assert clasificar_precio(1.0) == "Normal"


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso inválido")

    termino = sys.argv[1]
    resultados = buscar_canciones(termino)
    canciones_filtradas = filtrar_por_love(resultados)
    guardar_csv(canciones_filtradas)
    print(f"Se guardaron {len(canciones_filtradas)} canciones en canciones.csv")


if __name__ == "__main__":
    main()
