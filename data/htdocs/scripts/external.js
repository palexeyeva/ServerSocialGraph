function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

/*Скрыть/показать окно с результатом поиска*/
$(document).ready(function () {
  PopUpHide();
});
function PopUpShow() {
  $("#popup1").show();
}
function PopUpHide() {
  $("#popup1").hide();
}
/* Скрыть/показать социальный граф */
$(document).ready(function () {
  GraphHide();
});

function GraphHide() {
  $("#graph1").hide();
}

function GraphShow() {
  $("#popup1").hide();
  $("#graph1").show();
}

/*Задание диапазона*/
function handleChange(input) {
  if (input.value < 12) input.value = 12;
  if (input.value > 110) input.value = 110;
}

function checkLetter(input) {
  var value = input.value;
  var rep = /[-\.;":'a-zA-Zа-яА-Я]/;
  if (rep.test(value)) {
    value = value.replace(rep, "");
    input.value = value;
  }
}

// function checkFrom(input) {
//   let elem = document.getElementById('ageToS');
//   let elemAS = document.getElementById('ageToAS');
//   if (input.value > elem.value && elem.value!='') {
//     input.value = elem.value;
//     elemAS.value = elem.value;
//   };
// }

function checkTo(input) {
  let elem = document.getElementById('ageFromAS');
  if (input.value < elem.value && elem.value !='') input.value = elem.value;
}

function checkFrom(input) {
  let elem = document.getElementById('ageToAS');
  if (input.value > elem.value && elem.value !='') input.value = elem.value;
}

function onButtonReset() {
    location.reload();
    var inputs = document.querySelectorAll('input[type=text]');

    for (var i = 0;  i < inputs.length; i++) {
        inputs[i].value = '';
    };
}
//получение id страны при клике по стране
function getCountryValue(select) {
  countryId = select.options[select.selectedIndex].value;
  return countryId;
}

//Динамическое создание блоков div
function creatediv(id, name, href, image) {

var newdiv = document.createElement('div'); 
newdiv.setAttribute('id', id);  
        newdiv.style.left = "10px"; 
        newdiv.style.marginLeft = "20px";
        newdiv.style.bottom = bottom = "10"; 
        newdiv.style.marginTop = "10px";


    //newdiv.style.background = "#FFFFF"; 
    //newdiv.style.border = "1px solid #000"; 
    var link = document.createElement('a');
    link.href = href;
    link.title = href;

    var img = new Image(100, 100);
    img.src = image;

    if (name) { newdiv.innerHTML = name; 
    } 
    else { 
        newdiv.innerHTML = "nothing"; 
    } 
  
document.body.appendChild(newdiv);
document.getElementById(id).appendChild(e);
document.getElementById(id).appendChild(img);
}

//Функция передачи данных
function elem(){

deptObj = { one : '1', two : '2'};

$.ajax({
    type: 'POST',
    data: deptObj,
    url: "test.py",
    success: function(result) { console.log("Success!"); console.log(result); },
    error: function(request, error) { console.log("Error"); console.log(request); }
});
}


