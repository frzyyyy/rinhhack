<?php
    require_once 'connect.php';
    $name = $_POST['name'];
    $category = $_POST['category'];
    $description = $_POST['description'];
    $date = $_POST['date'];
    $author = $_POST['author'];

    $sql = 'INSERT INTO user_task(name, category, description, date, author) VALUES(:name, :category, :description, :date, :author)';

	$query = $pdo->prepare($sql);

	$query->execute(
        array(":name" => $name,
              ":category" => $category,
              ":description" => $description,
              ":date" => $date,
              ":author" => $author)
    );

	header('Location: index.php');

?>