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
		top: findPos(document.getElementById("toggleEl")) - 10,
		left: 0,
		behavior: "smooth",
	});
}

function toggleFunc(myID) {
  var x = document.getElementById("toggleEl");
  var formSec = document.getElementById("formSection")
  if (myID === "change") {
    x.innerHTML = "You are interested in changing your current supplier.";
  } else {
    x.innerHTML = "You are looking to partner with a new supplier.";
  }
  formSec.style.display = "block";
  doScroll();
}
