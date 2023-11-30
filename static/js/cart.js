let updateBtns = document.getElementsByClassName('update-cart')

for(let i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:',productId,'action',action)

        console.log('USER :',user)

        if (user == 'AnonymousUser') {
            addCookieItem(productId,action)
        }else{
            updateUserOrder(productId,action)
        }
    })    
}

function addCookieItem(productId,action){
    console.log("user is not authenticated")

    if(action == 'add'){
        if(productId == undefined){
            cart[productId] = {'quantity':1}
        }else{
            if (!cart[productId]) {
                cart[productId] = { 'quantity': 1 };
            } else {
                cart[productId]['quantity'] += 1;
            }
        }
    }

    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <=0){
            console.log('item deleted')
            delete cart[productId];
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
    console.log('cart',cart)
    location.reload()
        
}

function updateUserOrder(productId,action){
    console.log("user is authenticated , sending data ...");

    let url = '/update-cart/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body : JSON.stringify({'productId':productId,'action':action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) => {
        console.log('data:',data);
        location.reload()
    })
    .catch((error) => {
        console.error('Fetch error:', error);
    });

}