import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import io
import os

# Use a service account.
cred = credentials.Certificate('markdown-sync-f5c89ff01724.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

directory = "example_drive"


#files directly updated in the firebase store get messed up. dont do it
#reading and writing to/from via disc works perfectly though
def writeFiles():
    for l in os.listdir(directory):
        f = open(f"{directory}/{l}", "r")
        doc_ref = db.collection("obsidian_vault").document(l)
        doc_ref.set({"Markdown": f.read()})


def readFiles():
    for doc in db.collection("obsidian_vault").stream():
        f = open(f"{directory}/{doc.id}", "w")
        contents = doc.to_dict().get("Markdown")
        print(f"{doc.id}: {contents}")
        f.write(contents)


writeFiles()
readFiles()