formSec.style.display = "none";

function findPos(obj) {
	var curtop = 0;
	if (obj.offsetParent) {
		do {
			curtop += obj.offsetTop;
		} while ((obj = obj.offsetParent));
		return [curtop];
	}
}



function doScroll() {
	console.log("test");
	window.scrollTo({
		top: findPos(document.getElementById("toggleEl")) - 20,
		left: 0,
		behavior: "smooth",
	});
}

function toggleFunc(myID) {
  var x = document.getElementById("toggleEl");
  var nature = document.getElementById("nature");
  var formSec = document.getElementById("formSection")
  if (myID == "change") {
    x.innerHTML = "Looking to find an alternate to your existing partner.";
  } else {
    x.innerHTML = "Looking to expand or develop a new partner network.";
    nature.value = "NE";
  }
  formSec.style.display = "block";
  aboutSec.style.display = "block";
  doScroll();
}

function toggleFunc2() {
  var aboutSec = document.getElementById("aboutSec")
  var formSec = document.getElementById("formSection")
  var x = document.getElementById("toggleEl");
  var title = document.getElementById("titlenav");

  if (aboutSec.style.display == "block") {
        aboutSec.style.display = "none";
        window.scrollTo({
		top: findPos(title),
		left: 0,
		behavior: "smooth",
	});
  } else {
        aboutSec.style.display = "block";
        window.scrollTo({
		top: findPos(aboutSec) - 10,
		left: 0,
		behavior: "smooth",
	});
  }
}
