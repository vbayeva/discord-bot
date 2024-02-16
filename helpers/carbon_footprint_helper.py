import random

guide = ["Oszczędzaj energię: Wyłączaj światła, urządzenia elektroniczne i wtyczki, kiedy ich nie używasz",
         "Transport publiczny i carpooling: Korzystaj z transportu publicznego, aby zmniejszyć emisję CO2.",
         "Rower i chodzenie: Gdzie to możliwe, wybieraj rower lub idź pieszo.",
         "Dieta roślinna: Produkcja mięsa jest jednym z głównych źródeł emisji gazów cieplarnianych. Przejście na dietę bogatą w rośliny może znacząco zmniejszyć Twój ślad węglowy.",
         "Planuj zakupy: Kupuj tylko tyle, ile potrzebujesz, aby uniknąć marnowania żywności.",
         "Krótsze prysznice: Ogranicz czas spędzany pod prysznicem.",
         "Zakupy z drugiej ręki: Kupuj używane przedmioty zamiast nowych.",
         "Naprawiaj i ponownie używaj: Naprawiaj uszkodzone przedmioty, zamiast kupować nowe.",
         "Zminimalizuj użycie plastiku: Unikaj jednorazowych plastików, wybieraj produkty wielokrotnego użytku."
         ]

how_to_count_text = [
    "Wejdź na stronę carbonfootprint.com",
    "Wybierz opcję „Calculate your footprint",
    "Odpowiedz na szereg pytań dotyczących Twojego stylu życia, w tym transportu, zużycia energii w domu, podróży, diety i innych czynników.",
    "Po zakończeniu ankiety kalkulator przedstawi wynik Twojego śladu węglowego w tonach CO2 rocznie."
]

def get_random_guide():
    return random.choice(guide)

def get_how_to_count_footprint_text(index):
    return how_to_count_text[index]