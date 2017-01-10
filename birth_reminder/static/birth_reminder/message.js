
$("#id_message").on("change",function(){
        console.log($('#id_message').val());
        $.ajax({
            type:'POST',
            url:'/birth_reminder/update_message/',
            data:{
                id_message:$('#id_message').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response){
                //$('#id_message_text').val(response.id_message_text);
                //$('#id_message_subject').val(response.id_message_subject);
                $('#id_msg_subject').val(response.id_message_subject);
                $('#id_msg_text').val(response.id_message_text);
            }
});
return false;});

function disableForm(){
    $("#id_send_time").prop("disabled",true);
    $("#id_message").prop("disabled",true);
    $("#id_msg_subject").prop("disabled",true);
    $("#id_msg_text").prop("disabled",true);
}

function enableForm(){
    $("#id_send_time").prop("disabled",false);
    $("#id_message").prop("disabled",false);
    $("#id_msg_subject").prop("disabled",false);
    $("#id_msg_text").prop("disabled",false);
}

$("#id_is_active").on("change",function(){
        if (!$(this).is(":checked"))//unchecked
            disableForm();
        else
            enableForm();
});

window.onload=function(){
    //console.log($("#id_is_active").is(":checked"));
    if(!$("#id_is_active").is(":checked"))
    {
        disableForm();
    }
    else
    {
        enableForm();
    }
};

$(document).ready(function(){
    $("input:reset").click(function(){
        this.form.reset();
        if(!$("#id_is_active").is(":checked"))
            disableForm();
        else
            enableForm();
    });
});
