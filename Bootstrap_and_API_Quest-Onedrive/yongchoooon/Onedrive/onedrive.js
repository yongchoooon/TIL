'use strict';

function drag(e) {
  e.dataTransfer.setData("Text", e.target.id);
}

function checkAllToggle() {
  let checkboxes = document.querySelectorAll(".checkbox");
  for (let i= 1; i < checkboxes.length ; i++) {
    if (checkboxes[0].checked === false) {
      checkboxes[i].checked = true;
      document.getElementById('list-row-' + i).style.backgroundColor = "#f3f2f1";
    } else {
      checkboxes[i].checked = false;
      document.getElementById('list-row-' + i).style.backgroundColor = 'transparent';
    }
  }
}


$(".checkbox-label-1").click(function(){
  if($("#checkbox1").prop("checked")==false){
    console.log('11');
    $("#list-row-1").css('backgroundColor', '#f3f2f1');
  } else {
    console.log('22');
    $("#list-row-1").css('backgroundColor', 'transparent');
  }
  
});


// 체크하면 한 줄만 background color 바꾸려고 하는데 잘 안 됨
// 두 번째 코드가 그나마 가능성 있음


// function setBackgroundGray(i) {
//   let list_row_i = document.querySelectorAll("#list-row-" + i);
//   let checkbox = document.querySelectorAll("#checkbox" + i);
//   console.log(list_row_i);

//   if (checkbox[0].checked === false) {
//     checkbox.checked = true;
//     // list_row_i.style.backgroundColor = "#f3f2f1";
//   } else {
//     checkbox.checked = false;
//     // list_row_i.style.backgroundColor = "transparent";
//   }

// }

// function setBackgroundGray(i) {
//   let list_row_i = document.querySelector("list-row-" + i);
//   let checkbox = document.querySelector("checkbox" + i);
//   checkbox.setAttribute("checked", "false");
//   console.log(checkbox.getAttribute("checked") === "false");

//   if (checkbox.getAttribute("checked") === "false") {
//     console.log(2);
    
//     console.log(3);
//     list_row_i.style.backgroundColor = "#f3f2f1";
//     checkbox.setAttribute("checked", "checked");
//     console.log(4);
//   } else {
//     console.log(1);
//     checkbox.setAttribute('checked', 'false');
//     list_row_i.style.backgroundColor = "transparent";
//   }

// }