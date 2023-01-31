# test_senscritique
Ce repository est ma réponse au test technique pour le poste de DevOps chez SensCritique

On peut lancer l'API (Flask + Redis) avec 
```
docker-compose up --build
```

L'interface tournera sur **http://localhost:5000** 

`GET /product/<id>` - Attention, la base de donnée est initialement vide, bien que persistente

`POST /product/<id>` - Le fichier `add_product.py` permet d'ajouter un élément facilement (On peut bien évidement agir autrement, comme utiliser Postman à condition de bien respecter le format des arguments.
