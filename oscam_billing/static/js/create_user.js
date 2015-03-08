$(document).ready(function(){
    $("[name=select_dealer]").closest("div.form-group").hide();

    $("select[name=user_role]").change(function(){
        var value = $(this).val();
        if(value=="dealer"){
            $("[name=select_dealer]").closest("div.form-group").hide();
            $("[name=comission]").closest("div.form-group").show();
        } else {
            $("[name=select_dealer]").closest("div.form-group").show();
            $("[name=comission]").closest("div.form-group").hide();
        }
    });
});
