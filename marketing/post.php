<?php
 //   $json = $_REQUEST['json'];

# Получить JSON как строку
    $json_str = file_get_contents('php://input');

# Получить объект
    $json_obj = json_decode($json_str);

    $sqlSelect = "SELECT count(id) AS n FROM aspirinjson WHERE orgId = ". $json_obj->id."";

    $fp = fopen('counter.txt', 'a+');
    $name = $json_obj->name;
    $mytext = "$json_str.\r\n"; // Исходная строка
    $mytext = "$sqlSelect.\r\n"; // Исходная строка
    $mytext .= "$name.\r\n"; // Исходная строка
    $test = fwrite($fp, $mytext); // Запись в файл
    if ($test) echo 'Данные в файл успешно занесены.';
    else echo 'Ошибка при записи в файл.';
    fclose($fp); //Закрытие файла

    include "config.php";
    include "connect.php";


    $n_row = 0;
    if ($result = $mysqli->query($sqlSelect)) { 
        while($row = $result->fetch_assoc() ){
            $n_row = $row['n'];                   
        }
    }
    if ($n_row==0){
        $sq = "INSERT INTO aspirin (orgId,a,s,p,r,n) VALUES (". $json_obj->id.",". $json_obj->a.",". $json_obj->s.",". $json_obj->p.",". $json_obj->r.",". $json_obj->n.");";
        $sqljson = "INSERT INTO aspirinjson (orgId,json) VALUES (". $json_obj->id.",'". $json_str."');";

        if ($mysqli->query($sq)) {  } else {echo "Error: " . $sq . "<br>" . $mysqli->error; }
        if ($mysqli->query($sqljson)) {  } else {echo "Error: " . $sq . "<br>" . $mysqli->error; }
    }else{
        $sql = "UPDATE aspirinjson SET json ='". $json_str."' WHERE orgId = ". $json_obj->id."";
        if ($mysqli->query($sql)) {  } else {echo "Error: " . $sq . "<br>" . $mysqli->error; }
        $fp = fopen('counter.txt', 'a+');
        $mytext = "$sql.\r\n"; // Исходная строка
        $test = fwrite($fp, $mytext); // Запись в файл
        if ($test) echo 'Данные в файл успешно занесены.';
        else echo 'Ошибка при записи в файл.';
        fclose($fp); //Закрытие файла

    }
?>