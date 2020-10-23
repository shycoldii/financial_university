<?php
if (isset($_POST["okbutton"]))
{

if ($_POST["name_of_guest"] == "")
exit("Введите имя <a href='questbook.php'>Назад!</a>");
if ($_POST["message_of_guest"] == "")
exit("Введите сообщение <a href='questbook.php'>Назад!</a>");
 
    $f=fopen("gost.txt","at") or die("Файл не открывается");
    flock($f,2);
    fputs($f,$_POST["name_of_guest"]."\n");
    fputs($f,$_POST["message_of_guest"]."\n");
    flock($f,3);
    fclose($f);
    }
    header("location:questbook.php");
?>
