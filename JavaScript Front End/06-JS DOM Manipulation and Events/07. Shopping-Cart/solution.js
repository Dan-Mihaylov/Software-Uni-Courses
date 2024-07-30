function solve() {
   const cart = {};   // will keep {'productName': price}
   const resultElement = document.querySelector('textarea');

   Array.from(document.getElementsByClassName('product'))
      .forEach(el=>{
         el.addEventListener('click', addProduct);
      })

   function addProduct(event) {
      
      if (event.target.className !== 'add-product') {
         return;
      }

      const productName = event.target.parentNode.parentNode
         .querySelector('.product-details .product-title').textContent;
      
      const productPrice = Number(event.target.parentNode.parentNode
         .querySelector('.product-line-price').textContent).toFixed(2);

      addToCart(productName, productPrice);

      resultElement.textContent += `Added ${productName} for ${productPrice} to the cart.\n`

   }

   function addToCart(product, price) {
      if (!cart[product]) {
         cart[product] = 0;
      }
      cart[product] += Number(price);
   }

   document.querySelector('button.checkout').addEventListener('click', (e)=>{
      const productList = Object.keys(cart);
      const totalPrice = Object.values(cart).reduce((prev, curr)=>{return prev + curr}, 0).toFixed(2);

      resultElement.textContent += `You bought ${productList.join(', ')} for ${totalPrice}.`;

      Array.from(document.querySelectorAll('button'))
         .forEach(btn=>{
            btn.setAttribute('disabled', 'disabled');
         })
   })
}

//"Added {name} for {money} to the cart.\n"
// price to second digit
// "You bought {list} for {totalPrice}."