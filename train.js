// TASK- A

/* SAVOL:: 
      Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni 
      ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
      MASALAN countLetter("e", "engineer") 3ni return qiladi.

*/

// Yechim::
// split() ni qoymaguncha ishlamadi , splitni internetdan oldim
  
function task(a,b){
    return b.split("").filter(ele => ele === a).length;

}

const result = task("e","ele");
console.log(result);