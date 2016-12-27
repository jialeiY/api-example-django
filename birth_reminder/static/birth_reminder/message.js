
$("#id_message_name").on("change",function(){
        console.log($('#id_message_name').val());
        $.ajax({
            type:'POST',
            url:'/birth_reminder/update_message/',
            data:{
                id_message_name:$('#id_message_name').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response){
                $('#id_message_text').val(response.id_message_text);
                $('#id_message_subject').val(response.id_message_subject);
             /*   location.reload();
                console.log('yyysd');*/
            }
});
return false;});
