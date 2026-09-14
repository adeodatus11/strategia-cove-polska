from pathlib import Path
import markdown,re,html,shutil
root=Path(__file__).resolve().parent
src=root/'materialy'
pages=[('plan','Propozycja dla miasta',src/'Plan_opracowania_strategii_COVE_Polska.md'),('operacyjny','Plan operacyjny 2026/27',src/'Plan_operacyjny_2026_2027.md'),('edukacja-lll','Edukacja i LLL — pilotaże',src/'Edukacja_i_LLL.md'),('katapult','Katapult — narzędzia',src/'Katapult_PL.md'),('katapult-linki','Katapult — rejestr linków',src/'Katapult_linki.md'),('warsztat','Karty warsztatowe',src/'Karty_warsztatowe.md'),('zrodla','Źródła i instytucje',src/'Rejestr_zrodel.md'),('analiza','IBE · WEF · PwC',src/'Analiza_VET_IBE_WEF_PwC_Polska.md'),('kompetencje','Wiarygodność i AI',src/'Cele_operacyjne_wiarygodnosc_zrodel_AI_VET.md')]

mapping={p.name:slug+'.html' for slug,title,p in pages}
for slug,title,p in pages:
 text=p.read_text()
 def link(m):
  url=m.group(2)
  if not url.startswith(('http:','https:','#')) and Path(url).name in mapping:
   url=mapping[Path(url).name]
  elif not url.startswith(('http:', 'https:', '#')) and Path(url).name in mapping.values():
   url=Path(url).name
  return '['+m.group(1)+']('+url+')'
 text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
 if slug=='zrodla':
  text=text.replace('Pliki pobrane znajdują się w katalogu `zrodla`. Kopia lokalna dokumentuje wersję wykorzystaną w analizie; aktualność polityk należy ponownie sprawdzić przed przyjęciem strategii.','Nazwy plików w tabelach odnoszą się do archiwum roboczego autora. Na stronie udostępniamy odnośniki do oryginalnych publikacji. Aktualność polityk należy ponownie sprawdzić przed przyjęciem strategii.')
 md=markdown.Markdown(extensions=['tables','toc','fenced_code'],extension_configs={'toc':{'permalink':False}})
 body=md.convert(text)
 body=body.replace('<table>','<div class="table-scroll" tabindex="0" role="region" aria-label="Tabela — przewiń poziomo na małym ekranie"><table>').replace('</table>','</table></div>')
 # Download original editable content, with document links pointing to published pages.
 (root/'materialy'/p.name).write_text(re.sub(r'\]\(([^/)]+\.html)\)', r'](../\1)', text))
 def navlink(s,t):
  return f'<a href="{s}.html"'+(' aria-current="page"' if s==slug else '')+f'>{t}</a>'
 primary={'plan','operacyjny','edukacja-lll'}
 nav=''.join(navlink(s,t) for s,t,_ in pages if s in primary)
 secondary=''.join(navlink(s,t) for s,t,_ in pages if s not in primary and s!='katapult-linki')
 nav+=f'<details class="resource-nav" {"open" if slug not in primary else ""}><summary>Materiały pomocnicze</summary>{secondary}</details>'
 date='14 września 2026'
 download='Katapult_omowienia_i_karty_PL.md' if slug=='katapult' else p.name
 document=f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Plan rozwoju COVE Polska we Wrocławiu: współpraca edukacji, nauki i firm, pilotaże VET oraz wiarygodne korzystanie z AI."><title>{html.escape(title)} — COVE Polska</title><meta name="theme-color" content="#12364b"><link rel="stylesheet" href="style.css"></head><body class="{slug}"><a class="skip" href="#tresc">Przejdź do treści</a><header class="project-header"><a class="brand" href="index.html" aria-label="COVE Polska — strona główna"><img src="assets/branding/cove-polska.png" alt="COVE Polska" width="210" height="84"></a><div class="header-title"><span>EDUKACJA · WSPÓŁPRACA · ROZWÓJ</span><strong>Strategia COVE Polska</strong></div><div class="project-marks"><a href="https://win4smes.eu/" aria-label="Projekt WIN4SMEs"><img class="win-logo" src="assets/branding/win4smes-2025.png" alt="WIN4SMEs — Workplace Innovation" width="82" height="82"></a><img class="eu-logo" src="assets/branding/eu-cofunded.png" alt="Projekt WIN4SMEs współfinansowany przez Unię Europejską" width="260" height="58"></div></header><div class="project-ribbon"><div><span>Wrocław <span aria-hidden="true">/</span> Centrum Doskonałości Kształcenia Zawodowego</span><span>Perspektywa 2026–2027</span></div></div><div class="layout"><aside><p class="nav-label">STRATEGIA I PLAN DZIAŁANIA</p><nav aria-label="Dokumenty">{nav}</nav><details open><summary>Na tej stronie</summary>{md.toc}</details><p class="aside-note">Wrocław<br>Pierwszy rok: X 2026 – IX 2027</p></aside><main id="tresc"><div class="notice"><strong>Propozycja do rozmowy</strong> · Aktualizacja serwisu: {date}. Daty źródeł wskazano w treści.</div><div class="actions"><a download href="materialy/{download}">Pobierz tekst (.md)</a><button type="button" onclick="window.print()">Drukuj / zapisz PDF</button></div><article>{body}</article><footer class="project-footer"><div class="footer-heading"><strong>COVE Polska</strong><span>Edukacja zawodowa bliżej potrzeb Wrocławia.</span></div><div class="funding-panel"><a href="https://win4smes.eu/"><img src="assets/branding/win4smes-2025.png" alt="WIN4SMEs" width="78" height="78"></a><img src="assets/branding/eu-cofunded.png" alt="Co-funded by the European Union" width="280" height="62"></div><p>Projekt <a href="https://win4smes.eu/">WIN4SMEs</a> jest współfinansowany przez Unię Europejską. Oznaczenie finansowania odnosi się do projektu WIN4SMEs. Przedstawiony plan rozwoju COVE Polska na lata 2026–2027 jest propozycją do rozmowy, wymagającą uzgodnień z partnerami i Gminą Wrocław.</p><div class="footer-links"><a href="https://covepolska.pl/">COVE Polska ↗</a><a href="https://win4smes.eu/">WIN4SMEs ↗</a><a href="zrodla.html">Źródła i przypisania</a></div></footer></main></div><script>if(matchMedia("(max-width:900px)").matches)document.querySelector("aside > details").open=false;</script><script src="katapult.js" defer></script></body></html>'''
 (root/(slug+'.html')).write_text(document)
shutil.copyfile(root/'plan.html',root/'index.html')
(root/'.nojekyll').touch()
print(f'Zbudowano {len(pages)+1} stron HTML.')
