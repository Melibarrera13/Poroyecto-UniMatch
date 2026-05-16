# 09 — Algoritmo de Matching (Explicación Formal)

## Objetivo del algoritmo
Calcular un puntaje de compatibilidad entre dos usuarios en relación a un tema específico, considerando criterios académicos y de disponibilidad.

El algoritmo genera recomendaciones ordenadas por puntaje y crea un match si el usuario lo acepta.

---

## Variables consideradas

### 1. Coincidencia exacta de tema (peso alto)
Si ambos usuarios estudian el mismo `id_tema`, se habilita el cálculo.

Puntaje base:
- Tema en común: +50 puntos
- Tema no en común: no se considera candidato

### 2. Compatibilidad de nivel
Valores posibles:
- básico
- intermedio
- avanzado

Regla:
- Si nivel igual: +20
- Si diferencia de 1 nivel (básico/intermedio o intermedio/avanzado): +10
- Si diferencia de 2 niveles (básico/avanzado): +0

### 3. Compatibilidad de objetivo
Valores posibles:
- aprender
- practicar
- repasar
- explicar

Regla:
- aprender ↔ explicar: +20 (alta complementariedad)
- practicar ↔ practicar: +15
- repasar ↔ repasar: +10
- objetivo igual (otros casos): +10
- objetivos incompatibles: +0

### 4. Idioma
- Idioma igual: +10
- Idioma diferente: +0

### 5. Disponibilidad horaria (incluye zona horaria)
Se verifica si existen bloques horarios solapados para ambos usuarios.

- Solapamiento de al menos 1 bloque: +20
- Sin solapamiento: +0

### 6. Proximidad en grafo (Neo4j)
Se calcula si los usuarios comparten vecinos en el grafo (por ejemplo, temas relacionados o comunidades).

- Conexión indirecta en 2 saltos: +10
- Conexión indirecta en 3 saltos: +5
- Sin conexión: +0

---

## Fórmula de puntaje total

```
puntaje_total =
  50 (tema común)
  + puntaje_nivel
  + puntaje_objetivo
  + puntaje_idioma
  + puntaje_horario
  + puntaje_grafo
```

Rango típico:
- mínimo: 50
- máximo aproximado: 130

---

## Clasificación del resultado

- 110 a 130: Match excelente
- 90 a 109: Match recomendado
- 70 a 89: Match aceptable
- 50 a 69: Match débil

---

## Uso de Redis
Las recomendaciones generadas se almacenan temporalmente en:

`cache:matches:{userId}`

con TTL de 10 minutos.

---

## Uso de PostgreSQL
El match se crea en tabla MATCH con estado "pendiente" y puntaje_compatibilidad.

---

## Uso de Neo4j
Se registra relación en grafo:

(User)-[:MATCHED_WITH {topicId, score, createdAt}]->(User)

---

## Observación académica
Este algoritmo es determinístico y basado en reglas para fines universitarios.
En un entorno real podría complementarse con técnicas de Machine Learning.
