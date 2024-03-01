

function scaleTitle(number) {

    const title = document.getElementById('card-title-'+number);
    const textLength = title.textContent.length;

    const maxLength = 26
    const factor = Math.min(1, (maxLength / textLength))

    const fontSize = factor * 9.5

    const padding = (1 - (factor)) * 2.5

    title.style.fontSize = fontSize + "pt"
    title.style.paddingTop = padding + "mm"

}


const attributes = '<div class="card-attribute">${{ATTRIBUTE_NAME}}:<div class="card-attribute-value">${{ATTRIBUTE_VALUE}}</div></div>'


function generateCards() {

    var i = 0

    while (document.getElementById('card-title-'+i) !== null) {
        scaleTitle(i)
        i = i+1
    }

    





    
}



