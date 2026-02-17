#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VECTA Módulo: Auto-Reparación con Groq

Comando: repárate

Ejecuta ciclo completo de auto-reparación:
1. Detecta último crash
2. Analiza con Groq
3. Propone solución
4. Aplica
5. Ejecuta tests
6. Si falla → refina y reintenta
7. Cristaliza conocimiento
"""

import os
import sys

# Path setup
ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from core.auto_repair_groq import auto_repair_last_crash
from core.meta_cognitive import get_meta_cognitive


def execute(inputs: dict, **kwargs) -> dict:
    """
    Ejecuta auto-reparación
    
    Args:
        inputs: {
            'crash_id': str (opcional)
        }
    
    Returns:
        {
            'success': bool,
            'iterations': int,
            'knowledge_id': str,
            'message': str
        }
    """
    project_root = kwargs.get('project_root', '.')
    
    print("\n" + "🔧 "*30)
    print("VECTA AUTO-REPARACIÓN")
    print("🔧 "*30)
    
    # Obtener stats pre-reparación
    meta = get_meta_cognitive(project_root)
    stats_before = meta.get_stats()
    
    print(f"\n📊 Meta-Cognitivo:")
    print(f"   Cristales: {stats_before['total_crystals']}")
    print(f"   Exitosos: {stats_before['successful']}")
    print(f"   Fallidos: {stats_before['failed']}")
    
    # Ejecutar auto-reparación
    result = auto_repair_last_crash(project_root)
    
    if result['success']:
        stats_after = meta.get_stats()
        
        message = f"""
✅ AUTO-REPARACIÓN EXITOSA

Iteraciones: {result['iterations']}
Approach final: {result['final_approach'][:100]}...
Conocimiento: {result['knowledge_id']}

Meta-Cognitivo enriquecido:
  Antes: {stats_before['total_crystals']} cristales
  Ahora: {stats_after['total_crystals']} cristales
  Tests pasados: {stats_after['tests_passed']}
"""
        print(message)
        
        return {
            'success': True,
            'iterations': result['iterations'],
            'knowledge_id': result['knowledge_id'],
            'message': message
        }
    
    else:
        message = f"""
❌ AUTO-REPARACIÓN FALLÓ

Razón: {result.get('error', 'Unknown')}
Iteraciones intentadas: {result.get('iterations', 0)}

El meta-cognitivo ha registrado los intentos fallidos.
Próxima vez se refinará automáticamente.
"""
        print(message)
        
        return {
            'success': False,
            'iterations': result.get('iterations', 0),
            'message': message
        }


if __name__ == "__main__":
    # Test
    result = execute({}, project_root='.')
    print(f"\n✓ Resultado: {result['success']}")
