# Strategia COVE Polska

Publiczna strona materiałów do konsultacji dotyczących rozwoju COVE Polska we Wrocławiu.

Zawiera plan strategii, karty warsztatowe, rejestr źródeł, analizę IBE/WEF/PwC oraz cele edukacyjne dotyczące wiarygodności informacji i AI.

## Aktualizacja

Edytuj odpowiedni plik Markdown w `materialy/`, następnie uruchom `python3 build.py` (wymagany pakiet Python `Markdown==3.10.3`). Zatwierdź źródła i wygenerowany HTML. GitHub Pages publikuje katalog główny gałęzi `main`.

Źródłowe raporty zewnętrzne pozostają na stronach wydawców; serwis zawiera odnośniki. Materiał jest propozycją do konsultacji, nie przyjętą strategią.

## Dział Katapult

`katapult.html` zawiera polskie omówienia, siedem etapów, jedenaście pozycji katalogu, sześć obszarów współpracy i siedem autorskich kart. Nie jest pełnym ani oficjalnym tłumaczeniem publikacji Katapult. Autorstwo materiałów wskazano przy każdej pozycji; oryginały są podlinkowane u wydawców.

Treści działu edytuje się w `katapult_content.py`, po czym uruchamia `python3 katapult_content.py` i `python3 build.py`. Rejestr linków jest zapisany w `katapult-linki.json` i `materialy/Katapult_linki.md`. Kopie pobranych oryginałów są przechowywane w lokalnym archiwum poza publicznym repozytorium.

Karty warsztatowe zapisują notatki wyłącznie w localStorage przeglądarki. Możliwy jest eksport JSON i wydruk. Nie ma serwera zbierającego treść notatek.
