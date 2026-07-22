"""Punto de entrada principal del proyecto académico.

Este módulo inicializa un menú en consola para interactuar con los distintos
agentes del sistema multiagéntico.
"""

import os
import time

from agentes import (
    ejecutar_agente_coordinador,
    ejecutar_agente_datos_metodologia,
    ejecutar_agente_politicas_publicas,
    ejecutar_agente_programador_visualizacion,
    ejecutar_subagente_revisor_critico,
    ejecutar_subagente_verificador_fuentes,
)


def limpiar_pantalla() -> None:
    """Limpia la consola para una mejor experiencia de usuario."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_titulo() -> None:
    """Muestra el título principal del proyecto."""
    print("=" * 90)
    print("Sistema Multiagéntico para el Análisis de Implementación de la Política de Seguridad Ciudadana y Recuperación del Espacio Público del Distrito Metropolitano de Quito")
    print("=" * 90)


def mostrar_menu() -> None:
    """Muestra el menú principal de opciones del sistema."""
    print("\nMenú principal")
    print("1. Ejecutar Agente Coordinador")
    print("2. Ejecutar Agente de Políticas Públicas")
    print("3. Ejecutar Agente de Datos y Metodología")
    print("4. Ejecutar Agente de Programación y Visualización")
    print("5. Ejecutar Subagente Verificador")
    print("6. Ejecutar Subagente Revisor Crítico")
    print("7. Salir")


def ejecutar_accion(opcion: int) -> None:
    """Ejecuta una acción según la opción seleccionada."""
    mensajes = {
        1: "Seleccionaste: Agente Coordinador",
        2: "Seleccionaste: Agente de Políticas Públicas",
        3: "Seleccionaste: Agente de Datos y Metodología",
        4: "Seleccionaste: Agente de Programación y Visualización",
        5: "Seleccionaste: Subagente Verificador",
        6: "Seleccionaste: Subagente Revisor Crítico",
    }

    if opcion == 1:
        print(f"\n{mensajes[opcion]}")
        ejecutar_agente_coordinador()
    elif opcion == 2:
        print(f"\n{mensajes[opcion]}")
        ejecutar_agente_politicas_publicas()
    elif opcion == 3:
        print(f"\n{mensajes[opcion]}")
        ejecutar_agente_datos_metodologia()
    elif opcion == 4:
        print(f"\n{mensajes[opcion]}")
        ejecutar_agente_programador_visualizacion()
    elif opcion == 5:
        print(f"\n{mensajes[opcion]}")
        ejecutar_subagente_verificador_fuentes()
    elif opcion == 6:
        print(f"\n{mensajes[opcion]}")
        ejecutar_subagente_revisor_critico()
    elif opcion == 7:
        print("\nSaliendo del sistema...\n")
    else:
        print("\nOpción no válida. Intenta nuevamente.\n")

    time.sleep(1.2)


def main() -> None:
    """Función principal que controla la ejecución del menú."""
    while True:
        limpiar_pantalla()
        mostrar_titulo()
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\nPor favor ingrese un número válido.\n")
            time.sleep(1.2)
            continue

        ejecutar_accion(opcion)

        if opcion == 7:
            break


if __name__ == "__main__":
    main()
