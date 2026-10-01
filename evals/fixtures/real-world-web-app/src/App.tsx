export function App(){
  let saved=false;
  async function save(){saved=true; toast("Saved"); await fetch("/api/customer",{method:"POST"});}
  function remove(){ if(confirm("Are you sure?")) fetch("/api/customer/42",{method:"DELETE"}); }
  return <div className="shell"><aside>Customers Settings</aside><main><input defaultValue="Acme"/><button onClick={save}>Save</button><button onClick={remove}>Delete</button></main></div>
}
function toast(x:string){console.log(x)}