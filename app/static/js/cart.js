function addCount(stock) {
    var element = document.getElementById("countNumber");
    if(element.value < stock) {
    element.value = parseInt(element.value)+ 1;
    }
};

function removeCount() {
    var element = document.getElementById("countNumber");
    if(element.value > 1) {
    element.value = parseInt(element.value) - 1;
    } 
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function addToCart(productId) {
    var cart = JSON.parse(getCookie('shopping_cart'));
    if (cart == null) {
        cart = {};
    }
    product_id = parseInt(productId);
    if (!(product_id in cart)) {
        cart[product_id] = 0;
    }
    cart[product_id] = cart[product_id] + parseInt(document.getElementById("countNumber").value);
    setCookie('shopping_cart', JSON.stringify(cart), 100);
}

function addToCartByAmount(productId, amount) {
    var cart = JSON.parse(getCookie('shopping_cart'));
    if (cart == null) {
        cart = {};
    }
    product_id = parseInt(productId);
    if (!(product_id in cart)) {
        cart[product_id] = 0;
    }
    cart[product_id] = amount + 1;
    setCookie('shopping_cart', JSON.stringify(cart), 100);
}

function removeFromCart(product_id) {
    var cart = JSON.parse(getCookie('shopping_cart'));
    if (cart == null) {
        cart = {};
    }
    if (product_id in cart && cart[product_id] > 0) {
        cart[product_id] = cart[product_id] - 1;
    }
    setCookie('shopping_cart', JSON.stringify(cart), 100);
}

function removeAllFromCart(product_id) {
    var cart = JSON.parse(getCookie('shopping_cart'));
    if (cart == null) {
        cart = {};
    }
    if (product_id in cart && cart[product_id] > 0) {
        cart[product_id] = 0;
    }
    setCookie('shopping_cart', JSON.stringify(cart), 100);
}