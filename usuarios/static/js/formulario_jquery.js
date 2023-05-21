// $("#formulario_contacto").validate({
//     rules:{
//         nombre:{
//             required: true,
//             minlenght: 1,
//             maxlenght: 30,
//         },
//         email:{
//             required: true,
//             email: true
//         },
//         comentarios:{
//             required: true,
//             minlenght: 1,
//             maxlenght: 200,
//             remote: true
//         }
//     }
// });


// $("#btnSubIndex").click(function() {
//     if ($("#formulario_contacto").valid() == false){
//         return;
//     }
//     let nombre = $("#nombre").val()
//     let email = $("#email").val()
//     let comentarios = $("#comentario").val()
// });


$(document).ready(function(){
    $(".error").hide();
    $(".errorNombre").hide();
    $(".errorComment").hide();
    $("#btnSubIndex").click(function(){
        var nombre ="";
        nombre = $("#nombre").val();
        if(nombre.length==0){
            $(".errorNombre").show();
        }else{
            $(".errorNombre").hide();
        }
        var email ="";
        var at=0;
        email = $("#email").val();
        for (var i = 0, j = email.length; i < j; i++){
            if(email[i] == "@"){
                at++;
            }
        }
        if(at == 1){
            $(".error").hide();
        }else{
            $(".error").show();
        }   
        var comment = "";
        comment = $("#comentario").val();
        if(comment.length==0){
            $(".errorComment").show();
        }else{
            $(".errorComment").hide();
        }
    });
});