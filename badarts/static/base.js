$(document).ready(function(){
    $('.carousel').carousel();
    $('.truncate-btn').on('click', function(e){
        $('#artist-bio').toggleClass('truncate');
    });
});
