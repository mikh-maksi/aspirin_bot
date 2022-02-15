<?php
$param = json_decode($_REQUEST["param"]);
//$result = "Результат: a = ".$param->id."; b = ".$param->description;
$res = $_REQUEST["param"];
//$result = $param[0]->description;




    $fp = fopen("analyticsIn2.txt", "a"); // Открываем файл в режиме записи 
                $mytext = $result." \r\n"; // Исходная строка
                $test = fwrite($fp, $mytext); // Запись в файл
                fclose($fp); //Закрытие файла
    include "../../config.php";
    include "../../connect.php";
    
    $sql = "UPDATE swotJSON SET param = '$res' WHERE id = 1";

    if (!$result = $mysqli->query($sql)) {
        echo $mysqli->error;$result->close(); 
    }
    

  
?>