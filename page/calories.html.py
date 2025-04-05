<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello! Pavlova.S | Калории</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="анонимно">
    <link rel="stylesheet" href="../src/css/style.css">
    
  </head>
  <body>
    
    <!-- Navbar -->
   <header>
    <nav class="navbar navbar-expand-lg fixed-top">
        <div class="container">
            <a class="navbar-brand" href="../index.html"><span class="text-warning">Hi!</span><span class="text-muted">Cal</span></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active text-muted" href="calories.html">Калории</a>
              </li>
              <li class="nav-item">
                <a class="nav-link text-muted" href="recipe.html">Рецепты</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
   </header>


<!-- Carousel -->
<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
    
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="../img/carousel1.jpg" class="d-block w-100" id ="menu"alt="...">
        <div class="carousel-caption ">
          <h5>Check Kalori Yuk</h5>
          <p>Узнайте, сколько калорий поступает в ваш организм.</p>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Cari tahu Kalori" aria-label="Recipient's username" aria-describedby="basic-addon2">
            <div class="input-group-append">
              <span onclick="window.location.href='pizza.html'" class="input-group-text" id="basic-addon2">Поиск</span>
            </div>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <img src="../img/carousel2.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption ">
          <h5>Check Kalori Yuk</h5>
          <p>Узнайте, сколько калорий поступает в ваш организм.</p>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Cari tahu Kalori" aria-label="Recipient's username" aria-describedby="basic-addon2">
            <div class="input-group-append">
              <span onclick="window.location.href='#portfolio'" class="input-group-text" id="basic-addon2">Поиск</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- about section -->
  <section id="about" class="about section-padding">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-12 col-12">
          <div class="about-img">
            <img src="../img/about.jpg" class="img-fluid" alt="">
          </div>
        </div>
        <div class="col-lg-8 col-md-12 col-12 ps-lg-5 mt-md-5">
          <div class="about-text text-primary">
            <h2>
              Какова его калорийность?
            </h2>
            <p style="color:white">
              Калорийность - это величина или единица измерения, которая показывает, сколько энергии можно получить из продуктов питания и напитков. Поэтому важно всегда удовлетворять свои ежедневные потребности в калориях, чтобы вы были более энергичны, когда находитесь в движении.
            </p>
            <a class="btn btn-primary mt-3" href="calories.html" role="button">Смотрите количество калорий</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  
 <!-- Footer -->
 <footer class="py-3 my-4">
  <ul class="nav justify-content-center border-bottom pb-3 mb-3">
    <li class="nav-item"><a href="../index.html" class="nav-link px-2 text-muted">Главная</a></li>
    <li class="nav-item"><a href="calories.html" class="nav-link px-2 text-muted">Калории</a></li>
    <li class="nav-item"><a href="recipe.html" class="nav-link px-2 text-muted">Рецепты</a></li>
  </ul>
  <p class="text-center text-muted">© 2025 Pavlova.S</p>
</footer>

    <!-- js -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>

  </body>
</html>