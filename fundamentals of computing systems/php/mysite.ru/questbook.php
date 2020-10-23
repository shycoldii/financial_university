<meta charset="utf-8">
<html><head>
<title> Гостевая книга </title></head>
<body>
<form action="add_message.php" method="post"> 
Имя <br>  <input type="text" name="name_of_guest"><br>
Сообщение:<br>
<br>
<textarea name="message_of_guest" cols=10 rows=5>
</textarea>
<br><input type="submit" value="OK" name="okbutton">

</form>
</body>
</html>
<?php
$f=fopen("gost.txt","rt") or die("Не могу открыть файл");
while (!feof($f))
{
$data=fgets($f); //Получаем фамилию
echo "<small>Имя:</small>".$data."<br>";
$data=fgets($f); //Получаем сообщение
echo "<small>Сообщение:</small>".$data."<br>";
echo "<hr>";
}
fclose($f);
?>
