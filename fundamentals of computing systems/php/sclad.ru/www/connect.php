<meta charset="utf-8">
<?php
$sqlhost="localhost";
$sqluser="mysql";
$sqlpass="mysql";
$db="Firma";
mysql_connect($sqlhost,$sqluser,$sqlpass) or die("MySQL is unallowed ".mysql_error());
mysql_select_db($db) or die("no connection with database".mysql_error());
?>
