<meta charset="utf-8">
<html><head></head> 
<body>
<?php
if (isset($_POST["okb"]))
{
echo "Получатель 
".$_POST["person"];
$komu="cashaev@rambler.ru";
$tema="Вопрос от ".$_POST["person"]." ".$_POST["email"];
$text_pisma=$_POST["q"];
$z=mail($komu,$tema,$text_pisma);
}
 
?>
</body> </html>