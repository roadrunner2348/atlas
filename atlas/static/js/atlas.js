str = $(".barcode-39").first().text();
$(".barcode-39").barcode( str, "code39", {barHeight:20, fontSize:14});

$(".chosen-select").chosen();

$(".tolowercase").keyup(function () {
  this.value = this.value.toLowerCase();
});
