class Kotatko:
        def zamnoukej(self):
            print("Mnau!")
            print(f"{self.jmeno}: Mnau!")

mourek = Kotatko()
mourek.jmeno = "Mourek"

micka = Kotatko()
micka.jmeno = "Micka"

print(mourek.jmeno)
print(micka.jmeno)
mourek.zamnoukej()
micka.zamnoukej()

class Kotatko:
    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko()
mourek.jmeno = 'Mourek'
mourek.snez('ryba')


class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f'<Kotatko jmenem {self.jmeno}>'

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

class Stenatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(selfself, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutna!")

    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutna!")

class Kotatko(Zviratko):
    def zamnoukej(self):
        print(f"{self.jmeno}: Mnau!")

class Stenatko(Zviratko):
    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')

class Kotatko(Zviratko):
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi vubec nechutna!")

micka = Kotatko('Micka')
micka.snez('granule')

class Kotatko(Zviratko):
    def snez(self, jidlo):
        print(f"({self.jmeno} na {jidlo} chvíli fascinovaně kouká)")
        super().snez(jidlo)


micka = Kotatko('Micka')
micka.snez('granule')

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


standa = Hadatko('Stanislav')
standa.snez('myš')

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('flákota')

class Zviratko:
    def __init__(self, jmeno):
            self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")


class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Mňau!")


class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Haf!")

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez('flákota')