<?php
// Добавляем Клиента: Zoho_id, name, child_id, Выбранный курс
// 


    $name = $_REQUEST['name'];
    $adress = $_REQUEST['adress'];
    $inn = $_REQUEST['inn'];

    $kved = $_REQUEST['kved'];
    $group = $_REQUEST['group'];


    $fp = fopen("log_upload.txt", "a"); // Открываем файл в режиме записи 
                $mytext = $name." ".$adress." ".$inn." \r\n"; // Исходная строка
                $test = fwrite($fp, $mytext); // Запись в файл
                fclose($fp); //Закрытие файла
    
    include "../config.php";
    include "../connect.php";
    
    class answer{
        var $answer;
        var $id;
        var $code;
        var $inn;
        }  
    
    $answ = new answer();


    $sql = "SELECT * FROM organisation WHERE inn = $inn";
    $out = false;
    $flag = false;
    if ($result = $mysqli->query($sql)) { 
        while($row = $result->fetch_row() ){
            $out = $row[0];
            $flag = true;
        } 
        $result->close(); 
    }

    if(!$out){
        $sql = "INSERT INTO organisation (name, adress, inn) VALUES ('$name','$adress','$inn')";
        if (!$result = $mysqli->query($sql)) {
            echo $mysqli->error;$result->close(); 
        }
        $id = $mysqli->insert_id;
        $kvedArray = explode('|',$kved);

        foreach ($kvedArray as $value){
            $sql = "INSERT INTO kvedOrg (orgId, kvedClassId) VALUES ($id,'$value')";
            if (!$result = $mysqli->query($sql)) {
                echo $mysqli->error;$result->close(); 
            }
        }
        $answ->answer = "New record";
        $answ->id = $id;
        $answ->code = 1;
        $answ->inn = $inn;

    } else{
        $answ->answer = "Already";
        $answ->id = $out;
        $answ->code = 2;
        $answ->inn = $inn;
    }

    header('Access-Control-Allow-Origin: *');
    header('Content-type: application/json; charset=utf-8');

    echo json_encode($answ);
    
?>