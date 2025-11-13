from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import session
from database import SessionLocal
from DL.detect_and_predict import emotion_detection
from models.model import PersonCreate, PersonResponse, Person
from database import Base, engine, get_db 
from datetime import datetime
import uuid, aiofiles


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/predict_emotion")
async def predict_emotion(file: UploadFile = File(...), db: session = Depends(get_db)):
    images_type = ["image/jpeg", "image/png", "image/jpg"]

    if file.content_type not in images_type:
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    file_ext = file.filename.split(".")[-1]
    temp_filename = f"{uuid.uuid4()}.{file_ext}"

    async with aiofiles.open(temp_filename, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    # contents = file.file.read()
    emotion, confidence = emotion_detection(temp_filename)


    if hasattr(confidence, "numpy"):
        confidence = float(confidence.numpy())

    # if emotion is None:
    #     raise HTTPException(status_code=404, detail="Aucun visage detecte")

    new_entry = Person(
        emotion=emotion,
        confidence=confidence
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return {new_entry}


@app.get("/predictions", response_model=list[PersonResponse])
def predi(db: session = Depends(get_db)):
    records = db.query(Person).all()
    return records










#     if file.content_typenot not in ALLOWRD_TYPES:
#         raise HTTPException(status_code=400, detail=f"type non autorise: (file.content_type)")
    
#     file_ext = file.filename.split(".")
#     temp_filename = f"{uuid.uuid4()}.{file_ext}"
#     with open (temp_filename, "wb") as buffer
#     file.file.close()

#     try:
#         img= cv2








#     #  Enregistrer l'image envoyée
#     file_path = "DL/temp_image.png"
#     with open(file_path, "wb") as f:
#         f.write(await file.read())

#     #  Lancer le script detect_and_predict.py
#     result = subprocess.run(["python", "DL/detect_and_predict.py"], capture_output=True, text=True)

#     #  Lire ce que le script a affiché
#     output = result.stdout.strip()
#     if not output:
#         emotion, confidence = "unknown", 0.0
#     else:
#         emotion, confidence = output.split()
#         confidence = float(confidence)

#     # 4 Sauvegarder dans la base de données
#     new_person = Person(
#         emotion=emotion,
#         confidence=confidence,
#         created_at=datetime.utcnow()
#     )
#     db.add(new_person)
#     db.commit()
#     db.refresh(new_person)

#     return new_person



# @app.get("/history", response_model=PersonResponse)
# def get_history(db: session = Depends(get_db)):
#     records = db.query(Person).all()
#     return records