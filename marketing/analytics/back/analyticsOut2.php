<?php
    $name = $_REQUEST['name'];
    $adress = $_REQUEST['adress'];
    $type = $_REQUEST['type'];

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

   
    class swot{
        var $id;
        var $type;
        var $n;
        var $description;
        var $priority;
        }  
    
    $swt = new swot();
/*
    $sql = "SELECT * FROM swot INNER JOIN swotTypes
    ON swot.type = swotTypes.id ORDER BY swot.type";
    if (isset($_REQUEST['type']))     $sql = "SELECT * FROM swot WHERE type = ".$_REQUEST['type'];
    if ($result = $mysqli->query($sql)) { 
        while($row = $result->fetch_row() ){
            $out = $row[0]." ".$row[1]." ".$row[2]." ".$row[3];
            $swt = new swot();
            $swt->id = $row[0];
            $swt->type = $row[6];
            $swt->n = $row[2];
            $swt->description = $row[3];
            $swt->priority = $row[4];
            
            $swts[] = $swt;
        } 
        $result->close(); 
    }
*/


$sql = "SELECT * FROM swotJSON WHERE id = 1";

if ($result = $mysqli->query($sql)) {
    while($row = $result->fetch_row() ){ 
    $answer = $row[1];
    }
}
    header('Access-Control-Allow-Origin: *');
    header('Content-type: application/json; charset=utf-8');

   // echo json_encode($swts);
   echo $answer;

?>