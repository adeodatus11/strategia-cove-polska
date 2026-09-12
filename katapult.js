(() => {
  const search = document.querySelector('#tool-search');
  if (!search) return;
  const tools = [...document.querySelectorAll('.kat-tool')];
  const normalize = value => value.toLocaleLowerCase('pl').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ł/g, 'l');
  function filter() {
    const words = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    tools.forEach(el => { el.hidden = !words.every(w => normalize(el.dataset.search).includes(w)); });
    document.querySelector('#tool-count').textContent = `Widoczne narzędzia: ${tools.filter(el => !el.hidden).length} z ${tools.length}`;
  }
  search.addEventListener('input', filter); filter();
  document.querySelectorAll('.tool-links a').forEach(link => link.addEventListener('click', () => {search.value='';filter();}));
  const fields = [...document.querySelectorAll('[data-note]')];
  const status = document.querySelector('#save-status');
  const key = 'cove-katapult-notatki-v1';
  try { const saved = JSON.parse(localStorage.getItem(key) || '{}'); fields.forEach(f => { if (typeof saved[f.dataset.note] === 'string') f.value = saved[f.dataset.note]; }); }
  catch { status.textContent = 'Zapis lokalny niedostępny. Pobierz notatki przed zamknięciem strony.'; }
  fields.forEach(field => field.addEventListener('input', () => {
    try {localStorage.setItem(key, JSON.stringify(Object.fromEntries(fields.map(f=>[f.dataset.note,f.value]))));status.textContent='Notatki zapisane w tej przeglądarce.';}
    catch {status.textContent='Nie udało się zapisać lokalnie. Pobierz notatki JSON.';}
  }));
  document.querySelector('#export-notes').addEventListener('click', () => {
    const data = {projekt:'COVE Polska',typ:'Autorskie karty robocze, nie formularze Katapult',data:new Date().toISOString(),notatki:fields.map(f=>({pole:f.dataset.label,tresc:f.value}))};
    const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json;charset=utf-8'}));
    const a=document.createElement('a');a.href=url;a.download='COVE-Polska-notatki-warsztat.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  let openState=[];
  window.addEventListener('beforeprint',()=>{
    openState=[...document.querySelectorAll('article details')].map(el=>[el,el.open]);openState.forEach(([el])=>{el.open=true;});
    fields.forEach(f=>{const out=document.createElement('div');out.className='print-note';out.textContent=f.value||'—';f.insertAdjacentElement('afterend',out);});
  });
  window.addEventListener('afterprint',()=>{openState.forEach(([el,open])=>{el.open=open;});document.querySelectorAll('.print-note').forEach(el=>el.remove());});
  document.querySelector('#print-notes').addEventListener('click',()=>{document.body.classList.add('print-worksheets');window.print();document.body.classList.remove('print-worksheets');});
})();
