//это массив данных такой обрабатывается
// var data = [
//   ["Диана", "Ганина", "1999-08-16", "https://vk.com/dinndi", "https://sun1-96.userapi.com/impg/H6M5KcIel0yMiI-Lij0aU24DI1NAGeCeZiwDxQ/_ppXu1i5QcY.jpg?size=810x1080&quality=96&sign=1af2277c9274457b496941b8def1485f&type=album", "Москва"], 
//   ["Диана", "Ганина", "2004-12-12", "https://vk.com/didyn", "https://klike.net/uploads/posts/2019-06/1561009159_3.jpg", "Адлер"], 
//   ["Диана", "Ганина", "1996-02-12", "https://vk.com/937238", "https://klike.net/uploads/posts/2018-11/1543310584_1.jpg", "Питер"]];


var data = new Array();

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
function PopUpShow(data) {
  $("#popup1").show();
    //функция получает данные и вызывает строителя
    for (var i = 0; i < data.length; i++) {
      var j = 0;
      creatediv(i, data[i].split(';')[0], data[i].split(';')[1], data[i].split(';')[2], data[i].split(';')[3], data[i].split(';')[4], data[i].split(';')[5]);
     }
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
  var globalCountryId;
//получение id страны при клике по стране
function getCountryValue(select) {
  countryId = select.options[select.selectedIndex].value;
  globalCountryId = countryId;
  // console.log(globalCountryId);
  return countryId;
}

function getFields(name, surName, sex, bdate, country, city){
  let dt = {
    name: name.value,
    surName: surName.value,
    sex: sex.value,
    bdate: bdate.value,
    country: country.value,
    city: city.value
  };
$.ajax({
    type: 'POST',
    data: dt,
    url: "test.py",
    success: function(result) { console.log("Success!"); outFields();},
    error: function(request, error) { console.log("Error"); console.log(request); }
});

function outFields() {
  $.get("res.txt", function(res){
    data = res.split('\n');
    console.log(data);
    for (var i = 0; i < 6; i++) {
      console.log(data[0].split(';')[i])
    }
    PopUpShow(data);
  });
  // alert(data[0].split(';')[5]);
  
} 
}
//Динамическое создание блоков div
//это массив данных такой обрабатывается
// var data = [
// ["Диана", "Ганина", "1999-08-16", "https://vk.com/dinndi", "https://sun1-96.userapi.com/impg/H6M5KcIel0yMiI-Lij0aU24DI1NAGeCeZiwDxQ/_ppXu1i5QcY.jpg?size=810x1080&quality=96&sign=1af2277c9274457b496941b8def1485f&type=album", "Москва"], 
// ["Диана", "Ганина", "2004-12-12", "https://vk.com/didyn", "https://klike.net/uploads/posts/2019-06/1561009159_3.jpg", "Адлер"], 
// ["Диана", "Ганина", "1996-02-12", "https://vk.com/937238", "https://klike.net/uploads/posts/2018-11/1543310584_1.jpg", "Питер"]];

//функция самого создания
function creatediv(id, name, surname, bdate, href, image, city) {

var newdiv = document.createElement('div'); 
newdiv.setAttribute('id', id);  
        newdiv.style.left = "10px"; 
        newdiv.style.marginLeft = "20px";
        newdiv.style.bottom = bottom = "10"; 
        newdiv.style.marginTop = "30px";

    var img = new Image(100, 130);
    img.src = image;

    
    var nm = document.createElement('a');
    var bdt = document.createElement('p');
    var ct = document.createElement('p');

    if (name || surname) { 
        nm.href = href;
        nm.title = href;
        nm.innerText = name + " " + surname;
    } 
    

    if (bdate) { 
        bdt.innerText = bdate;
    } 
    

    if (city) { 
        ct.innerText = city;
    } 

    img.style.padding = "10px";
    img.style.display = "block";
    nm.style.display = "block";
    nm.style.margin = "10px";
    bdt.style.margin = "10px";
    ct.style.margin = "10px";
    nm.style.fontSize = "16pt";
    bdt.style.fontSize = "14pt";
    ct.style.fontSize = "14pt";
    nm.style.color = "white";
  
document.getElementById("popWindow").appendChild(newdiv);
document.getElementById(id).appendChild(img);
document.getElementById(id).appendChild(nm);
document.getElementById(id).appendChild(bdt);
document.getElementById(id).appendChild(ct);
}

   //функция получает данные и вызывает строителя
  function create(){
   for (var i = 0; i < data.length; i++) {
    creatediv(i, data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]);
   }
   
}


function getFieldsAS(name, surName, sex, bdate, country, city, ageFrom, ageTo, job){
  let data = {
    name: name.value,
    surName: surName.value,
    sex: sex.value,
    bdate: bdate.value,
    country: country.value,
    city: city.value,
    ageFrom: ageFrom.value,
    ageTo: ageTo.value, 
    job: job.value
  };
  console.log(data)
$.ajax({
    type: 'POST',
    data: data,
    url: "test.py",
    success: function(result) { console.log("Success!"); console.log(result);},
    error: function(request, error) { console.log("Error"); console.log(request); }
});
}

