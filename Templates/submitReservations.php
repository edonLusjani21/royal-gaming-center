<?php
// Connection parameters for your SQL Server
$serverName = "EDONLUSJANI\\Sqlexpress";  // Use double backslashes to escape the backslash
$connectionOptions = array(
    "Database" => "Ticsys", // The database you want to connect to
    "Uid" => "your_username", // Your SQL Server username
    "PWD" => "your_password" // Your SQL Server password
);

// Establishes the connection to the SQL Server
$conn = sqlsrv_connect($serverName, $connectionOptions);

// Check connection
if (!$conn) {
    die("Connection failed: " . sqlsrv_errors());
}

// Get data from the form (make sure to sanitize input in a real scenario)
$name = $_POST['name'];
$date = $_POST['date'];
$time = $_POST['time'];
$pcs = implode(", ", $_POST['pcs']); // Assuming the selected PCs are passed as an array

// SQL Query to insert reservation data
$query = "INSERT INTO Reservations (Name, Date, Time, PCs) VALUES (?, ?, ?, ?)";
$params = array($name, $date, $time, $pcs);

// Execute the query
$stmt = sqlsrv_query($conn, $query, $params);

if ($stmt) {
    echo "Reservation successfully submitted!";
} else {
    echo "Error: " . sqlsrv_errors();
}

// Close the connection
sqlsrv_close($conn);
?>
