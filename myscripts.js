function myFunction(element,value) {
  document.getElementById("myDropdown").classList.toggle("show");



}

function myFunction2(element) {
  var str="WM"

  if (str == "") {
      document.getElementById("sax").innerHTML = "select plzz";
      return;
  } else {
      if (window.XMLHttpRequest) {
          // code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp = new XMLHttpRequest();
      } else {
          // code for IE6, IE5
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
      xmlhttp.onreadystatechange = myFunction2(element) {

          if (this.readyState == 4 && this.status == 200) {

              document.getElementById("txtHint").innerHTML = this.responseText;
          }
      };

      xmlhttp.open("GET","localhost/getUser.php",true);
      xmlhttp.send();
  }
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

$(function() {
  $('input[name="daterange"]').daterangepicker({
    opens: 'left'
  }, function(start, end, label) {
    console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
  });
});
