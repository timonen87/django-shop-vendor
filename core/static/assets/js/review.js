

$('#commnetForm').submit(function(element){
    element.preventDefault();

    const monthNamees = ["Январь", "Февраль", "Март", "Апрель", "Май",
    "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];


    let dt = new Date();
    let time = dt.getDate() + " " + monthNamees[dt.getUTCMonth()] + ", " + dt.getFullYear()
    

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),

        dataType: 'json',

        success: function(response) {
           
            $('#commnetForm').each(function(){
                this.reset();
                console.log('reviews submit');
                $('#data-review').removeClass('active');
                $('.overlay').removeClass('active');
            });
            


            if(response.bool == true) {

                $('#comment-message').html('Комментарий добавлен!')
                
                $('#commnetForm').hide()
                $('#no_comment').hide()

                let rating = (el) => {
                    let _star = ''
                    for(let i = 1; i <= el; i++) {
                        _star += '<i class="ri-star-fill"></i>'
                    }
                    return _star
                }

                let html = `
               
                <div class="comment-block">
                <div class="profile">
                <div class="thumb-name">
                    <div class="profile-img">
                    <img src="/static/assets/img/ig_01.jpg" alt="">
                    </div>

                </div>
                <div class="grouping">
                    <div class="name">${response.context.user}</div>
                    <div class="rating">
                    ${rating(response.context.rating)}
                    </div>
                    <div class="date grey-color">${time} </div>
                </div>
                </div>
                <div class="comment">
                <strong>Комментарий:</strong>
                    <p class="grey-color">${response.context.review}</p>
                </div>
                </div>
                
                        `
                
                $('.body-review').prepend(html)

   
                    }
                }
            })

        })



// $(document).ready(function () {
//     $('.filter-checkbox').on('click', function (){
//         console.log('chekbox checked')

//         let filter_object = {

//         }

//         $('.filter-checkbox').each(function(){
//             let filter_value= $(this).val()
//             let filter_key = $(this).data('filter')

//             // console.log('filter value is:', filter_value)
//             // console.log('filter key  is:', filter_key)

//             filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(el){
//                 return el.value
//             })
//         })
//         console.log('Filter obj is:', filter_object)
//         $.ajax({
//             url: "/filter-products",
//             data: filter_object,
//             dataType: "json",
//             beforeSend: function() {
//                 console.log('sending data')
//             },
//             success: function(response){
//                 console.log(response)

//                 $('#filtered-product').html(response.data)
//             }
//         })

//     })
// })

