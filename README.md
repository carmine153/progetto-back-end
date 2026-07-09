# Polling Application API

**Studente:** Carmine Pignatiello 

## Informazioni Progetto
- **Tipo di progetto:** REST API
- **Framework utilizzato:** Django, Django REST Framework

## Descrizione
Applicazione per la gestione di sondaggi online. Il sistema permette agli utenti di creare, visualizzare e votare sondaggi. Include una logica di protezione delle risorse basata sulla proprietà dell'oggetto e un ciclo di vita del sondaggio.

## Funzionalità Implementate
### Utente (Autenticato)
- Creazione, modifica e cancellazione dei propri sondaggi.
- Votazione su sondaggi attivi.
### Pubblico (Non autenticato)
- Visualizzazione lista sondaggi.
- Visualizzazione risultati sondaggi.
### Amministratore
- Gestione totale tramite pannello amministrativo Django.

## Istruzioni di Installazione (Locale)
1. Clonare il repository: `git clone https://github.com/carmine153/progetto-back-end`
2. Creare un ambiente virtuale: `python -m venv venv`
3. Attivare l'ambiente: `venv\Scripts\activate` (Windows)
4. Installare le dipendenze: `pip install -r requirements.txt`
5. Applicare le migrazioni: `python manage.py migrate`
6. Popolare il database con dati demo: 'python manage.py seed_data'
7. Avviare il server: `python manage.py runserver`

## Database e Dati Demo
- **File Database:** `db.sqlite3`
- **Contenuto:** Il database include i dati demo generati tramite lo script `seed_data.py`.

## Account Demo
| Username | Password | Ruolo |
| :--- | :--- | :--- |
| `admin_demo` | `admin12345` | Amministratore |
| `user_demo` | `user12345` | Utente Standard |

## Online Deployment
- [Link al progetto online]: *[Inserisci qui il link al deployment, es. Render/PythonAnywhere]*

## API Endpoints
| Metodo | URL | Auth | Ruolo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/polls/` | No | Tutti | Lista sondaggi |
| `POST` | `/api/polls/` | Sì | User | Crea sondaggio |
| `POST` | `/api/polls/{id}/vote/` | Sì | User | Vota sondaggio |
| `GET` | `/api/polls/{id}/results/` | No | Tutti | Risultati sondaggio |
| `DELETE` | `/api/polls/{id}/` | Sì | Owner | Cancella sondaggio |

*Nota: Per i campi JSON (request body), inviare oggetti strutturati secondo il modello (es. `{"title": "Titolo", "question_text": "Domanda"}`).*

## Utilizzo con HTTPie
Per testare le API da terminale tramite HTTPie:

1. **Installazione**: `pip install httpie`
2. **Base URL**: `http://127.0.0.1:8000/api/`
3. **Login**: 
   `http POST :8000/api-token-auth/ username=user_demo password=user12345`
4. **Utilizzo Token**: 
   `http POST :8000/api/polls/ "Authorization: Token <TUO_TOKEN>" title="Nuovo Sondaggio"`


## Test di Verifica (Demo per il Docente)
Nell'interfaccia sono già presenti 3 sondaggi di prova utili a spiegare il funzionamento.

### 1. Test  Chiusura Sondaggio
Verifica che non sia possibile votare un sondaggio disattivato.
- **Sondaggio**: "Sondaggio Chiuso - Test Voto" (ID del sondaggio chiuso)
- **Azione**: `POST /api/polls/{id}/vote/` con `{"choice_id": X}`
- **Risultato Atteso**: `400 Bad Request` ("Il sondaggio è chiuso")

### 2. Test Permessi di Sicurezza
Verifica che un utente standard non possa modificare i sondaggi altrui.
- **Sondaggio**: "Sondaggio di Admin - Test Sicurezza" (ID creato da admin)
- **Azione**: `OPTIONS-DELETE /api/polls/{id}/` (autenticato come `user_demo`)
- **Risultato Atteso**: 'detail': 'You do not have permission to perform this action.' oppure 403

### 3. Test Flusso di Successo
Verifica il corretto funzionamento delle operazioni permesse.
- **Sondaggio**: "Sondaggio di User - Test OK"
- **Azione A**: `POST /api/polls/{id}/vote/` con `{"choice_id": X}` (autenticato come `user_demo`)
- **Azione B**: `GET /api/polls/{id}/results/`
- **Risultato Atteso**: `200 OK` e contatore voti aggiornato.   
