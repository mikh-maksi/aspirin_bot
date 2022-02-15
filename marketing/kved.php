<?php
include "config.php";
include "connect.php";

$fp = fopen("kved.json", "r"); // Открываем файл в режиме чтения
$full_text = '';
if ($fp) {
    while (!feof($fp)){
        //echo $i++;
        $mytext = fgets($fp, 999);
       // Echo $mytext;
        $full_text .= $mytext;
}
}
else echo "Ошибка при открытии файла";
fclose($fp);
//var_dump(json_decode($full_text));
$data = json_decode($full_text);

echo $data->sections[0][0]->sectionCode;
echo "<br>";
echo "<b>".count($data->sections[0])."</b>";
$n = count($data->sections[0]);
$sql = "TRUNCATE sections";
if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
$sql = "TRUNCATE groups";
if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
$sql = "TRUNCATE divisions";
if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
$sql = "TRUNCATE classes";
if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }






for($i=0;$i<$n;$i++){
    echo "<h2>".$data->sections[0][$i]->sectionCode.". ";
    echo $data->sections[0][$i]->sectionName."</h2>";
    $sql = "INSERT INTO sections (sectionCode,sectionName) VALUES
    ('".$data->sections[0][$i]->sectionCode."','".addslashes($data->sections[0][$i]->sectionName)."')";
    if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
   



    $n1 = count($data->sections[0][$i]->divisions);
    for($j=0;$j<$n1;$j++){
        echo "<h3>".($data->sections[0][$i]->divisions[$j]->divisionCode).". ";
        echo ($data->sections[0][$i]->divisions[$j]->divisionName)."</h4>";
        $sql = "INSERT INTO divisions (divisionsCode,divisionsName,sectionId) VALUES
        ('".$data->sections[0][$i]->divisions[$j]->divisionCode."','".addslashes($data->sections[0][$i]->divisions[$j]->divisionName)."','".$data->sections[0][$i]->sectionCode."')";
        if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
       
        $n2 = count($data->sections[0][$i]->divisions[$j]->groups);
        for($k=0;$k<$n2;$k++){
            echo "<h4>".($data->sections[0][$i]->divisions[$j]->groups[$k]->groupCode).". ";
            echo ($data->sections[0][$i]->divisions[$j]->groups[$k]->groupName)."</h4>";
            $sql = "INSERT INTO groups (groupCode,groupName,divisionId) VALUES
            ('".$data->sections[0][$i]->divisions[$j]->groups[$k]->groupCode."','".addslashes($data->sections[0][$i]->divisions[$j]->groups[$k]->groupName)."','".$data->sections[0][$i]->divisions[$j]->divisionCode."')";
            if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }

            $n3 = count($data->sections[0][$i]->divisions[$j]->groups[$k]->classes);
            for($l=0;$l<$n3;$l++){
                $sql = "INSERT INTO classes (classCode,className,groupId) VALUES
                ('".$data->sections[0][$i]->divisions[$j]->groups[$k]->classes[$l]->classCode."','".addslashes($data->sections[0][$i]->divisions[$j]->groups[$k]->classes[$l]->className)."','".$data->sections[0][$i]->divisions[$j]->groups[$k]->groupCode."')";
                if (!$result = $mysqli->query($sql)) { echo "Ошибка: " . $mysqli->error . "\n";   exit;    }
                echo "<h5>".($data->sections[0][$i]->divisions[$j]->groups[$k]->classes[$l]->classCode).". ";
                echo ($data->sections[0][$i]->divisions[$j]->groups[$k]->classes[$l]->className)."</h5>";
            }   
        }
    }
}
echo "<br>";
echo $data->sections[0][0]->sectionName;
echo "<br>";
echo "<b>".count($data->sections[0][0]->divisions)."</b>";
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->divisionCode);
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->divisionName);

echo "<br>";
echo "<b>".count($data->sections[0][0]->divisions[0]->groups)."</b>";
echo "<br>";

echo ($data->sections[0][0]->divisions[0]->groups[0]->groupCode);
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->groups[0]->groupName);
echo "<br>";
echo "<b>".count($data->sections[0][0]->divisions[0]->groups[0]->classes)."</b>";
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->groups[0]->classes[0]->classCode);
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->groups[0]->classes[0]->className);
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->groups[0]->classes[1]->classCode);
echo "<br>";
echo ($data->sections[0][0]->divisions[0]->groups[0]->classes[1]->className);
echo "<br>";




var_dump( $data->sections[0][0]);


?>