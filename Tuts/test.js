function sendWhatsAppMessage(recipient, message) {
    var url = "https://web.whatsapp.com/send?phone=" + recipient + "&text=" + encodeURIComponent(message);
    window.open(url);
  }
  
sendWhatsAppMessage('8979466093', 'Hello, World!');  