import urllib.request
import csv

# urllib.request.urlretrieve("https://i.imgur.com/e1zA7Ql.png", "Img/img.png")


def dowloader(hoja):
    f = open('Data/'+hoja+'.csv', 'r')

    with f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            print("Descargando ", row['Nombre'], " desde ", row['Column1'], "a ", hoja)
            filename = "Img/"+hoja+"/"+row['Nombre']+".png"
            urllib.request.urlretrieve(row['Column1'], filename)


dowloader("Statblock")

dowloader("Race")

