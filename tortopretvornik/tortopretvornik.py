import bottle
from model import *

recept = Recept([], None)


@bottle.get("/")
def spletna_stran():
    return bottle.template("SpletnePredloge/osnovna.tpl")


@bottle.post("/dodaj_polmer1/dodaj")
def dodajPolmer1():
    polmer = float(bottle.request.forms.get("polmer"))
    if recept.pekac == None:
        recept.pekac = Pekac(None, None)
    recept.pekac.polmer1 = polmer
    bottle.redirect("/")


@bottle.post("/dodaj_polmer1/")
def dodaj_polmer1():
    return bottle.template("SpletnePredloge/vnos_polmera1.tpl")


@bottle.post("/dodaj_polmer2/dodaj")
def dodaj_polmer2():
    polmer = float(bottle.request.forms.get("polmer"))
    if recept.pekac == None:
        recept.pekac = Pekac(None, None)
    recept.pekac.polmer2 = polmer
    bottle.redirect("/")


@bottle.post("/dodaj_polmer2/")
def dodaj_polmer2():
    return bottle.template("SpletnePredloge/vnos_polmera2.tpl")


@bottle.post("/dodaj_kolicino/")
def dodaj_kolicino():
    return bottle.template("SpletnePredloge/vnos_kolicine.tpl")


@bottle.post("/dodaj_kolicino/dodaj")
def pomozna():
    sestavina = bottle.request.forms.get("sestavina")
    kolicina = float(bottle.request.forms.get("kolicina"))
    mera = bottle.request.forms.get("tip")
    sestavina2 = Sestavina(kolicina, sestavina, mera)
    recept.dodaj_sestavino(sestavina2)
    bottle.redirect("/")


@bottle.get("/pretvori/")
def pretvorjeno2():
    recept.Izracunaj()
    return bottle.template("SpletnePredloge/izpis_kolicin.tpl", seznam=recept.sestavine)


bottle.run(debug=True, reloader=True)
