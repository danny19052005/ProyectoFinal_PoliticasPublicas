"""Paquete de agentes del sistema multiagéntico."""

from .agente_coordinador import ejecutar as ejecutar_agente_coordinador
from .agente_politicas_publicas import ejecutar as ejecutar_agente_politicas_publicas
from .agente_datos_metodologia import ejecutar as ejecutar_agente_datos_metodologia
from .agente_programador_visualizacion import ejecutar as ejecutar_agente_programador_visualizacion
from .subagente_verificador_fuentes import ejecutar as ejecutar_subagente_verificador_fuentes
from .subagente_revisor_critico import ejecutar as ejecutar_subagente_revisor_critico

__all__ = [
    "ejecutar_agente_coordinador",
    "ejecutar_agente_politicas_publicas",
    "ejecutar_agente_datos_metodologia",
    "ejecutar_agente_programador_visualizacion",
    "ejecutar_subagente_verificador_fuentes",
    "ejecutar_subagente_revisor_critico",
]
