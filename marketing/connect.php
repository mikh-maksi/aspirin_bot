<?php

$mysqli = new mysqli( $config["server"], $config["login"], $config["pass"], $config["db"]);  

//$mysqli = mysqli_connect( $config["server"], $config["login"], $config["pass"], $config["db"]);  


if (!$mysqli) { printf("Невозможно подключиться к базе данных. Код ошибки: %s\n", mysqli_connect_error());   exit; 
} 

mysqli_set_charset ($mysqli,"utf8");
/*
if (!$mysqli->set_charset("utf8")) {printf("Ошибка при загрузке набора символов utf8: %s\n", $mysqli->error); exit();
} else {
// printf("Текущий набор символов: %s\n", $link->character_set_name());
}
*/
