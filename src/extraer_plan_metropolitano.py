# -*- coding: utf-8 -*-
"""
Extractor de texto del Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027

Este módulo extrae el contenido textual del PDF oficial del plan sin utilizar OCR.
Genera archivos de texto plano y metadatos para facilitar el análisis académico.

Advertencia: El texto extraído automáticamente debe contrastarse con el PDF original
antes de citarlo o utilizarlo en análisis académico riguroso.
"""

import json
from pathlib import Path
from datetime import datetime
from pypdf import PdfReader


def verificar_ruta_pdf():
    """
    Verifica que el archivo PDF exista en la ubicación esperada.
    
    Returns:
        Path: Ruta del archivo PDF si existe
        None: Si el archivo no se encuentra
    """
    ruta_pdf = Path("documentos") / "Plan_Metropolitano_Seguridad_Convivencia_2023_2027.pdf"
    
    if not ruta_pdf.exists():
        print(f"❌ Error: El archivo PDF no se encuentra en: {ruta_pdf.absolute()}")
        print("   Por favor, verifica que el archivo exista en la carpeta 'documentos/'")
        return None
    
    return ruta_pdf


def extraer_texto_pdf(ruta_pdf):
    """
    Extrae el texto de todas las páginas del PDF utilizando pypdf.
    
    Args:
        ruta_pdf (Path): Ruta del archivo PDF a procesar
    
    Returns:
        tuple: (diccionario con página y texto, número total de páginas, lista de páginas sin texto)
    """
    try:
        lector = PdfReader(ruta_pdf)
        total_paginas = len(lector.pages)
        paginas_sin_texto = []
        diccionario_texto = {}
        
        print(f"📄 Procesando PDF con {total_paginas} páginas...")
        
        for num_pagina in range(total_paginas):
            pagina = lector.pages[num_pagina]
            texto = pagina.extract_text()
            
            # Registrar páginas sin texto
            if not texto or texto.strip() == "":
                paginas_sin_texto.append(num_pagina + 1)
                diccionario_texto[num_pagina + 1] = ""
            else:
                diccionario_texto[num_pagina + 1] = texto
        
        paginas_con_texto = total_paginas - len(paginas_sin_texto)
        print(f"✓ Extracción completada: {paginas_con_texto} páginas con texto, {len(paginas_sin_texto)} sin texto")
        
        return diccionario_texto, total_paginas, paginas_sin_texto
    
    except Exception as e:
        print(f"❌ Error al procesar el PDF: {str(e)}")
        return None, None, None


def guardar_texto(diccionario_texto, ruta_salida):
    """
    Guarda el texto extraído en un archivo de texto plano.
    
    Args:
        diccionario_texto (dict): Diccionario con número de página y texto
        ruta_salida (Path): Ruta donde guardar el archivo de texto
    
    Returns:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        # Crear directorio si no existe
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        
        with open(ruta_salida, 'w', encoding='utf-8') as archivo:
            for num_pagina in sorted(diccionario_texto.keys()):
                # Escribir encabezado de página
                archivo.write(f"\n===== PÁGINA {num_pagina} =====\n\n")
                
                # Escribir contenido
                texto = diccionario_texto[num_pagina]
                if texto:
                    archivo.write(texto)
                else:
                    archivo.write("[Página sin contenido de texto extraíble]")
                
                archivo.write("\n")
        
        print(f"✓ Texto guardado en: {ruta_salida}")
        return True
    
    except Exception as e:
        print(f"❌ Error al guardar el archivo de texto: {str(e)}")
        return False


def guardar_metadatos(ruta_pdf, total_paginas, paginas_con_texto, paginas_sin_texto, ruta_metadatos):
    """
    Guarda los metadatos del procesamiento en formato JSON.
    
    Args:
        ruta_pdf (Path): Ruta del PDF procesado
        total_paginas (int): Número total de páginas
        paginas_con_texto (int): Número de páginas con texto
        paginas_sin_texto (list): Lista de números de páginas sin texto
        ruta_metadatos (Path): Ruta donde guardar el archivo JSON
    
    Returns:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        # Crear directorio si no existe
        ruta_metadatos.parent.mkdir(parents=True, exist_ok=True)
        
        metadatos = {
            "nombre_archivo": ruta_pdf.name,
            "ruta_archivo": str(ruta_pdf.absolute()),
            "total_paginas": total_paginas,
            "paginas_con_texto": paginas_con_texto,
            "paginas_sin_texto": paginas_sin_texto,
            "fecha_procesamiento": datetime.now().isoformat(),
            "herramienta_utilizada": "pypdf (extracción de texto sin OCR)",
            "advertencia_metodologica": (
                "El texto extraído automáticamente debe contrastarse con el PDF original "
                "antes de citarlo o utilizarlo en análisis académico riguroso. "
                "La extracción automática puede omitir, alterar o malinterpretar contenido, "
                "especialmente en tablas, gráficos o formatos especiales."
            )
        }
        
        with open(ruta_metadatos, 'w', encoding='utf-8') as archivo:
            json.dump(metadatos, archivo, ensure_ascii=False, indent=4)
        
        print(f"✓ Metadatos guardados en: {ruta_metadatos}")
        return True
    
    except Exception as e:
        print(f"❌ Error al guardar metadatos: {str(e)}")
        return False


def main():
    """
    Función principal que orquesta la extracción del PDF.
    """
    print("\n" + "=" * 70)
    print("EXTRACTOR DE CONTENIDO - PLAN METROPOLITANO 2023-2027")
    print("=" * 70 + "\n")
    
    # Verificar que el PDF existe
    ruta_pdf = verificar_ruta_pdf()
    if ruta_pdf is None:
        print("\n⚠️  Abortando proceso...\n")
        return False
    
    # Extraer texto del PDF
    diccionario_texto, total_paginas, paginas_sin_texto = extraer_texto_pdf(ruta_pdf)
    if diccionario_texto is None:
        print("\n⚠️  Abortando proceso...\n")
        return False
    
    # Definir rutas de salida
    ruta_texto_salida = Path("resultados") / "plan_metropolitano_texto.txt"
    ruta_metadatos_salida = Path("resultados") / "plan_metropolitano_metadatos.json"
    
    # Guardar texto extraído
    if not guardar_texto(diccionario_texto, ruta_texto_salida):
        print("\n⚠️  Error: No se pudo guardar el archivo de texto.\n")
        return False
    
    # Guardar metadatos
    paginas_con_texto = total_paginas - len(paginas_sin_texto)
    if not guardar_metadatos(ruta_pdf, total_paginas, paginas_con_texto, paginas_sin_texto, ruta_metadatos_salida):
        print("\n⚠️  Advertencia: No se pudo guardar los metadatos.\n")
        return False
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DEL PROCESAMIENTO")
    print("=" * 70)
    print(f"✓ Total de páginas procesadas: {total_paginas}")
    print(f"✓ Páginas con texto extraído: {paginas_con_texto}")
    print(f"✓ Páginas sin contenido extraíble: {len(paginas_sin_texto)}")
    if paginas_sin_texto:
        print(f"  Páginas sin texto: {paginas_sin_texto}")
    print(f"✓ Archivo de texto: {ruta_texto_salida}")
    print(f"✓ Archivo de metadatos: {ruta_metadatos_salida}")
    print("\n⚠️  IMPORTANTE: Contrasta el texto extraído con el PDF original")
    print("   antes de utilizarlo en análisis académico riguroso.\n")
    print("=" * 70 + "\n")
    
    return True


if __name__ == "__main__":
    """
    Punto de entrada del script.
    Ejecuta la función principal si el archivo se llama directamente.
    """
    main()
