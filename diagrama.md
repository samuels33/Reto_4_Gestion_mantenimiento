# Diagrama grafico 🎨

Este diagrama muestra cómo fluye la información en el sistema de gestión de mantenimiento de flota. El técnico ingresa por consola (`input()`) los datos de cada aeronave (matrícula, modelo y horas de vuelo) y de sus componentes críticos (nombre, horas de uso y límite de horas). Esos datos se guardan en una estructura de memoria compuesta por un diccionario general que contiene listas de diccionarios: cada aeronave es un diccionario con sus datos y una lista de componentes, y cada componente es a su vez un diccionario. Finalmente, el módulo de consulta recorre esta estructura con ciclos `for` y reporta los componentes que superaron su límite de horas y requieren mantenimiento inmediato.

![Diagrama de bloques del sistema de mantenimiento de flota](diagrama<.jpeg)

*Figura 1. Diagrama de bloques: flujo de datos y estructura de almacenamiento.*
