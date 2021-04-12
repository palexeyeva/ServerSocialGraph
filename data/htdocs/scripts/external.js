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
function resultSelect() {
  var elem = document.createElement
}

//Функция не работает
function elem(){
  // alert(javascript_out);
  // alert(my_js_data["field1"]);
  // alert(my_js_data["field2"]);
  $.post('test.py', 
  {param1: "param1", 
  param2: 2
  },
  function(data) {
  alert('Загрузка завершена.');
});
}


function ret(input) {
//   $.ajax({
//     type: 'POST',
//     url: "C:/Server/data/htdocs/test.py",
//     data: {
//         "name": input
//     },
//     dataType: "html"
// }).done(function (e) {
//   e.stopPropagation();
    // $('#modal-1').modal('hide');
    // table.row.data([val_no, val_name, val_address, val_phone, val_car, val_penalty, UserIndex_CreateEditButton(val_no, val_name, val_address, val_phone, val_car, val_penalty), UserIndex_CreateDeleteButton(val_no)], $('#' + tempUpdate));
// });
}