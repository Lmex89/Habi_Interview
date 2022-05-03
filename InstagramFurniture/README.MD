Microservicio para Entrevista para Habi


 ** Se requiere python 3.8 
 ** Se requiere crear un virtual env, utilizando el commando pip install -r requierements.txt
 ** Se utilizo Django y DjangoRestFramework solo para conectar los endpoints 
 ** Se utilizo RawSqL para escribir a mano las queries necesarias para crear la funcionalidad
 del microservio de los inmuebles 

 Parte 1:

 Endpoint : /localhos:8000/api/v1/furniture GET LIST

 returna la sigueinte estructura:
        {
    "data": [
        {
            "id": 15,
            "property": {
                "price": 210000000,
                "address": "calle 23 #45-67",
                "city": "medellin",
                "description": "",
                "year": 2002
            },
            "status": "pre_venta",
            "update_date": "2021-04-12T22:23:56Z"
        },
        {
            "id": 43,
            "property": {
                "price": 210000000,
                "address": "calle 23 #45-67r",
                "city": "medellin",
                "description": "",
                "year": 2002
            },
            "status": "pre_venta",
            "update_date": "2021-04-10T13:24:56Z"
        }
    ]
}

y en los params es permitido enviar parametros :
Aqui un ejemplo:
    {{url}}/api/v1/furniture/?year=2002&status=[1,2,3]


Parte 2:

Modelo de DJango

Model ILikeitUser
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    property = models.ForeignKey(Property, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)


Model de la base de datos:

CREATE TABLE ILikeitUser (
    id int NOT NULL,
    user_id int NOT NULL,
    property_id int,
    created_at datetime,
    PRIMARY KEY (ID),
    FOREIGN KEY (User) REFERENCES auth_user(id)
);

ALTER TABLE `ILikeitUser` ADD UNIQUE `unique_index`(`user_is`, `property_id`,);

Solo es necesario crear un modelo que contenga id, como primary key 
que tenga como llave foranea a los usuarios, y el inmueble (property)
de tal manera que se pueda obtener el id de un usario registrado, y que este 
a su vez no pueda ser null, y como llave foranea a la tabla Property donde 
se pueda obtener a que inmueble se puede hacer hacer me gusta ...

Alterando la tabla para que se cree un unique_together de tal menera que un 
usuario registrado solo pueda darle me gusta a un unico inmuble y este no pueda
repetirse 