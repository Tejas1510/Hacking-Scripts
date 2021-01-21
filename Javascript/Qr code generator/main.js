var qrData = document.querySelector("#qr-data");
var qrCode = new QRCode(document.querySelector("#qrcode"));

function qrGenerator() {


    var data = qrData.value;
    qrCode.makeCode(data);

}