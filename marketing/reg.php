<?php
    //header('Content-Type: text/html; charset=utf-8');
    include "config.php";
    $mysqli = new mysqli($config['server'], $config['user'], $config['pass'], $config['db']);
    mysqli_set_charset ($mysqli,"utf8");
    $name = $_REQUEST["name"];
    $business_type = $_REQUEST["business_type"];
    $inn = $_REQUEST["inn"];
    $kved = $_REQUEST["kved"];
    $nEmpl = $_REQUEST["nEmpl"];
    $turnover = $_REQUEST["turnover"];
    $sql = "INSERT INTO `users` (`id`, `name`, `business_type`, `kved`, `nEmpl`, `turnover`, `inn`) VALUES (NULL, '$name', $business_type,'$kved',  $nEmpl, $turnover,$inn )";
    if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }


    $jsonOut = array('result' => '1');
    header('Content-type: application/json');
    echo json_encode($jsonOut);
?>