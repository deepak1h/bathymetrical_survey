
<?php

$servername = "localhost" ;
$username = "id11590553_aeronicsdb";
$password = "aeblwGDuXzw*w*$7";
$database = "id11590553_aeronics";


$lat = $_REQUEST["lat"];
$lon = $_REQUEST["lon"];
$ele = $_REQUEST["ele"];
$dep = $_REQUEST["dep"];

if(isset($dep)&&isset($lon))
{

// create connection

$con =new mysqli($servername,$username,$password,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "INSERT INTO data (time, lat, lon, ele, dep) VALUES (CURRENT_TIME(), '$lat', '$lon', '$ele', 'dep')";

if($con->query($query)==TRUE)
{
	die("success");
}
else
{
	die("failed");
}
}
else
{
die("data not set");	
}

?>
