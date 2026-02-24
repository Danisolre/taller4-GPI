#!/bin/bash
echo "=== FASE 1: Generacion de datos ==="
python scripts/generate_data.py
echo ""
echo "=== FASE 2: Limpieza ==="
python scripts/clean_data.py
echo ""
echo "=== FASE 3: Analisis ==="
python scripts/analyze_data.py
echo ""
echo "=== FASE 4: Visualizacion ==="
python scripts/visualize_data.py
echo ""
echo "=== PIPELINE COMPLETADO ==="
