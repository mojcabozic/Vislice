STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'

class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
        self.crke = crke
    
    def napacne_crke(self):             #izpeljan seznam
        return [c for c in self.crke if c.upper() not in self.geslo.upper()] 

    #def pravilne_crke(self):            #s for loopom
    #    pravilne = []
    #    for i in self.geslo:
    #        if i.upper() in self.geslo.upper():
    #            pravilne.append(i)
    #
    #    return pravilne

    def pravilne_crke(self):
        return [c for c in self.crke if c.upper() in self.geslo.upper()] 

    def stevilo_napak(self):
        return len(self.napacne_crke()) #napacne crke so metoda

    def zmaga(self):
        return not self.poraz() and len(self.pravilne_crke()) == len(set(self.geslo))

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        pravilni_del = ""

        for i in self.geslo:
            if i.upper() in self.crke:
                pravilni_del += i.upper()
            else:
                pravilni_del += "_"

        return pravilni_del

    def nepravilni_ugibi(self):
       return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA

        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA

        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

    
with open("besede.txt") as f:
    bazen_besed = f.read().split() #read vrne niz, split pa seznam

import random

def nova_igra():
    geslo = random.choice(bazen_besed)

    return Igra(geslo)






