
let estimatedData = document.getElementById("estimated");
let actual = document.getElementById("actual");
let finalAppend = document.getElementById('result')

function getOutput() {
  let actualValue = parseInt(actual.value)
  let estimatedValue = parseInt(estimatedData.value)
  let final = (actualValue/ estimatedValue)* 100

  let bonus = null 
  
  if (final > estimatedValue){
    bonus = final - estimatedValue
  }
  let time = new Date();
  let formattedTime = time.toLocaleTimeString();
 
  let date = new Date();
  let options = {day: '2-digit', month: '2-digit', year: '2-digit'};
  let formattedDate = date.toLocaleDateString('en-GB', options);

  let createPara = document.createElement('p')
  createPara.textContent ='Score-:' + String(final) +"   Bonus-:" +bonus + '   Date -:'+ formattedTime+' / '+formattedDate
  createPara.classList.add("temp")
  finalAppend.appendChild(createPara)
}
