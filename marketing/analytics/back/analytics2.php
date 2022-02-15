<?php
    $name = $_REQUEST['name'];
    $adress = $_REQUEST['adress'];
    $inn = $_REQUEST['inn'];

    $kved = $_REQUEST['kved'];
    $group = $_REQUEST['group'];


    $fp = fopen("analytics2.txt", "a"); // Открываем файл в режиме записи 
                $mytext = $name." ".$adress." ".$inn." \r\n"; // Исходная строка
                $test = fwrite($fp, $mytext); // Запись в файл
                fclose($fp); //Закрытие файла
    
    /*
    if ( 0 < $_FILES['file']['error'] ) {
        echo 'Error: ' . $_FILES['file']['error'] . '<br>';
    }
    else {
        move_uploaded_file($_FILES['file']['tmp_name'], 'uploads/' . $_FILES['file']['name']);
    }
  */
    include "../../config.php";
    include "../../connect.php";

    $sql = "INSERT INTO swot (type, n, description) VALUES (1,1,'Сильная сторона 1')";
    if (!$result = $mysqli->query($sql)) {
        echo $mysqli->error;$result->close(); 
    }

    $sql = "INSERT INTO swot (type, n, description) VALUES (2,1,'Слабая сторона 1')";
    if (!$result = $mysqli->query($sql)) {
        echo $mysqli->error;$result->close(); 
    }
    $sql = "INSERT INTO swot (type, n, description) VALUES (3,1,'Возможность 1')";
    if (!$result = $mysqli->query($sql)) {
        echo $mysqli->error;$result->close(); 
    }
    $sql = "INSERT INTO swot (type, n, description) VALUES (4,1,'Угроза 1')";
    if (!$result = $mysqli->query($sql)) {
        echo $mysqli->error;$result->close(); 
    }




?>