// TASK - B
/* Savol:
 Shunday function tuzing, u 1ta string parametrga ega bolsin,
 hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi. 

Yechim:
*/

function countNum(a){
   
  return a.split("").filter( ele =>  !isNaN(ele)).length
     
 }
const result = countNum("ghjhf43hy8k")
console.log("result:", result)











// TASK- A

/* SAVOL:: 
      Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni 
      ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
      MASALAN countLetter("e", "engineer") 3ni return qiladi.

*/

// Yechim::
// split() ni qoymaguncha ishlamadi , splitni internetdan oldim
  
//function task(a,b){
//    return b.split("").filter(ele => ele === a).length;

 // }

//const result = task("e","ele");
//console.log(result);