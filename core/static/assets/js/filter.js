function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
       
}


const forms = document.querySelector('form[name=filter]');
console.log(forms)

forms.addEventListener('reset', function(e){
    e.preventDefault()
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);


})

forms.addEventListener('submit', function(e){
    e.preventDefault()
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);


})


function render(data) {
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('#filtered-product-fetch')
    div.innerHTML = output

  
}

let html =  '\
    {{#data}}\
        <div class="item" >\
        <div class="dot-image">\
        <a href="" class="product-permalink"></a>\
        <div class="thumbnai">\
            <img src="/media/{{ image }}" alt="">\
        </div>\
        <div class="thumbnail hover">\
            <img src="/media/{{ image2 }}" alt="">\
        </div>\
        <div class="actions">\
            <ul>\
            <li><a href=""><i class="ri-star-line"></i></a></li>\
            <li><a href=""><i class="ri-arrow-left-right-line"></i></a></li>\
            <li><a href="{{ pid }}"><i class="ri-eye-line"></i></a></li>\
            </ul>\
        </div>\
        <div class="label"><span>-25%</span></div>\
        </div>\
        <div class="dot-info">\
        <h2 class="dot-title"><a href="{{ pid }}">{{ title }}</a></h2>\
        <div class="product-price">\
            <span class="before">₽ {{ old_price }}</span>\
            <span class="current">₽ {{ price }}</span>\
        </div>\
        </div>\
        </div>\
    {{/data}}\
    '

