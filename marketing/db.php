<?php

    include "config.php";
    $mysqli = new mysqli($config['server'], $config['user'], $config['pass'], $config['db']);


        $name = $_POST["name"];
        $number = $_POST["number"];
        $text = $_POST["text"];
        $fcsv = fopen("text.csv", "a"); // Открываем файл в режиме записи 
        $textOut = $_POST["name"].";".$_POST["number"].";".$_POST["text"]."\r\n";
        $test = fwrite($fcsv, $textOut); 
        if (!$test) echo 'Ошибка при записи в файл.';
        fclose($fcsv);
        
        $sql = "INSERT INTO list (name,number,text) VALUES ('$name',$number,'$text') ";
        if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
    

        


    


?>