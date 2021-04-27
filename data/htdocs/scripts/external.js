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
    for (var i = 0; i < data.length - 1; i++) {
      var j = 0;
      creatediv(i, data[i].split(';')[0], data[i].split(';')[1], data[i].split(';')[2], data[i].split(';')[3], data[i].split(';')[4], data[i].split(';')[5], data[i].split(';')[6]);
     }
    var norb = '<norb>' + (data.length-1) + '</norb>';
    $('.js_len').empty().html(norb);
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
   $.ajax({
      type: 'POST',
      url: "data_file.json",
      success: function(result) { console.log("Success!"); graphBuild(result);},
      });  
}

// function graphViz(){
//       $.ajax({
//       type: 'POST',
//       url: "data_file.json",
//       success: function(result) { console.log("Success!"); graphBuild(result);},
//       });  
  
// }

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
    PopUpShow(data);
  });
  
} 
}

//функция создания динамических div
function creatediv(id, name, surname, bdate, href, image, city, idpers) {

var newdiv = document.createElement('div'); 
newdiv.setAttribute('id', id);  
        // newdiv.style.left = "10px"; 
        // newdiv.style.marginLeft = "20px";
        // newdiv.style.bottom = bottom = "10"; 
        // newdiv.style.marginTop = "30px";
        newdiv.setAttribute('class', 'b-pop__newdiv');

    var img = new Image(338, 450);
    img.src = image;
    img.setAttribute('class', 'b-pop__img'); 

    var nm = document.createElement('a');
    var bdt = document.createElement('p');
    var ct = document.createElement('p'); 
    var checkb = document.createElement("input");
    checkb.name = "chooseRadio";
    checkb.type="radio";
    checkb.value = idpers; 
    nm.target="_blank";
    checkb.id = id;
    checkb.setAttribute('class', 'b-pop__input'); 
    newdiv.value = idpers;

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

    // img.style.padding = "10px";
    // img.style.display = "block";
    nm.style.display = "block";
    nm.style.margin = "10px";
    // bdt.style.margin = "10px";
    // ct.style.margin = "10px";
    nm.style.fontSize = "14pt";
    bdt.style.fontSize = "14pt";
    ct.style.fontSize = "14pt";
    ct.style.margin = "10px"; 
    bdt.style.margin = "10px"; 
    nm.style.color = "white";
  
document.getElementById("popWindow").appendChild(newdiv);
document.getElementById(id).appendChild(checkb);
document.getElementById(id).appendChild(img);
document.getElementById(id).appendChild(nm);
document.getElementById(id).appendChild(bdt);
document.getElementById(id).appendChild(ct);
}

//возвращает выбранный под чекбоксом контейнер 
function chooseCheck(){
  var chooseDate;
  var checkboxes = document.getElementsByTagName('input');
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].type == 'radio') {
    if (checkboxes[i].checked) {
      chooseDate = document.getElementById(checkboxes[i].id);
      console.log(chooseDate.value);
      chooseID = chooseDate.value;
    }
  }  
  }
  $.ajax ({
    type: 'POST',
    url: "choosePreson.py",
    data: {
      chooseID: chooseID
    }, 
    success: function(result) {console.log("Success!!!!"); console.log(result);}
  });
  return chooseID;
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

function graphBuild(result){
  datas = result;
  console.log(datas);
  var graph = Viva.Graph.graph();


            // var data = {"people":[
            //     {"id": 1, "name":"Диана","group":1}, {"id": 2, "name":"Диляра","group":1}, {"id": 3, "name":"Полина","group":1}, {"id": 4, "name":"Глеб","group":2}, {"id": 5, "name":"Рома","group":2}, {"id": 6, "name":"Оля","group":1}
            //     ],
            //     "connections": [
            //     [1, 2, 3, 4, 5, 6],
            //     [2, 1, 3, 4],
            //     [3, 1, 2, 6],
            //     [4, 1, 2],
            //     [5, 1],
            //     [6, 1, 3]
            //     ]
            // }
            console.log(datas.people.length);
            for (var i = 0; i < datas.people.length; i++) {
                    // console.log(datas.people[i].id);
                    graph.addNode(datas.people[i].id, datas.people[i]);
                    
            }
            console.log(datas.connection.length);
            for (var i = 0; i < datas.connection.length; i++) {
                for (var j = 1; j < datas.connection[i].length; j++) {
                    graph.addLink(datas.connection[i][0], datas.connection[i][j]);
                }
                
            }

               var layout = Viva.Graph.Layout.forceDirected(graph, {
                        springLength : 35,
                        springCoeff : 0.00055,
                        dragCoeff : 0.09,
                        gravity : -1
                    });

                var graphics = Viva.Graph.View.svgGraphics(),
                nodeSize = 24,
                // we use this method to highlight all realted links
                // when user hovers mouse over a node:
                highlightRelatedNodes = function(nodeId, isOn) {
                   // just enumerate all realted nodes and update link color:
                   graph.forEachLinkedNode(nodeId, function(node, link){
                       var linkUI = graphics.getLinkUI(link.id);
                       if (linkUI) {
                           // linkUI is a UI object created by graphics below
                           linkUI.attr('stroke', isOn ? 'red' : 'gray');

                       }
                   });
                };

              // Since we are using SVG we can easily subscribe to any supported
            // events (http://www.w3.org/TR/SVG/interact.html#SVGEvents ),
            // including mouse events:
            graphics.node(function(node) {
                var ui = Viva.Graph.svg('g'),
                  // Create SVG text element with user id as content
                  svgText = Viva.Graph.svg('text').attr('y', '-4px').text(node.data.name).attr("style", "visibility: hidden"),
                  img = Viva.Graph.svg('image')
                     .attr('width', nodeSize)
                     .attr('height', nodeSize)
                     if (node.data.group == 1) {
                        img.link('https://memax.club/wp-content/uploads/2019/06/Kartinki_krasnyy_kvadrat_1_09105141.png');
                    } else{
                        img.link('https://www.freeiconspng.com/uploads/blue-square-image-3.png');
                    }

                $(ui).hover(function() { // mouse over
                    highlightRelatedNodes(node.id, true);
                    svgText.attr("style", "visibility");


                    // svgText = Viva.Graph.svg('text').attr('y', '-4px').text(node.id)
                }, function() { // mouse out
                    highlightRelatedNodes(node.id, false);
                    svgText.attr("style", "visibility: hidden");
                });
                ui.append(svgText);
              ui.append(img);
                return ui;
            })
            .placeNode(function(nodeUI, pos) {
                // 'g' element doesn't have convenient (x,y) attributes, instead
                // we have to deal with transforms: http://www.w3.org/TR/SVG/coords.html#SVGGlobalTransformAttribute
                nodeUI.attr('transform',
                            'translate(' +
                                  (pos.x - nodeSize/2) + ',' + (pos.y - nodeSize/2) +
                            ')');
            });

            graphics.link(function(link){
                return Viva.Graph.svg('path')
                              .attr('stroke', 'gray');
            }).placeLink(function(linkUI, fromPos, toPos) {
                var datas = 'M' + fromPos.x + ',' + fromPos.y +
                           'L' + toPos.x + ',' + toPos.y;

                linkUI.attr("d", datas);
            })

            // Finally render the graph with our customized graphics object:
            var renderer = Viva.Graph.View.renderer(graph, {
                    graphics : graphics
                });
            renderer.run();
            console.log(graph);

              // var iframe = '<svg>' + graph + '</svg>';
              // $('.social-graph__img').empty().html(iframe); 
}

