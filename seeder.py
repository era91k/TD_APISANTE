from model_patient import Patient
from pymongo import MongoClient

# 1. Établir une connexion avec MongoDB
client = MongoClient("mongo_sante")

# 2. Sélectionner une base de données
db = client.databases

# 3. Sélectionner une collection
collection = db.Patient

# 4. Insérer des objets dans la collection
patient = {"prenom": "hendy", 
           "nom": "laplume", 
           "ssn": 1990395239145
        }

collection.insert_one(patient)

# 5. Afficher les objets insérés
resultats = collection.find()
for resultat in resultats:
    print(resultat)