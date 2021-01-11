const btn = document.querySelector('#btn')

function onClick (e){
    btn.innerHTML++
}

btn.addEventListener('click', onClick)