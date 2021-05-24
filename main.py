import functions
import recognizeCharacter
import database

if __name__ == '__main__':
    img = functions.konturAlKırp()
    plaka = recognizeCharacter.karakterTanıma(img)
    plaka = plaka.replace(" ", "")
    plaka = plaka.upper()
    database.aracGirisi(plaka)

