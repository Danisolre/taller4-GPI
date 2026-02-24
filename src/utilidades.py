def formatear_monto(valor):
    return f"${valor:,.0f}"

def calcular_duracion(fecha_inicio, fecha_fin):
    from datetime import datetime
    d1 = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    d2 = datetime.strptime(fecha_fin, '%Y-%m-%d')
    return (d2 - d1).days
