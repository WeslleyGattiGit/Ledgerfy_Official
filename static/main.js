const btn_check = document.getElementById("btn-check");
var checado = false;

btn_check.addEventListener("click", () => {
  btn_check.classList.toggle("on");
  checado = !checado;
});