let selected=null;
setInterval(()=>{
  // intentionally disruptive: replaces/reorders the table and loses current selection
  const rows=[...document.querySelectorAll("tbody tr")].sort(()=>Math.random()-.5);
  document.querySelector("tbody").replaceChildren(...rows);
  selected=null;
},3000);