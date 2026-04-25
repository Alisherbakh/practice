// E-TASK (NodeJS)
//
// Shunday function tuzing, u bitta string argumentni
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"
//  Yechim:

function getReverse(a){
      return a.split("").reverse().join("")
}

result = getReverse("apple")
console.log(result)



// D-TASK (NodeJS)

// Shunday function tuzingki unga integerlardan iborat array pass bolsin
//  va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
// Yechim:

// function bigNumber(numb) {
//  
//   a = Math.max.apply(null, numb)
//   return numb.indexOf(a)
//  }
// const result = bigNumber([5,10, 21, 12, 21, 8])
// console.log("result:", result)





// C-TASK (NodeJS)
// Savol::
//Shunday function tuzing, u 2ta string parametr ega bolsin,
// hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
//MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;



//function checkContent(a, b) {
//      a =a.toLowerCase().split("").sort().join("")
//      b = b.toLowerCase().split("").sort().join("")
//  return a === b
// }
// result = checkContent("mitgroup", "tgmipour")
// console.log("result:", result)

















// TASK - B
/* Savol:
 Shunday function tuzing, u 1ta string parametrga ega bolsin,
 hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi. 

Yechim:
*/

// function countNum(a){
   
//  return a.split("").filter( ele =>  !isNaN(ele)).length
     
//  }
// const result = countNum("ghjhf43hy8k")
// console.log("result:", result)











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