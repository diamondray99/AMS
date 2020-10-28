const button = document.querySelector(".container")
const bar1 = document.querySelector(".bar1")
const bar2 = document.querySelector(".bar2")
const create = document.querySelector(".create")
const edit = document.querySelector(".edit")
const remove = document.querySelector(".remove")
const logos = document.querySelectorAll(".func")
const allElements = [button, bar1, bar2, create, edit, remove, logos[0], logos[1], logos[ 2]]
button.addEventListener("click", expand)

function expand() {
    allElements.forEach(element => element.classList.toggle("exp"))
}
