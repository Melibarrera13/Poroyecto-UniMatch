"""main.py - Ejecución de ejemplo (UniMatch 2.0)

Este archivo demuestra el uso de la capa DAO y del MatchingService.
No representa un servidor real, sino una prueba académica de integración.

Requisitos:
- PostgreSQL con scripts ejecutados
- Redis activo
- Neo4j activo
"""

from src.services.matching_service import MatchingService


def main():
    service = MatchingService()

    user_id = 1
    topic_id = 1

    print("=== Recomendaciones para Usuario 1 (Tema 1) ===")
    recomendaciones = service.recomendar_matches(user_id=user_id, topic_id=topic_id, limit=5)

    for r in recomendaciones:
        print(f"- Usuario {r['id_usuario']} | {r['nombre']} | Puntaje: {r['puntaje']}")

    if recomendaciones:
        candidato = recomendaciones[0]
        print("\nConfirmando match con el candidato mejor puntuado...")
        match_id = service.confirmar_match(
            user_id_1=user_id,
            user_id_2=candidato["id_usuario"],
            topic_id=topic_id,
            score=candidato["puntaje"]
        )
        print(f"Match creado con ID: {match_id}")


if __name__ == "__main__":
    main()
