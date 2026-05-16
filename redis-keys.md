erDiagram
    UNIVERSIDAD ||--o{ USUARIO : pertenece
    USUARIO ||--o{ HORARIO_DISPONIBLE : tiene
    TEMA ||--o{ ALIAS_TEMA : posee
    USUARIO ||--o{ USUARIO_TEMA : estudia
    TEMA ||--o{ USUARIO_TEMA : es_estudiado
    USUARIO ||--o{ MATCH : usuario1
    USUARIO ||--o{ MATCH : usuario2
    TEMA ||--o{ MATCH : tema
    MATCH ||--o{ MENSAJE : contiene

    UNIVERSIDAD {
        int id_universidad PK
        string nombre
        string pais
    }

    USUARIO {
        int id_usuario PK
        string nombre
        string email
        string contrasena_hash
        string pais
        string idioma
        int id_universidad FK
    }

    TEMA {
        int id_tema PK
        string nombre_estandar
        string area
    }

    ALIAS_TEMA {
        int id_alias PK
        string texto_alias
        string idioma
        int id_tema FK
    }

    USUARIO_TEMA {
        int id_usuario PK, FK
        int id_tema PK, FK
        string nivel
        string objetivo
    }

    HORARIO_DISPONIBLE {
        int id_horario PK
        string dia
        time hora_inicio
        time hora_fin
        string zona_horaria
        int id_usuario FK
    }

    MATCH {
        int id_match PK
        int id_usuario1 FK
        int id_usuario2 FK
        int id_tema FK
        string estado
        datetime fecha_match
        float puntaje_compatibilidad
    }

    MENSAJE {
        int id_mensaje PK
        int id_match FK
        int id_emisor FK
        string contenido
        datetime fecha_hora
        boolean leido
    }
