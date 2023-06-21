$('#add-to-cart-btn').on('click', function(){
    let quantity = $('#product-quantity').val()
    let product_title = $('#product-title').val()
    let product_id = $('#product_id').val()
    let product_price = $('#current-product-price').text()
    let this_val = $(this)

    console.log('id', product_id )
    console.log('title', product_title )
    console.log('Quantity', quantity )
    console.log('price', product_price )
    console.log('Current element', this_val )


    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_id,
            'qty': quantity,
            'title': product_title,
            'price': product_price
        },
        dataType: 'json',
        beforeSend: function(){
            console.log('Добаялется в корзину')
        },
        success: function(response){
            this_val.html('Добавлено')
            console.log('Добавлено в корзину!')
            $('.cart-items-count').text(response.totalcartitems)
        }
    })

})