var n = "";
function nAdd(x) {
  navigator.vibrate(50);
  if (
    x == "(" ||
    x == ")" ||
    x == "0" ||
    x == "1" ||
    x == "2" ||
    x == "3" ||
    x == "4" ||
    x == "5" ||
    x == "6" ||
    x == "7" ||
    x == "8" ||
    x == "9"
  ) {
    if (document.querySelector(".display2").innerHTML == "0" && x == ")") {
    } else if (document.querySelector(".display2").innerHTML == "0") {
      document.querySelector(".display2").innerHTML = x;
      n = x;
    } else if (
      !(x == "0" && document.querySelector(".display2").innerHTML == "0")
    ) {
      document.querySelector(".display2").innerHTML += x;
      n += x;
    }
  } else if (
    document
      .querySelector(".display2")
      .innerHTML.charAt(
        document.querySelector(".display2").innerHTML.length - 1
      ) != x &&
    n.length > 0
  ) {
    if (
      n.charAt(n.length - 1) == "(" ||
      n.charAt(n.length - 1) == ")" ||
      n.charAt(n.length - 1) == "0" ||
      n.charAt(n.length - 1) == "1" ||
      n.charAt(n.length - 1) == "2" ||
      n.charAt(n.length - 1) == "3" ||
      n.charAt(n.length - 1) == "4" ||
      n.charAt(n.length - 1) == "5" ||
      n.charAt(n.length - 1) == "6" ||
      n.charAt(n.length - 1) == "7" ||
      n.charAt(n.length - 1) == "8" ||
      n.charAt(n.length - 1) == "9"
    ) {
      n += x;
    } else n = n.substring(0, n.length - 1) + x;
    document.querySelector(".display2").innerHTML = n
      .replace("*", "×")
      .replace("/", "÷");
    n = n.replace("×", "*").replace("÷", "/");
  }
  document.querySelector(".display2").scrollBy(1000, 0);
}
function equal() {
  if (document.querySelector(".display2").innerHTML.trim() != "") {
    navigator.vibrate([50, 50, 50]);
    var x = n.replace("×", "*");
    document.querySelector(".display1").innerHTML +=
      "<div class='calculation'>" +
      document.querySelector(".display2").innerHTML +
      " = " +
      (eval(x) == "Infinity" ? "∞" : eval(x)) +
      "</div><br>";
    document.querySelectorAll(".calculation").forEach((e) => {
      e.addEventListener("click", () => {
        document.querySelector(".display2").innerHTML = e.innerHTML.substring(
          0,
          e.innerHTML.indexOf("=")
        );
        n = e.innerHTML;
        console.log(e.innerHTML.substring(0, e.innerHTML.indexOf("=")));
      });
    });
    document.querySelector(".display1").scrollBy(0, 1000);
    document.querySelector(".display2").innerHTML =
      eval(x) == "Infinity" ? "∞" : eval(x);
    n = document.querySelector(".display2").innerHTML;
  }
}
document.querySelectorAll("td").forEach((e) => {
  e.addEventListener("click", () => {
    console.log(e.innerHTML);
    if (e.innerHTML != "=" && e.innerHTML != "AC" && e.innerHTML != "&lt;")
      nAdd(e.innerHTML);
    else if (e.innerHTML == "=") equal();
    else if (e.innerHTML == "AC") {
      document.querySelector(".display2").innerHTML = "0";
      n = "0";
    } else if (e.innerHTML == "&lt;") {
      document.querySelector(".display2").innerHTML = document
        .querySelector(".display2")
        .innerHTML.toString()
        .substring(
          0,
          document.querySelector(".display2").innerHTML.toString().length - 1
        );
      if (document.querySelector(".display2").innerHTML == "")
        document.querySelector(".display2").innerHTML = "0";
      n = document.querySelector(".display2").innerHTML;
    }
  });
});
