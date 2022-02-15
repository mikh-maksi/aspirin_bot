<?php
    header('Content-Type: text/html; charset=utf-8');
    include "config.php";
    include "connect.php";
?><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    <script
        src="https://code.jquery.com/jquery-3.3.1.min.js"
        integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
        crossorigin="anonymous"></script>
</head>
<body>
    <?php 
    ?>
   <!-- <form action="back/fop.php" method="get">-->
    <div class="wrapper">
        <h2>Регистрация</h2>
        <table class = "table">
        <tr>
                <td>П.І.Б.</td>
                <td><input type="text" id = "name"></td>
            </tr>
            <tr>
                <td>Zoho Code</td>
                <td><input type="text" id = "inn"></td>
            </tr>
            <tr>
                <td>Вік дитини</td>
                <td><input type="text" id = "child_age" ></td>
            </tr>



            <tr>
                <td colspan = 2>  <button id ="send">Send</button>
                <!--<input type="submit" value = "send">-->
                </td>
            </tr>
        </table>
        <div id="output"></div>
        <!-- </form> -->
           <script>
    function kved_Plus(){
        var inpts = kveddiv.getElementsByClassName("kved");
        console.log(inpts.length);
        var kvedInpt = document.createElement('input');
        kvedInpt.className = "kved";
        kvedInpt.id = "kved"+inpts.length;
        kvedInpt.setAttribute("list", "kvedList") ;
        kvedInpt.setAttribute("name", "kved") ;
        kveddiv.appendChild(kvedInpt);
    }
    kvedPlus.addEventListener("click",kved_Plus);

    $('#send').on('click', function() {
    var inpts = kveddiv.getElementsByClassName("kved");
    var kved_data = '';
    for (i=0;i<inpts.length;i++){
        console.log(inpts[i].value);
        kved_data += inpts[i].value ;
        if (i<inpts.length-1) kved_data +='|';
    }
 
    
    var name_data = $('#name').val();
    var inn_data = $('#inn').val();
    var adress_data = $('#adress').val();
    var group_data = $('#group').val();   

    console.log(name_data);
    console.log(inn_data);
    console.log(adress_data);
    console.log(group_data);
    console.log(kved_data);

    var form_data = new FormData();
    form_data.append('name',name_data);
    form_data.append('adress',adress_data);    
    form_data.append('inn',inn_data);
    form_data.append('kved',kved_data);   
    form_data.append('group',group_data); 

    $.ajax({
                url: 'back/start.php',
                dataType: 'text',
                cache: false,
                contentType: false,
                processData: false,
                data: form_data,
                type: 'post',
                success: function(php_script_response){
                 var res = JSON.parse(php_script_response)
                    console.log(res);
                    document.getElementById("output").innerHTML="";
                var msg = document.createElement("div");
                msg.setAttribute('role', 'alert');

                if (res.code==1){
                    var str = "Пользователь с ИНН "+res.inn+" успешно зарегистрирован успешно!";
                    msg.className = "alert alert-success";
                }
                if (res.code==2){
                    var str = "Пользователь с ИНН "+res.inn+" уже существует!";
                    msg.className = "alert alert-warning";
                }
                var node = document.createTextNode(str);
                msg.appendChild(node);
                output.appendChild(msg);
                var info = document.createElement("div");
                
                info.innerHTML = '<div class="alert alert-success" role="alert">  <h4 class="alert-heading">Информация для пользователя!</h4>  <p>Для просмотра данных Вам необходимо перейти в раздел <a href = "organisation.php?id='+res.id+'&inn='+res.inn+'">Страница организации/ФЛП ИНН('+res.inn+').</a> При входе необходимо будет указать свой ИНН и электронную почту, указанную при регистрации</p>  <hr>  <p class="mb-0">В указанном разделе Вы сможете ввести данные и просмотреть уже введенные данные</p></div>';            
                
                output.appendChild(info);


                }
     });
});
    </script>
    </div>
</body>
</html>