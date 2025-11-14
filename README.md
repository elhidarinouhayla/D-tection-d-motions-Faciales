# Detection-demotions-Faciales



## Objectif du projet

Les maladies cardiovasculaires sont la première cause de mortalité dans le monde, responsables de 17,9 millions de décès par an.

L’objectif de ce projet est de fournir une API capable d’estimer le risque de maladie cardiovasculaire d’un patient à partir de ses données cliniques.


## Structure du projet
```
emotion_api/
│
├── DL/                          
│   ├── detect_and_predict.py     
│   ├── emotion_cnn_model.ipynb  
│   ├── emotion_cnn_model.keras   
│   ├── haarcascade.xml           
│   └── data/                     
│       ├── train/                
│       └── test/                
├── models/                       
│   └── model
│
├── test/                        
│   └── test_main.py
│
├── .env                         
├── .gitignore                     
├── config.py                     
├── database.py                  
├── main.py                       
├── README.md                       
└── requirements.txt               

```


---

## Installation

1. Cloner le dépôt GitHub :  

```shell
    git https://github.com/elhidarinouhayla/D-tection-d-motions-Faciales.git
    cd project
```

2. Créer un environnement virtuel :

 - Linux / Mac :
```shell
    python -m venv venv
    source venv/bin/activate
```
 - Windows :
```shell
    python -m venv venv
    venv\Scripts\activate
```

3. Installer les dépendances :

```shell
    pip install -r requirements.txt
```

4. Lancer l’API en mode développement :

```shell
    uvicorn main:app --reload
```

 - L’API sera accessible à l’adresse : http://127.0.0.1:8000

 - Documentation interactive Swagger : http://127.0.0.1:8000/docs

Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.


## 🧠 Partie deep learning
