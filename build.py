from pathlib import Path
import markdown,re,html,shutil
root=Path(__file__).resolve().parent
src=root/'materialy'
pages=[('edukacja-lll','Edukacja i LLL',src/'Edukacja_i_LLL.md'),('katapult','Katapult — narzędzia',src/'Katapult_PL.md'),('katapult-linki','Katapult — rejestr linków',src/'Katapult_linki.md'),('plan','Plan strategii',src/'Plan_opracowania_strategii_COVE_Polska.md'),('warsztat','Warsztat i pilotaże',src/'Karty_warsztatowe.md'),('zrodla','Źródła',src/'Rejestr_zrodel.md'),('analiza','IBE · WEF · PwC',src/'Analiza_VET_IBE_WEF_PwC_Polska.md'),('kompetencje','Wiarygodność i AI',src/'Cele_operacyjne_wiarygodnosc_zrodel_AI_VET.md')]
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
 nav=''.join(f'<a href="{s}.html"'+(' aria-current="page"' if s==slug else '')+f'>{t}</a>' for s,t,_ in pages if s!='katapult-linki')
 date='12 września 2026' if (slug.startswith('katapult') or slug=='edukacja-lll') else '10 września 2026'
 download='Katapult_omowienia_i_karty_PL.md' if slug=='katapult' else p.name
 document=f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Plan rozwoju COVE Polska we Wrocławiu: współpraca edukacji, nauki i firm, pilotaże VET oraz wiarygodne korzystanie z AI."><title>{html.escape(title)} — COVE Polska</title><link rel="stylesheet" href="style.css"></head><body class="{slug}"><a class="skip" href="#tresc">Przejdź do treści</a><header><a class="brand" href="index.html">COVE Polska<span>Strategia rozwoju</span></a><a class="toplink" href="zrodla.html">Materiały i źródła</a></header><div class="layout"><aside><nav aria-label="Dokumenty">{nav}</nav><details open><summary>Na tej stronie</summary>{md.toc}</details><p class="aside-note">Wrocław · Dolny Śląsk<br>Horyzont 2027–2030</p></aside><main id="tresc"><div class="notice"><strong>Materiał do konsultacji</strong> · Opracowanie z {date}. Propozycje wymagają uzgodnienia z partnerami.</div><div class="actions"><a download href="materialy/{download}">Pobierz tekst (.md)</a><button type="button" onclick="window.print()">Drukuj / zapisz PDF</button></div><article>{body}</article><footer>Opracowanie robocze COVE Polska. Datę sprawdzenia materiałów podano w treści działu. <a href="zrodla.html">Sprawdź źródła</a>.</footer></main></div><script>if(matchMedia("(max-width:900px)").matches)document.querySelector("aside details").open=false;</script><script src="katapult.js" defer></script></body></html>'''
 (root/(slug+'.html')).write_text(document)
shutil.copyfile(root/'plan.html',root/'index.html')
(root/'.nojekyll').touch()
print(f'Zbudowano {len(pages)+1} stron HTML.')
