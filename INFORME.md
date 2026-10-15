# Informe de Pruebas Unitarias y Cobertura

## Datos
* **Nombre:** Daniela Lopez Trujillo
* **Grupo:** Pruebas Unitarias y DevOps
* **Fecha:** 14 de Octubre de 2026

## Análisis por módulo
* **Calculadora:** Valida operaciones aritméticas básicas y límites numéricos.
* **Conversor:** Realiza conversiones de temperatura, peso y distancia.
* **Descuentos:** Evalúa rebajas unitarias, acumulativas y apiladas con validación de errores.
* **Fibonacci:** Genera secuencias numéricas y verifica pertenencia con control de índices negativos.

## Tabla de bugs
| Función | Entrada | Erróneo vs Esperado | Corrección |
| :--- | :--- | :--- | :--- |
| `descuento_acumulativo` | `[10, 20]` | Fallaba al recibir listas. | Recorrido iterativo de la lista. |
| `aplicar_descuento` | Precio negativo | Retornaba valores negativos. | Validación estricta con `ValueError`. |
| `fibonacci` | Índice `-1` | Devolvía listas vacías o errores. | Control explícito de excepciones. |

## Cobertura
* 100% de éxito en las 15 pruebas unitarias ejecutadas.
* Cobertura individual entre 95% y 100% en los módulos implementados.

## Reflexión final
La cobertura de código ayuda a identificar líneas no ejecutadas, pero no garantiza la ausencia total de errores lógicos. Este laboratorio permitió afianzar la importancia de diseñar pruebas robustas y manejar excepciones adecuadamente.
