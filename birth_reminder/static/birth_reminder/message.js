
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
