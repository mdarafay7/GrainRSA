<!DOCTYPE html>
<html>
<head>
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php


$con = mysqli_connect('localhost','abdo','test123','TESTDB');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"ajax_demo");
$sql="SELECT * FROM user WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<th>DATE</th>
<th>ID</th>
<th>SETTLEMENT</th>
<th>HIGH</th>
<th>LOW</th>
<th>VOLUME</th>
<th>OPEN_INT</th>

</tr>";
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['DATE'] . "</td>";
    echo "<td>" . $row['ID'] . "</td>";
    echo "<td>" . $row['COMMODITY'] . "</td>";
    echo "<td>" . $row['SETTLEMENT'] . "</td>";
    echo "<td>" . $row['HIGH'] . "</td>";
    echo "<td>" . $row['LOW'] . "</td>";
    echo "<td>" . $row['VOLUME'] . "</td>";
    echo "<td>" . $row['OPEN_INT'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>
