import spacy
import re

nlp = spacy.load("en_core_sci_sm")

protocol_doses = {
    "FEC": {
        "5-FU": 500,
        "Epirubicin": 100,
        "Cyclophosphamide": 500
    },
    "AC": {
        "Doxorubicin": 60,
        "Cyclophosphamide": 600
    }
}

def calculate_bsa(weight, height):
    return round(0.007184 * (weight ** 0.425) * (height ** 0.725), 2)

def extract_info(note):
    doc = nlp(note)
    weight = re.search(r'(\d{2,3})\s?kg', note)
    height = re.search(r'(\d{3})\s?cm', note)
    protocol = re.search(r'(FEC|AC)', note, re.IGNORECASE)
    diagnosis = None

    for ent in doc.ents:
        if any(x in ent.text.lower() for x in ['cancer', 'lymphoma', 'leukemia']):
            diagnosis = ent.text
            break

    result = {
        "diagnosis": diagnosis,
        "weight_kg": int(weight.group(1)) if weight else None,
        "height_cm": int(height.group(1)) if height else None,
        "protocol": protocol.group(1).upper() if protocol else None,
        "intent": "start_chemotherapy"
    }

    if result["weight_kg"] and result["height_cm"] and result["protocol"] in protocol_doses:
        bsa = calculate_bsa(result["weight_kg"], result["height_cm"])
        result["bsa"] = bsa
        result["dosage"] = {drug: round(dose * bsa, 1) for drug, dose in protocol_doses[result["protocol"]].items()}

    return result
import spacy
import re

nlp = spacy.load("en_core_sci_sm")

protocol_doses = {
    "FEC": {
        "5-FU": 500,
        "Epirubicin": 100,
        "Cyclophosphamide": 500
    },
    "AC": {
        "Doxorubicin": 60,
        "Cyclophosphamide": 600
    }
}

def calculate_bsa(weight, height):
    return round(0.007184 * (weight ** 0.425) * (height ** 0.725), 2)

def extract_info(note):
    doc = nlp(note)
    weight = re.search(r'(\d{2,3})\s?kg', note)
    height = re.search(r'(\d{3})\s?cm', note)
    protocol = re.search(r'(FEC|AC)', note, re.IGNORECASE)
    diagnosis = None

    for ent in doc.ents:
        if any(x in ent.text.lower() for x in ['cancer', 'lymphoma', 'leukemia']):
            diagnosis = ent.text
            break

    result = {
        "diagnosis": diagnosis,
        "weight_kg": int(weight.group(1)) if weight else None,
        "height_cm": int(height.group(1)) if height else None,
        "protocol": protocol.group(1).upper() if protocol else None,
        "intent": "start_chemotherapy"
    }

    if result["weight_kg"] and result["height_cm"] and result["protocol"] in protocol_doses:
        bsa = calculate_bsa(result["weight_kg"], result["height_cm"])
        result["bsa"] = bsa
        result["dosage"] = {drug: round(dose * bsa, 1) for drug, dose in protocol_doses[result["protocol"]].items()}

    return result
