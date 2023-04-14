const updateBtns = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log("id: "  , productId, "action: " , action)
        console.log(user)

        if (user === 'AnonymousUser') {
            console.log("Not Authenticated");
        } else {
            updateUserOrder(productId, action)
        }
    })
    
}

function updateUserOrder(productId, action) {
    let url = '/update_item/'

    fetch(url, {
        method: "post",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrftoken, 
        },

        body: JSON.stringify({'productId' : productId, "action" : action})
    }).then((response) => {
        return response.json()
    }).then((data) =>{
       console.log("DATA: ", data )
       location.reload()
    })

}