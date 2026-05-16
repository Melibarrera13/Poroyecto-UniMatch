# 07 — Diccionario de Datos

## Tabla: UNIVERSIDAD
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_universidad | SERIAL | PK | Identificador único de universidad |
| nombre | VARCHAR(150) | NOT NULL | Nombre oficial |
| pais | VARCHAR(80) | NOT NULL | País |

## Tabla: USUARIO
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_usuario | SERIAL | PK | Identificador del usuario |
| nombre | VARCHAR(120) | NOT NULL | Nombre visible |
| email | VARCHAR(150) | UNIQUE NOT NULL | Email de acceso |
| contrasena_hash | VARCHAR(255) | NOT NULL | Hash seguro de contraseña |
| pais | VARCHAR(80) | NOT NULL | País del usuario |
| idioma | VARCHAR(40) | NOT NULL | Idioma principal |
| id_universidad | INT | FK | Universidad asociada |

## Tabla: TEMA
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_tema | SERIAL | PK | Identificador de tema |
| nombre_estandar | VARCHAR(200) | UNIQUE NOT NULL | Nombre normalizado |
| area | VARCHAR(120) | NOT NULL | Área (ej: Matemática, Programación) |

## Tabla: ALIAS_TEMA
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_alias | SERIAL | PK | Identificador de alias |
| texto_alias | VARCHAR(200) | NOT NULL | Texto alternativo |
| idioma | VARCHAR(40) | NOT NULL | Idioma del alias |
| id_tema | INT | FK NOT NULL | Tema asociado |

## Tabla: USUARIO_TEMA
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_usuario | INT | PK/FK | Usuario |
| id_tema | INT | PK/FK | Tema |
| nivel | VARCHAR(20) | NOT NULL | básico/intermedio/avanzado |
| objetivo | VARCHAR(20) | NOT NULL | aprender/practicar/repasar/explicar |

## Tabla: HORARIO_DISPONIBLE
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_horario | SERIAL | PK | Identificador |
| dia | VARCHAR(12) | NOT NULL | Lunes..Domingo |
| hora_inicio | TIME | NOT NULL | Inicio |
| hora_fin | TIME | NOT NULL | Fin |
| zona_horaria | VARCHAR(60) | NOT NULL | Ej: America/Argentina/Buenos_Aires |
| id_usuario | INT | FK NOT NULL | Usuario asociado |

## Tabla: MATCH
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_match | SERIAL | PK | Identificador |
| id_usuario1 | INT | FK NOT NULL | Usuario 1 |
| id_usuario2 | INT | FK NOT NULL | Usuario 2 |
| id_tema | INT | FK NOT NULL | Tema en común |
| estado | VARCHAR(20) | NOT NULL | pendiente/aceptado/rechazado/finalizado |
| fecha_match | TIMESTAMP | NOT NULL | Fecha de creación |
| puntaje_compatibilidad | NUMERIC(5,2) | NOT NULL | Puntaje calculado |

## Tabla: MENSAJE
| Campo | Tipo | Restricción | Descripción |
|------|------|-------------|-------------|
| id_mensaje | SERIAL | PK | Identificador |
| id_match | INT | FK NOT NULL | Match asociado |
| id_emisor | INT | FK NOT NULL | Usuario que envía |
| contenido | TEXT | NOT NULL | Mensaje |
| fecha_hora | TIMESTAMP | NOT NULL | Momento |
| leido | BOOLEAN | DEFAULT FALSE | Estado de lectura |
