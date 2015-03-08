
$(document).ready(function(){

    init_remove_confirmation();

});

function init_remove_confirmation(){
    $(".remove-confirmation").click(function(){
        $('#remove_confirmation').find("span#link").html($(this).attr('href'));
        $('#remove_confirmation').modal("show");
        return false;
    });

    $('#remove_confirmation').find('#yes').click(function(){
        var url = $('#remove_confirmation').find("span#link").html();
        window.location = url;
    });
}
