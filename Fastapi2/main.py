from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app= FastAPI(title= 'Videojuegos', 
            version='1.0.1')

#http://127.0.0.1:8000

@app.get("/")
def index(): 
    return 'HOLA A MUNDO'

@app.get('/user_id/{str}')
def userdata(user_id):
    '''Ingrese el usuario, retorna el dinero gastado por el mismo, porcentaje de recomendacion y cantidad de items'''
    df=pd.read_csv('Funciones/userdata1.csv')
    usuario = df[df['user_id'] == user_id]
    
    if len(usuario) == 0:
        return "El usuario no existe."
    
    dinero_gastado = usuario['dinero_gastado'].values[0]
    porcentaje_recomendacion = usuario['porcentaje de recomendación'].values[0]
    items_count = usuario['items_count'].values[0]
    
    return dinero_gastado, porcentaje_recomendacion, items_count
    
