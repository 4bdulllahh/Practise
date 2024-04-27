window.onload = function() {
    var video = document.getElementById('myVideo');
    video.onended = function() {
        video.play();
    };
};
