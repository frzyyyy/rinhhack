<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>
<body>
    <form action="#" method="POST">
        <label>Название</label>
        <input type="text" name="name">
        <label>Категория</label>
        <input type="select" name="category">
        <label>Описание</label>
        <input type="text" name="description">
        <label>Сроки</label>
        <input type="date" name="date">
        <label>Организатор</label>
        <input type="text" name="author">
        <button type="submit" value="add">Создать</button>
    </form>
    <ul>
		<?php
		require 'connect.php';
		$query = $pdo->query('SELECT * FROM `user_task` ORDER BY `id` DESC');
		while($row = $query->fetch(PDO::FETCH_OBJ)) {
		        echo '<div><li>'. $row->title .' <a href="delete.php?id='.$row->id.'" id="card-link-click">X</a></li>' . ' </div>';
			}
		 ?>
	</ul>
    <!-- <form>
    <div class="form-group">
    <label for="formGroupExampleInput">Название</label>
    <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder">
    </div>
    <div class="form-group">
    <label for="exampleFormControlSelect1">Категория</label>
    <select class="form-control" id="exampleFormControlSelect1">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
    </div>
    <div class="form-group">
    <label for="exampleFormControlTextarea1">Описание</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
    <div class="form-group">
    <label for="exampleFormControlFile1">Изображение</label>
    <input type="file" class="form-control-file" id="exampleFormControlFile1">
    </div>
    <label for="date">Сроки</label>
    <input type="date" id="date" name="date"/>
    <button type="submit" class="btn btn-primary">Создать</button>
    </form> -->
    <!-- <div class="card" style="width: 18rem;">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Заголовок задачи</h5>
    </div>
    </div> -->
</body>
</html>