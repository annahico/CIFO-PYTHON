import io
import re

patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")


arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')
llistadecadenes = [cadena.replace(",,", ",ND,").replace(
    '""', '') for cadena in arxiu.readlines()]

matriu = []

# Processar cada línia i trobar coincidències
for cadena in llistadecadenes:
    temp = patro.findall(cadena)
    matriu.append(temp)

# Inicialitzar llistes per a pel·lícules i puntuacions
movies = []
scores = []

# Extracció de pel·lícules i puntuacions
for llista in matriu[1:]:  # Comencem des de 1 per saltar-nos l'encapçalament
    try:
        movies.append(llista[1])  # Nom de la pel·lícula
        scores.append(float(llista[6]))  # Puntuació
    except (ValueError, IndexError):
        continue  # Ignorar si hi ha un error en la conversió

# Anàlisi de les pel·lícules amb puntuació
num_movies = len(scores)
if num_movies == 0:
    print("No hi ha pel·lícules amb puntuació vàlida.")
else:
    # 1. Pel·lícula amb la puntuació més alta
    best_score = max(scores)
    best_movie_index = scores.index(best_score)
    best_movie = movies[best_movie_index]
    print(f"La pel·lícula amb la puntuació més alta és: {
          best_movie} amb un {best_score}")

    # 2. Pel·lícula amb la puntuació més baixa
    worst_score = min(scores)
    worst_movie_index = scores.index(worst_score)
    worst_movie = movies[worst_movie_index]
    print(f"La pel·lícula amb la puntuació més baixa és: {
          worst_movie} amb un {worst_score}")

    # 3. Mitjana de puntuacions
    mean_score = sum(scores) / num_movies
    print(f"La puntuació mitjana de totes les pel·lícules és: {
          mean_score:.2f}")

    # 4. Número total de pel·lícules amb puntuació vàlida
    print(f"El número total de pel·lícules amb puntuació vàlida és: {
          num_movies}")
