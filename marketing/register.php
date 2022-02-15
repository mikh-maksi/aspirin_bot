<?php
    include "config.php";
    include "connect.php";

    $name = $_REQUEST["name"];
    $business_type = $_REQUEST["business_type"];
    $inn = $_REQUEST["inn"];
    $kved = $_REQUEST["kved"];
    $nEmpl = $_REQUEST["nEmpl"];
    $turnover = $_REQUEST["turnover"];

    $fcsv = fopen("text.csv", "a"); // Открываем файл в режиме записи 
    $textOut = $_REQUEST["name"].";".$_REQUEST["business_type"].";".$_REQUEST["inn"].";".$_REQUEST["kved"].";".$_REQUEST["nEmpl"].";".$_REQUEST["turnover"]."\r\n";
    $test = fwrite($fcsv, $textOut); 
    if (!$test) echo 'Ошибка при записи в файл.';
    fclose($fcsv);

    echo $_REQUEST["name"].";".$_REQUEST["business_type"].";".$_REQUEST["inn"].";".$_REQUEST["kved"].";".$_REQUEST["nEmpl"].";".$_REQUEST["turnover"];

    $sq = "INSERT INTO users (name,business_type,inn,kved,nEmpl,turnover) VALUES ('$name',$business_type,$inn,'$kved',$nEmpl,$turnover);";

    $sq = "INSERT INTO users (name,inn) VALUES ('max',342);";
    echo $sq;

    echo $mysqli;
  
    if ($mysqli->query($sq)) {  } else {echo "Error: " . $sq . "<br>" . $mysqli->error; }

    echo $res;
?>