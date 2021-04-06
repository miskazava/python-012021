from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()

cilova_mena = input("Zadej cílovou měnu: ")
pozadovano_v_cilove_mene = input("Zadej požadované množství: ")
pozadovano_v_cilove_mene = int(pozadovano_v_cilove_mene)
cena_v_korunach = prevodnik.convert(cilova_mena, 'CZK', pozadovano_v_cilove_mene)
print(f"Pro získání {pozadovano_v_cilove_mene} {cilova_mena} budete potřeba {cena_v_korunach} CZK.")