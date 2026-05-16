# 01 — Caso de Estudio: UniMatch 2.0

## Nombre del sistema
**UniMatch 2.0 — Plataforma Global de Match Académico por Temas**

## Descripción general
UniMatch 2.0 es una plataforma orientada a estudiantes universitarios y autodidactas que desean encontrar compañeros de estudio para aprender, practicar o repasar un contenido específico.

A diferencia de plataformas tradicionales, UniMatch no realiza coincidencias únicamente por universidad o materia, sino por:

- **Tema exacto**
- **Nivel de conocimiento** (básico / intermedio / avanzado)
- **Objetivo** (aprender / practicar / repasar / explicar)
- **Idioma**
- **Disponibilidad horaria**, incluyendo zona horaria
- **Preferencias de interacción** (chat asincrónico o sesiones en vivo)

## Alcance académico del proyecto
Este caso de estudio fue diseñado para la materia **Bases de Datos II** con el objetivo de aplicar un enfoque **políglota**, combinando tecnologías de datos complementarias:

- PostgreSQL como núcleo transaccional.
- Redis como sistema de almacenamiento clave-valor para caché y sesiones.
- Neo4j como base de datos orientada a grafos para recomendaciones y análisis de relaciones.

## Actores involucrados
- **Usuario estudiante**: registra su perfil, selecciona temas y busca matches.
- **Sistema de matching**: calcula compatibilidad y propone candidatos.
- **Administrador (rol futuro)**: podría auditar contenidos, usuarios y reportes.

## Objetivo del sistema
Facilitar el aprendizaje colaborativo y reducir la deserción académica generada por la falta de apoyo y acompañamiento.

UniMatch 2.0 busca que cada estudiante encuentre rápidamente a otra persona que esté estudiando el mismo tema y que pueda complementar su objetivo.

## Suposiciones del proyecto
- Los usuarios cuentan con acceso a internet.
- Los usuarios completan su perfil de forma veraz.
- El sistema no reemplaza a un docente, sino que facilita colaboración entre pares.

## Entregables principales
- Modelo relacional PostgreSQL con constraints e índices.
- Diseño de claves y estructuras en Redis.
- Diseño de grafo y consultas en Neo4j.
- DAO (Data Access Object) para las tres bases de datos.
- Documentación completa en Markdown.
