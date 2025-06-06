from neo4j import GraphDatabase
import os

# ✅ Connexion sécurisée à Neo4j
URI = "neo4j+s://99060d00.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = os.getenv("NEO4J_PASSWORD", "owlnqPNurSDQgcwHN9n-tZy6LEM7pCZoLiLk1X0M6JM")  # ou remplace par ton mot de passe directement

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def create_patient_node(data):
    with driver.session() as session:
        session.run("""
            MERGE (p:Patient {name: $name})
            SET p.age = $age,
                p.sex = $sex,
                p.diagnosis = $diagnosis,
                p.protocol = $protocol,
                p.stade = $stade,
                p.doctor = $doctor
        """, {
            "name": data.get("patient"),
            "age": data.get("age"),
            "sex": data.get("sex"),
            "diagnosis": data.get("diagnosis"),
            "protocol": data.get("protocol"),
            "stade": data.get("stade"),
            "doctor": data.get("doctor")
        })

def get_all_patients():
    with driver.session() as session:
        result = session.run("MATCH (p:Patient) RETURN p")
        return [dict(record["p"]) for record in result]
