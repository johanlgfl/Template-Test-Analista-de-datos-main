# Prueba Técnica de Analista de Datos - Just Join IT

## Objetivo General

Evaluar las competencias en el manejo de estructuras de datos, algoritmos de búsqueda y ordenamiento, y el procesamiento eficiente de grandes volúmenes de datos en formato CSV, utilizando un enfoque práctico que simula un escenario real de análisis de datos en el ámbito laboral de Tecnologías de la Información (TI).

## Contexto

Just Join IT es una plataforma líder en Polonia para ofertas de empleo en el sector de TI. Esta prueba técnica se centra en el análisis de un conjunto de datos representativo de ofertas de trabajo, con el objetivo de extraer insights relevantes sobre tendencias en habilidades, tipos de empleo, y otros factores clave en el mercado laboral tecnológico.

## Estructura de carpetas

La plantilla del desafío tiene cuatro partes principales:

1. [DISClib](./DISClib) Carpeta raíz con la librería oficial. Para más información sobre su implementación, visita el [Repositorio de DISClib][disclib-url].
2. [App](./App) Carpeta con los scripts de Python siguiendo el patrón modelo-vista-controlador (MVC).
3. [Data](./Data) Carpeta con archivos de datos CSV para cargar en la aplicación.
4. [Docs](./Docs) Carpeta donde se debe poner el analisis de los requerimientos


## Estructura de App

El proyecto sigue el patrón Modelo-Vista-Controlador (MVC), dividido principalmente en tres archivos:

### `controller.py`

Responsable de mediar entre la vista (`view.py`) y el modelo (`model.py`), gestionando el flujo de datos y las operaciones entre la interfaz de usuario y la lógica de negocio. 

- **Funciones clave**: Inicialización del modelo, carga de datos desde archivos CSV, delegación de operaciones analíticas al modelo.

### `model.py`

Contiene las estructuras de datos y algoritmos para el procesamiento y análisis de datos. Utiliza la biblioteca DISClib para estructuras de datos y algoritmos de ordenamiento.

- **Estructuras de datos**: Listas, pilas, colas, mapas (tablas de hash).
- **Algoritmos**: Ordenamiento (Shell sort, Merge sort, etc.), análisis específico de los requerimientos.

### `view.py`

Gestiona la interacción con el usuario, presentando menús de opciones y resultados de las operaciones en formato tabular utilizando la librería `tabulate`.

## Desarrollo de la Prueba

Los candidatos deben enfocarse en desarrollar las siguientes partes, siguiendo las instrucciones específicas para cada archivo y asegurando la integración efectiva de todos los componentes del proyecto:

1. **Carga y procesamiento de datos**: Implementar la lógica para leer y procesar eficientemente los archivos CSV en `controller.py`, almacenando los datos en las estructuras adecuadas definidas en `model.py`.

2. **Análisis de datos**: Desarrollar funciones en `model.py` para realizar los análisis solicitados en los requerimientos de la prueba técnica, aplicando algoritmos de búsqueda y ordenamiento cuando sea necesario.

3. **Interfaz de usuario**: Expandir `view.py` para incluir opciones de menú que permitan al usuario ejecutar las operaciones de análisis de datos y visualizar los resultados.



