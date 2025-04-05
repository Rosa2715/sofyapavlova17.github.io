*{
    font-family: montserrat;
}
body{
    background: flfbff;
    background-color: #010101;
    color: white;
}
.bg-primary {
    background-color: #202429!important;

}
.text-primary {
    color: #edb50a!important;
}
.card {
    margin: 0 auto; /* Added */
    float: none; /* Added */
    margin-bottom: 10px; /* Added */
}
.section-padding{
    padding: 100px 0;
}
.carousel-item{
    height: 100vh;
    min-height: 300px;
}
.input-group-append{
    cursor: pointer;
}
.carousel-caption{
    bottom: 220px;
    z-index: 2;
}
.carousel-caption h5{
    font-size: 45px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 25px;
}
.carousel-caption p{
   width: 60%; 
   margin: auto;
   font-size: 18px;
   line-height: 1.9;
}

.carousel-inner::before{
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.7);
    z-index: 1;
}
.nav-link {
    color: #edb50a!important;
}
.navbar {
    background-color: #131716;
}
.navbar-nav a{
    font-size: 15px;
    text-transform: uppercase;
    font-weight: 500;
}
.navbar-ligth .navbar-brand{
    color: #000;
    font-size: 25px;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 2px;
}
.navbar-ligth .navbar-brand:focus,
.navbar-ligth .navbar-brand.hover{
    color: #000;
}
.navbar-ligth .navbar-nav.navbar-link{
    color: #000;
}
.w-100{
    height: 100vh;
}


.services .card-body i{
    font-size: 50px;
}


/* responsive css */

@media only screen and (min-width: 768px) and (max-width: 991px){
    .carousel-caption{
        bottom: 370px;
    }
    .carousel-caption p{
        max-width: 100%;
    }
}

@media only screen and(max-width: 767px){
    .navbar-nav{
        text-align: center;
    }
    .carousel-caption{
        bottom: 125px;
    }
    .carousel-caption h5{
        font-size: 17px;
    }
    .carousel-caption a{
        padding: 10px 15px;
    }
    .carousel-caption p{
        width: 100%;
        line-height: 1.6;
        font-size: 12px;
    }
}