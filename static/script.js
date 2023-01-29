document.querySelector('#product').addEventListener('change', function() {
    var product_id = this.value;
    var amount = document.querySelector('#amount').value;
    var supplier_products = JSON.parse('{{ supplier_products|json }}');
    var selected_product = supplier_products.find(function(product) {
      return product.id == product_id;
    });
    var total_cost = selected_product.price * amount;
    document.querySelector('#total_cost').value = total_cost;
  });
document.querySelector('#amount').addEventListener('change', function() {
    var product_id = document.querySelector('#product').value;
    var amount = this.value;
    var supplier_products = JSON.parse('{{ supplier_products|json }}');
    var selected_product = supplier_products.find(function(product) {
      return product.id == product_id;
    });
    var total_cost = selected_product.price * amount;
    document.querySelector('#total_cost').value = total_cost;
  });
document.getElementById("product").addEventListener("change", function(){
  var selectedProduct = this.options[this.selectedIndex];
  var price = selectedProduct.dataset.price;
  var amount = document.getElementById("amount").value;
  document.getElementById("total_cost").value = (price * amount).toFixed(2);
});
document.getElementById("amount").addEventListener("change", function(){
  var selectedProduct = document.getElementById("product").options[document.getElementById("product").selectedIndex];
  var price = selectedProduct.dataset.price;
  var amount = this.value;
  document.getElementById("total_cost").value = (price * amount).toFixed(2);
});
