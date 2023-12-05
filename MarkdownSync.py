import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('markdown-sync-f5c89ff01724.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection("obsidian_vault").document("TestDoc002")
doc_ref.set({"Markdown": "BBBBBBBBBBB"})