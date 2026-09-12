from pathlib import Path
import json,html
R=Path(__file__).resolve().parent
H=html.escape
BASE='https://www.wearekatapult.eu/files/'
road='https://wearekatapult.eu/tools/roadmap-to-a-centre-of-vocational-excellence/'
# Polish summaries, not translations of the source publications.
tools=[
('interesariusze','Analiza interesariuszy','Stakeholder Analysis','Artykuł + dostęp na zapytanie','https://wearekatapult.eu/tools/stakeholderanalysis','Katapult',1,
 'Badanie potrzeb, oczekiwań i oceny współpracy przez osoby należące do partnerstwa oraz pozostające poza nim. Wyniki służą rozmowie o dalszym kierunku działania. Katapult wskazuje, że uczestnicy istniejącej współpracy mogą oceniać ją bardziej pozytywnie niż osoby z zewnątrz.',
 'Właściwy kwestionariusz jest dostępny po kontakcie z Katapult. Przycisk pobierania na stronie prowadzi do innego materiału: Reflection on Collaboration.',
 'Zaprosić do diagnozy także firmy i szkoły, które dotąd nie uczestniczyły w COVE Polska.'),
('pestle','Skan otoczenia PESTLE','Vocational Excellence Scanning tool — Context scan','PDF · 6 stron',BASE+'Tools%20voor%20CoVE/Tool-PESTLE-scan.pdf','PoVE Water; materiał udostępniany przez Katapult',1,
 'Skan łączy sześć wymiarów otoczenia — polityczny, ekonomiczny, społeczny, technologiczny, prawny i środowiskowy — z rozpoznaniem mocnych i słabych stron, szans oraz zagrożeń. Oryginał powstał dla ekosystemu sektora wodnego i zawiera przykład szkocki.',
 'Pobrano PDF. Przykłady sektorowe wymagają sprawdzenia przed wykorzystaniem w innym regionie.',
 'Dla każdego ustalenia zapisać źródło, datę i konsekwencję dla jednej proponowanej usługi.'),
('bmc','Model działania partnerstwa','Business Model Canvas','PDF · 4 strony',BASE+'downloads/BMC%20English.pdf','Katapult i New Business Lab, na podstawie Osterwaldera i Pigneura',2,
 'Dziewięciopolowy model pomaga uzgodnić, komu partnerstwo służy, jaką wartość zapewnia, jak działa i jak się utrzymuje. W wersji dla współpracy edukacji i firm uwzględnia korzyści gospodarcze, społeczne i obywatelskie. Może być wielokrotnie aktualizowany.',
 'Pobrano PDF. Dostępny jest również artykuł Katapult objaśniający użycie narzędzia.',
 'Oddzielnie porównać wariant sekretariatu sieci i wariant operatora szkoleń; nie mieszać ich budżetów.'),
('empatia','Perspektywa odbiorcy','Empathy Map','PNG · plansza',BASE+'Tools%20voor%20CoVE/Empathy-map.png','Event Design Collective GmbH (2018); adaptacja z XPLANE; link w Katapult',2,
 'Plansza porządkuje spojrzenie odbiorcy: jego otoczenie, wypowiedzi, zachowania, myśli, odczucia, trudności i oczekiwane korzyści. Wspiera rozumienie sytuacji konkretnej grupy zamiast projektowania oferty wyłącznie z perspektywy organizatora.',
 'Pobrano PNG. Autorstwo podano zgodnie ze stopką planszy; nie jest to samodzielna publikacja autorstwa Katapult.',
 'Przygotować osobne profile nauczyciela, ucznia i mentora z MŚP. Oddzielić wypowiedzi z rozmów od hipotez zespołu.'),
('projekt','Karta projektu','Action plan','PDF · 6 stron',BASE+'Tools%20voor%20CoVE/Action-plan-format-projects.pdf','Format udostępniony przez Katapult w roadmapie',3,
 'Format prowadzi od uzasadnienia projektu przez cel, zakres i produkty do organizacji realizacji. Łączy planowane rezultaty z przeszkodami oraz działaniami, które mają je usunąć. Ułatwia określenie granic projektu i zasobów potrzebnych do jego wykonania.',
 'Pobrano PDF. W oryginale pojawia się dzielenie rocznej wartości przez „365 working days”; takiego założenia nie przenosimy do polskiej karty.',
 'Dla pilotażu wiarygodności AI ustalić zadanie końcowe, kryterium jakości, eksperta branżowego i koszt obsługi.'),
('warsztaty','Angażowanie partnerów','Workshops','Oferta warsztatów',road,'Katapult',4,
 'Roadmapa wskazuje warsztaty dotyczące współpracy z MŚP, opowiadania o przedsięwzięciu, komunikacji i prowadzenia relacji z partnerami.',
 'W roadmapie nie udostępniono plików tych warsztatów. Kontakt wskazany przez autora: hello@wearekatapult.eu.',
 'Sprawdzić propozycję usługi w rozmowie z trzema firmami; zapisać warunki, przy których rzeczywiście wezmą udział.'),
('porozumienie','Porozumienie o współpracy','CoVE Water Blueprint / MoU','PDF · 14 stron',BASE+'Tools%20voor%20CoVE/Blueprint-cooperation-agreement-CoVE.pdf','Platform of Vocational Excellence Water; udostępnienie Katapult',5,
 'Przykład porozumienia dla regionalnego CoVE służy opisaniu współpracy, ról, działań i wkładów partnerów. Dokument zawiera przykładowe rozwiązania organizacyjne i finansowe do dostosowania do konkretnego partnerstwa.',
 'Pobrano PDF. To materiał wyjściowy do uzgodnień, a nie gotowa umowa dla polskiej instytucji.',
 'Uzgodnić gospodarza środków, zasady podejmowania decyzji, dostęp do zasobów oraz warunki wejścia i wyjścia z partnerstwa.'),
('dojrzalosc','Dojrzałość partnerstwa','CoVE Phase Model','PDF · 10 stron',BASE+'Tools%20voor%20CoVE/Phase%20model.pdf','The Innovation Family; udostępnienie Katapult; wersja 20231207',5,
 'Model wyróżnia pięć poziomów: rozpoczęcie, rozwijanie, walidację, dalszy rozwój i trwałość. Pomaga rozmawiać o przygotowaniu organizacji, jej ofercie i zdolności do współpracy. Zestaw obejmuje cztery wymiary, po cztery kryteria w każdym.',
 'Pobrano PDF. Pięć poziomów dojrzałości to inny podział niż siedem etapów roadmapy.',
 'Ocenić oddzielnie gotowość zespołu, potwierdzony popyt i zasoby. Każdą ocenę poprzeć dowodem.'),
('peer','Przegląd koleżeński','Peer Reviews','PDF · 22 strony',BASE+'Tools%20voor%20CoVE/Peer%20Reviews.pdf','The Innovation Family; udostępnienie Katapult; wersja 20231207',6,
 'Przegląd organizują osoby z innych centrów, które poznają dokumentację i rozmawiają z uczestnikami partnerstwa. Jego wartość wynika z zewnętrznej perspektywy, wymiany doświadczeń i zaleceń dotyczących rozwoju. Materiał opisuje role zespołu oraz przebieg przygotowania, wizyty i informacji zwrotnej.',
 'Pobrano PDF z artykułu „Peer Review”. Należy uzgodnić zakres i dostępność recenzentów; samoocena nie oznacza certyfikacji.',
 'Poprosić recenzentów o ocenę dwóch pilotaży, podziału odpowiedzialności i możliwości utrzymania sekretariatu.'),
('refleksja','Przegląd jakości współpracy','Reflection on Collaboration','PDF · 7 stron','https://wearekatapult.eu/files/downloads/Tool%20Reflection%20on%20Collaboration.pdf','Common Eye we współpracy z PTvT i VSLS; plansze wskazują VO-raad',6,
 'Materiał wspiera rozmowę o wspólnych ambicjach, interesach, relacjach, organizacji i przebiegu współpracy. Łączy rozpoznanie trudności z zapisem dalszych ustaleń. Powrót do notatek pozwala sprawdzić, czy uzgodnione działania zostały wykonane.',
 'Pobrano PDF z przycisku na stronie Stakeholder Analysis. To narzędzie refleksji nad współpracą, nie kwestionariusz badania interesariuszy.',
 'Po pierwszym pilotażu przeprowadzić rozmowę partnerów o rzeczywistym obciążeniu, korzyściach i niewykonanych zobowiązaniach.'),
('skan','Diagnoza ekosystemu w PoVE Water','Scanning tool Platform of Vocational Excellence Water Project','Artykuł','https://wearekatapult.eu/scanning-tool-pove-water-project','Katapult / PoVE Water; artykuł z 10.02.2021',1,
 'Opis doświadczeń projektu pokazuje połączenie mapowania interesariuszy, rozpoznania zmian w otoczeniu, pogłębionego poznania potrzeb partnerów i uzgodnienia wartości centrum. Jest przykładem zastosowania narzędzi, a nie osobnym kompletnym formularzem badawczym.',
 'Pobrano artykuł. Podlinkowany adres povewater.eu/scanning-tools/ zwracał błąd 404 w dniu sprawdzenia.',
 'Włączyć diagnozę do jednego procesu warsztatowego, korzystając z istniejących danych regionalnych.'),
]
blocks=[
('edukacja','Kształcenie i pozyskiwanie uczestników','Education & Recruitment','https://wearekatapult.eu/improving-education','Szkoły i firmy współtworzą ofertę odpowiadającą potrzebom pracy; rozwój programów łączy się z przygotowaniem kadry i zainteresowaniem odbiorców.','Aktualizacja zadań zawodowych i pokazanie kandydatom, czego nauczą się podczas praktyk.'),
('lll','Uczenie się przez całe życie','Life Long Learning','https://wearekatapult.eu/building-block-life-long-learning','Oferta dla dorosłych wymaga elastycznych form, dopasowanych terminów oraz współpracy pracodawców w zapewnieniu uczestnictwa. Może rozwijać się na podstawie już zmodernizowanego kształcenia.','Krótkie moduły dla mentorów i pracowników firm, powiązane z ich zadaniami.'),
('innowacje','Innowacje w praktyce zawodowej','Professional Innovation','https://wearekatapult.eu/building-block-professional-innovation','Wspólne zespoły zajmują się problemami firm i tworzą rozwiązania możliwe do wdrożenia. Należy uzgodnić, czy najważniejszy jest efekt biznesowy, czy doświadczenie uczenia się.','Pilotaż poprawy instrukcji stanowiskowej albo wdrażania nowego pracownika.'),
('badania','Badania stosowane','Applied Research','https://wearekatapult.eu/applied-research','Partnerstwo może organizować badania odpowiadające na praktyczne pytania przedsiębiorstw. Wymaga to odpowiednich kompetencji badawczych i uzgodnień dotyczących współpracy.','Projekt z uczelnią dotyczący mierzalnego problemu technologicznego wskazanego przez MŚP.'),
('infrastruktura','Infrastruktura do uczenia się w praktyce','Context-rich Infrastructure','https://wearekatapult.eu/building-blocks/context-rich-infrastructure','Zaplecze odwzorowujące środowisko pracy łączy potrzeby kształcenia, przedsiębiorstw i rozwoju zawodowego. Wspólne korzystanie wymaga ustalenia dostępności i odpowiedzialności za zasoby.','Mapa istniejących pracowni, laboratoriów i BCU oraz uzgodnione zasady rezerwacji.'),
('siec','Organizowanie sieci współpracy','Network Building','https://wearekatapult.eu/network-building','Niewielki zespół może kojarzyć partnerów, utrzymywać relacje i ułatwiać dostęp do wiedzy oraz infrastruktury. Zadania edukacyjne i projektowe wykonują partnerzy dysponujący odpowiednimi zasobami.','Sekretariat COVE Polska prowadzący zgłoszenia potrzeb i dobierający wykonawców usług.')]
stages=[
('Rozpoznaj ekosystem','Ustal potrzeby i partnerów.',['interesariusze','pestle','skan'],'Mapa instytucji, potrzeb i istniejących usług; lista luk do sprawdzenia.'),
('Uzgodnij odbiorców i model','Opisz odbiorców oraz sposób tworzenia wartości.',['bmc','empatia'],'Porównanie dwóch wariantów działania COVE Polska i wybór założeń do testu.'),
('Zaprojektuj ofertę','Przełóż potrzeby na działania i zasoby.',['bmc','projekt'],'Dwie karty pilotażu z liderami, odbiorcami i nakładem pracy.'),
('Zaangażuj uczestników','Dopasuj komunikację do grup odbiorców.',['warsztaty'],'Potwierdzone warunki uczestnictwa szkół i firm; lista barier.'),
('Ustal zasady i uruchom','Uzgodnij współpracę, realizację i finansowanie.',['porozumienie','projekt','dojrzalosc'],'Decyzja o gospodarzu sekretariatu i uruchomieniu działań w zabezpieczonym budżecie.'),
('Zapytaj inne centra','Uzyskaj zewnętrzną informację zwrotną.',['peer','refleksja'],'Notatka z przeglądu, priorytety zmian i odpowiedzialność za ich wykonanie.'),
('Popraw i powtórz','Zaktualizuj model na podstawie doświadczeń.',['bmc'],'Strategia 1.0 oparta na wynikach pilotaży oraz termin kolejnego przeglądu.')]
forms=[
('potrzeba','Dowód potrzeby',['Jaki problem i u kogo zaobserwowaliśmy?','Jakie źródło lub rozmowa to potwierdza?','Kto już pomaga w jego rozwiązaniu?','Co COVE Polska może wnieść dodatkowo?']),
('otoczenie','Otoczenie i decyzja',['Zmiana w otoczeniu oraz jej źródło i data','Skutek dla nauczycieli, uczniów lub firm','Co możemy sprawdzić w ciągu miesiąca?','Decyzja, osoba odpowiedzialna i termin']),
('odbiorca','Odbiorca usługi',['Rola i sytuacja zawodowa odbiorcy','Wypowiedź z rozmowy — bez danych osobowych','Bariera udziału i sposób jej zmniejszenia','Korzyść, którą odbiorca uzna za wartą wysiłku']),
('model','Model usługi COVE Polska',['Odbiorcy i problem do rozwiązania','Rezultat oraz dowód jego osiągnięcia','Partnerzy, zasoby i sposób realizacji','Koszty stałe i koszty edycji','Potwierdzone finansowanie oraz luka']),
('pilot','Pilotaż do uruchomienia',['Zadanie, które wykona uczestnik','Kryterium jakości i osoba oceniająca','Lider i wkłady partnerów','Termin oraz koszt','Warunek kontynuacji lub zakończenia']),
('wspolpraca','Zobowiązania partnerów',['Kto wnosi jaki zasób i na jak długo?','Kto podejmuje decyzję i kto wykonuje działanie?','Jak rozwiązujemy brak zasobu lub opóźnienie?','Kiedy sprawdzimy wykonanie ustaleń?']),
('przeglad','Wniosek z przeglądu',['Co zadziałało — konkretny dowód','Co wymaga zmiany — konkretny przypadek','Zalecenie i odpowiedzialny partner','Termin ponownego sprawdzenia efektu'])]
R.joinpath('katapult-katalog.json').write_text(json.dumps({'date':'2026-09-12','source':road,'type':'Polskie omówienia i autorskie zastosowania, nie pełne tłumaczenia','tools':[dict(zip(['id','title_pl','title_original','format','url','attribution','stage','summary_pl','availability','application_cove'],t)) for t in tools]},ensure_ascii=False,indent=2))
parts=['# Katapult: narzędzia rozwoju CoVE\n',
'Polski przewodnik po materiałach • Sprawdzenie źródeł: 12 września 2026 r.\n',
'**Źródło metody:** roadmapa opracowana w Platform of Vocational Excellence Water i opublikowana przez Katapult. Poniżej znajdują się krótkie polskie omówienia, odnośniki do oryginałów oraz propozycje zastosowania w COVE Polska. **Nie jest to oficjalne tłumaczenie Katapult.**\n',
f'[Otwórz oryginalną roadmapę]({road}) · [Katalog narzędzi JSON](katapult-katalog.json) · [Rejestr sprawdzonych linków](katapult-linki.html)\n',
'**Priorytety COVE Polska:** [Rozwój kształcenia i uczenie się przez całe życie — model usług i pilotaż](edukacja-lll.html).\n',
'## Siedem etapów pracy\n',
'<div class="roadmap">']
for i,(title,summary,ids,result) in enumerate(stages,1):
 links=' '.join(f'<a href="#tool-{k}">{H(next(t[1] for t in tools if t[0]==k))}</a>' for k in ids)
 if i==3:links+=' <a href="#obszary">Sześć obszarów współpracy</a>'
 parts.append(f'<details class="road-step" {"open" if i==1 else ""}><summary><span class="step-no">{i}</span><span>{H(title)}</span></summary><div class="step-body"><p>{H(summary)}</p><div class="tool-links">{links}</div><p class="application"><strong>Propozycja dla COVE Polska:</strong> {H(result)}</p></div></details>')
parts+=['</div>','\nEtapy odnoszą się do roadmapy Katapult / PoVE Water. Proponowane rezultaty dla COVE Polska są autorskim uzupełnieniem.\n','## Katalog narzędzi\n','<div class="tool-controls"><label for="tool-search">Znajdź narzędzie</label><input id="tool-search" type="search" placeholder="Np. partnerzy, PDF, model, przegląd"><p id="tool-count" role="status" aria-live="polite"></p></div>']
for t in tools:
 id,title,original,fmt,url,attr,stage,summary,status,app=t
 parts.append(f'<section class="kat-tool" id="tool-{id}" data-search="{H(" ".join(map(str,t)).lower())}"><div class="tool-meta">Etap {stage} · {H(fmt)}</div><h3>{H(title)}</h3><p class="original-title">{H(original)}</p><p>{H(summary)}</p><p class="availability">{H(status)}</p><p class="application"><strong>Propozycja dla COVE Polska:</strong> {H(app)}</p><p class="credit"><strong>Autor / źródło:</strong> {H(attr)}.</p><a class="source-button" href="{H(url)}">Otwórz oryginał — {H(fmt.split(" · ")[0])}</a></section>')
parts+=['\n## Sześć obszarów współpracy\n',f'Katapult opisuje różne funkcje partnerstwa i zaleca stopniowy rozwój oferty. Poniższe nazwy odpowiadają artykułom z kolekcji [Building blocks](https://wearekatapult.eu/building-blocks/).\n','<div class="blocks-grid" id="obszary">']
for id,title,original,url,summary,app in blocks:
 parts.append(f'<section class="building-block"><h3>{H(title)}</h3><p class="original-title">{H(original)}</p><p>{H(summary)}</p><p><strong>W COVE Polska — propozycja:</strong> {H(app)}</p><a href="{H(url)}">Artykuł Katapult</a></section>')
parts+=['</div>','\n## Karty do pracy nad COVE Polska\n','Poniższe karty są autorskim uzupełnieniem tego opracowania. Nie odtwarzają formularzy Katapult. Możesz je wypełnić podczas warsztatu i wyeksportować notatki. Zapis odbywa się lokalnie w tej przeglądarce; nie jest współdzielony z partnerami.\n','<div class="worksheet-actions"><button id="export-notes" type="button">Pobierz notatki JSON</button><button id="print-notes" type="button">Drukuj wypełnione karty</button><span id="save-status" role="status" aria-live="polite"></span></div><div class="worksheets">']
for id,title,fields in forms:
 if i==3:links+=' <a href="#obszary">Sześć obszarów współpracy</a>'
 parts.append(f'<details class="worksheet"><summary>{H(title)}</summary><div class="worksheet-fields">')
 for n,label in enumerate(fields):
  key=f'{id}-{n}';parts.append(f'<label for="{key}">{H(label)}</label><textarea id="{key}" data-note="{key}" data-label="{H(title+" — "+label)}" rows="3" placeholder="Wpisz ustalenia zespołu…"></textarea>')
 parts.append('</div></details>')
parts+=['</div>','\n## Autorstwo, dostępność i zakres opracowania\n',
'Katapult udostępnia roadmapę i odsyła do materiałów różnych autorów. Autorstwo konkretnego narzędzia wskazano przy jego opisie. Stopka strony Katapult zawiera zastrzeżenie praw; w sprawdzonych plikach nie potwierdzono licencji pozwalającej na publikację pełnego tłumaczenia. Dlatego publikujemy **omówienia po polsku oraz własne karty**, a oryginały otwierają się na stronach wydawców.\n',
'Przejrzano roadmapę, artykuły o narzędziach, ich pliki, materiały powiązane i artykuły o sześciu obszarach współpracy. Zachowano również odnośniki z artykułów oraz plików PDF. Nie rozwijano bez końca całych serwisów zewnętrznych, kategorii i nawigacji „poprzedni/następny”. Nagrania zachowano jako linki; nie pobierano ani nie tłumaczono ich pełnej treści.\n',
'Dostępny kwestionariusz interesariuszy i programy warsztatów wymagają kontaktu z Katapult. Nie wysyłano żadnej wiadomości. Niektóre historyczne linki prowadzą do błędów lub zmienionych stron — szczegóły podano w rejestrze.\n',
'### Dodatkowe artykuły i nagrania\n',
'- [Artykuł o Business Model Canvas](https://wearekatapult.eu/tools/business-model-canvas).\n- [Artykuł o peer review](https://www.wearekatapult.eu/tools/peer-review/).\n- [Budowanie partnerstwa — artykuł i film](https://wearekatapult.eu/how-do-you-build-a-succesful-public-private-partnership).\n- [Doświadczenia warsztatowe PoVE Water](https://wearekatapult.eu/european-professionals-meet-online-to-work-on-tomorrows-vocational-water-sector-professional).\n- [Wideo przy pierwszym etapie](https://www.youtube.com/watch?v=qp0HIF3SfI4).\n- [Wideo przy drugim etapie](https://www.youtube.com/watch?v=QoAOzMTLP5s).\n- [Film o obszarach współpracy](https://vimeo.com/571253406).\n- [Materiał filmowy CIV Water](https://youtu.be/BDEK_thbEaA).\n',
'Pełna lista zachowanych odnośników i status pobrania: [rejestr linków](katapult-linki.html). Powrót do [planu strategii](plan.html).\n']
(R/'materialy/Katapult_PL.md').write_text('\n'.join(parts))
# Plain Markdown companion without layout markup, suitable for download and offline reading.
plain=['# Katapult — polskie omówienia narzędzi','Sprawdzenie: 12.09.2026. Nie jest to pełne ani oficjalne tłumaczenie. Źródło roadmapy: '+road]
for t in tools:
 id,title,original,fmt,url,attr,stage,summary,status,app=t
 plain+=['\n## '+title,original+' — '+fmt,'Źródło: '+attr+'\n'+url,summary,status,'Autorska propozycja dla COVE Polska: '+app]
for id,title,original,url,summary,app in blocks:plain+=['\n## '+title,original+'\n'+url,summary,'Autorska propozycja dla COVE Polska: '+app]
for id,title,fields in forms:plain+=['\n## Karta autorska: '+title]+['- '+f+': ____________________' for f in fields]
(R/'materialy/Katapult_omowienia_i_karty_PL.md').write_text('\n\n'.join(plain))
print(len(tools),'narzędzi',len(blocks),'obszarów',len(forms),'kart')
