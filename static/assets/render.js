

setInterval(function() {
    console.log('Doing..');
    fetch('/api/record', {
        method: 'POST'
    })
    var sshot = document.getElementById('img-frame');
    var wshot = document.getElementById("webcam-img");
    sshot.src = screen +'?rand=' + Math.random();
    wshot.src = snap +'?rand=' + Math.random();
}, 1500);


function screenshotnf() {
    document.getElementById('img-frame').src = errImg;
}

function webcamnf() {
    document.getElementById("webcam-img").src = errImg;
}
