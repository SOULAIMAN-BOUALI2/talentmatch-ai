# TalentMatch AI

TalentMatch AI est une plateforme intelligente de recrutement permettant d'importer des CV, d'extraire automatiquement les informations grâce à Gemini AI, de les stocker dans PostgreSQL et de rechercher les meilleurs candidats à partir d'une requête en langage naturel.

---

# Prérequis

- Python 3.11+ (ou version utilisée pour le projet)
- PostgreSQL
- Git
- Un environnement virtuel Python
- Une clé API Google Gemini

---

# 1. Cloner le projet

```bash
git clone <repository_url>

cd talentmatch-ai
```

---

# 2. Créer l'environnement virtuel

Windows

```bash
python -m venv venv
```

Linux / Mac

```bash
python3 -m venv venv
```

---

# 3. Activer l'environnement virtuel

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

# 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# 5. Configurer les variables d'environnement

Créer un fichier :

```
.env
```

Ajouter :

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/talentmatch_ai

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 6. Créer la base PostgreSQL

Créer une base :

```
talentmatch_ai
```

---

# 7. Lancer le Backend FastAPI

Depuis la racine du projet :

```bash
uvicorn api.main:app --reload
```

API disponible sur :

```
http://127.0.0.1:8000
```

Documentation :

```
http://127.0.0.1:8000/docs
```

---

# 8. Lancer Streamlit

Ouvrir un deuxième terminal.

Activer l'environnement et éxecuter cette commande :

```bash
venv\Scripts\activate
```

Puis :

```bash
streamlit run frontend/app.py
```

Interface disponible sur :

```
http://localhost:8501
```

---

# 9. Architecture du projet

```
talentmatch-ai/

api/
│
├── database/
├── models/
├── routers/
├── schemas/
└── services/

ai/
│
├── embeddings/
├── llm/
├── parser/
└── scoring/

frontend/
│
├── app.py
└── pages/

storage/
│
└── cvs/

requirements.txt

README.md
```

---

# Workflow

Le pipeline est le suivant :

```
Upload CV

↓

Lecture PDF

↓

Gemini AI

↓

Extraction des informations

↓

Embedding

↓

PostgreSQL

↓

Recherche RH

↓

Scoring

↓

Classement des candidats
```

---

# Fonctionnalités

- Upload de plusieurs CV PDF
- Extraction automatique avec Gemini AI
- Génération d'embeddings
- Stockage PostgreSQL
- Recherche en langage naturel
- Calcul automatique du score des candidats

---

# Technologies

- Python
- FastAPI
- Streamlit
- PostgreSQL
- SQLAlchemy
- Google Gemini
- SentenceTransformers
- PyMuPDF
- Pydantic