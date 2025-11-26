# ------------------------------------------------------------
# Grafo simple del campus de la Universidad AlphaTech
# (Versión sencilla usando diccionarios y listas)
# ------------------------------------------------------------

# 1. NODOS DEL CAMPUS
nodos = {
    "Aulas": "aulas",
    "Biblioteca": "biblioteca",
    "Laboratorio": "laboratorio de software",
    "Cafeteria": "cafeteria",
    "Administracion": "administracion",

    # 3 nodos creados por el estudiante
    "Auditorio": "auditorio",
    "ZonaVerde": "zona verde",
    "Parqueadero": "parqueadero"
}

# 2. ARISTAS (mínimo 12)
# Cada arista tiene:
# (origen, destino, longitud, congestion, tipo_camino, dirigida, cerrada)

aristas = [
    # Bidireccionales
    ("Aulas", "Biblioteca", 120, "media", "peatonal", False, False),
    ("Biblioteca", "Laboratorio", 80, "baja", "peatonal", False, False),
    ("Laboratorio", "Cafeteria", 150, "alta", "mixto", False, False),
    ("Cafeteria", "Administracion", 100, "media", "peatonal", False, False),
    ("Administracion", "ZonaVerde", 90, "baja", "peatonal", False, False),
    ("ZonaVerde", "Aulas", 140, "baja", "peatonal", False, False),

    # Dirigidas
    ("Aulas", "Auditorio", 110, "alta", "peatonal", True, False),
    ("Auditorio", "Parqueadero", 200, "media", "solo bicicletas", True, False),
    ("Parqueadero", "Cafeteria", 170, "alta", "mixto", True, False),
    ("Laboratorio", "Administracion", 95, "media", "peatonal", True, False),

    # Cerradas temporalmente
    ("Aulas", "Cafeteria", 180, "media", "peatonal", False, True),
    ("Biblioteca", "ZonaVerde", 130, "baja", "peatonal", False, True)
]

# ------------------------------------------------------------
# Mostrar nodos
# ------------------------------------------------------------
print("NODOS DEL CAMPUS:")
for n, tipo in nodos.items():
    print(f"- {n} ({tipo})")

# ------------------------------------------------------------
# Mostrar aristas
# ------------------------------------------------------------
print("\nARISTAS DEL CAMPUS:")
for a in aristas:
    origen, destino, dist, cong, tipo_camino, dirigida, cerrada = a
    print(f"{origen} -> {destino} | {dist}m | congestion: {cong} | tipo: {tipo_camino} | dirigida:{dirigida} | cerrada:{cerrada}")

# ------------------------------------------------------------
# EJEMPLO SENCILLO DE RUTA
# ------------------------------------------------------------
print("\nEjemplo de ruta simple de Aulas a Administracion (evitando caminos cerrados):")

ruta = ["Aulas", "Biblioteca", "Laboratorio", "Administracion"]

print(" -> ".join(ruta))
