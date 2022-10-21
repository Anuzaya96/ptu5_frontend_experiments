#Sukurti programą, kuri turėtų statinį puslapį,
#  pvz. localhost:5000 su norimu tekstu 
# (rekomenduojama naudoti šablonus)

#Sukurti programą, kuri įvedus norimą žodį adreso eilutėje 
# (po / simbolio) ir paspaudus ENTER, atspausdintų jį 
# penkis kartus.


#Sukurti programą, kuri puslapyje localhost:
# 5000/keliamieji parodytų visus keliamuosius
#  metus nuo 1900 iki 2100 metų.


#Sukurti programą, kuri leistų įvesti metus ir 
# paspaudus patvirtinimo mygtuką parodytų, 
# ar jie yra keliamieji.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "The Most Important Day of Your Life "

@app.route("/next_page/<kartojimasis>")
def next_page(kartojimasis):
    kartojimasis = (kartojimasis + " ") * 5
    return render_template("next_page.html", kartojimasis=kartojimasis) 
    

@app.route("/keliamieji/")
def keliamieji_metai():
    keliamieji=[]
    metai = range(1900, 2101)
    for x in metai:
        if x%4 == 0 and (x%100 != 0 or x%400 ==0):
            keliamieji.append(x)

    return render_template("keliamieji.html", keliamieji=keliamieji)

#Sukurti programą, kuri leistų įvesti metus ir 
# paspaudus patvirtinimo mygtuką parodytų, 
# ar jie yra keliamieji.
# reikia int, 

@app.route("/ar_keliamieji/")
def ar_keliamieji():
    return render_template("ar_keliamieji.html")


@app.route("/keliamuju_rezultatas/")
def rezultatas():
    metai = int(request.args["metai"])
    if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
        rezultatas = "keliamieji"
    else:
        rezultatas = "ne keliamieji"
    return render_template("keliamuju_rezultatas.html", rezultatas=rezultatas, metai=metai)


if __name__ == "__main__":
    app.run(debug=True)

