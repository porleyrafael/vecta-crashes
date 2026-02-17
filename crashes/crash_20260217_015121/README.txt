╔══════════════════════════════════════════════════════════╗
║          VECTA DEBUG SNAPSHOT                            ║
║          20260217_015121                              ║
╚══════════════════════════════════════════════════════════╝

ERROR CAPTURADO AUTOMÁTICAMENTE

Tipo: RuntimeError
Mensaje: VECTA_SELFTEST_FAILED: pytest exit_code=1

Usuario escribió: None

ARCHIVOS INCLUIDOS:
├── error.json              ← Información del error
├── stack_trace.txt         ← Stack trace completo
├── system_state.json       ← Estado de VECTA
├── last_action.json        ← Última acción ejecutada
├── runtime/                ← Archivos del runtime
│   ├── session_events.jsonl
│   ├── last_action.json
│   └── last_report.json
└── learned_modules/        ← Últimos módulos aprendidos

INSTRUCCIONES PARA CLAUDE:

1. Lee error.json para contexto
2. Lee stack_trace.txt para el error exacto
3. Revisa learned_modules/ si el error es de código generado
4. Lee session_events.jsonl para ver qué pasó antes del crash

STACK TRACE PREVIEW:
Traceback (most recent call last):
  File "C:\Users\Admin\Downloads\Feem\Desktop\VECTA\VECTA pruebas\VECTA_v4.6_AUTO_MEJORA_GROQ\vecta_zip62_v4.5.1\core\self_test.py", line 116, in report_failure_to_github
    raise RuntimeError(
RuntimeError: VECTA_SELFTEST_FAILED: pytest exit_code=1
...

═══════════════════════════════════════════════════════════

Para enviar a Claude:
1. Comprime esta carpeta completa
2. Súbela y menciónala en el chat
3. Claude analizará TODO el contexto automáticamente

═══════════════════════════════════════════════════════════
