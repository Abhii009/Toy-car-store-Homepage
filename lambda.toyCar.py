def lambda_handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Toy Car Store India</title>

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family: Arial, sans-serif;
            }

            body{
                background:#f5f7fa;
                color:#333;
            }

            header{
                background:#0f172a;
                color:white;
                padding:20px 40px;
                display:flex;
                justify-content:space-between;
                align-items:center;
            }

            .logo{
                font-size:28px;
                font-weight:bold;
            }

            nav a{
                color:white;
                text-decoration:none;
                margin-left:20px;
                font-size:16px;
            }

            .hero{
                text-align:center;
                padding:80px 20px;
                background:linear-gradient(135deg,#2563eb,#1d4ed8);
                color:white;
            }

            .hero h1{
                font-size:48px;
                margin-bottom:15px;
            }

            .hero p{
                font-size:20px;
                margin-bottom:25px;
            }

            .hero button{
                padding:12px 25px;
                border:none;
                border-radius:25px;
                background:white;
                color:#2563eb;
                font-size:16px;
                cursor:pointer;
                font-weight:bold;
            }

            .section-title{
                text-align:center;
                margin:50px 0 30px;
                font-size:32px;
            }

            .products{
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:25px;
                padding:20px;
            }

            .card{
                width:320px;
                background:white;
                border-radius:15px;
                overflow:hidden;
                box-shadow:0 4px 15px rgba(0,0,0,0.1);
                transition:0.3s;
            }

            .card:hover{
                transform:translateY(-8px);
            }

            .card img{
                width:100%;
                height:220px;
                object-fit:cover;
            }

            .card-content{
                padding:20px;
                text-align:center;
            }

            .card-content h3{
                margin-bottom:10px;
            }

            .price{
                color:green;
                font-size:24px;
                font-weight:bold;
                margin:15px 0;
            }

            .btn{
                display:inline-block;
                text-decoration:none;
                background:#2563eb;
                color:white;
                padding:10px 20px;
                border-radius:25px;
            }

            .features{
                display:flex;
                justify-content:center;
                flex-wrap:wrap;
                gap:30px;
                padding:50px 20px;
            }

            .feature-box{
                background:white;
                padding:25px;
                width:250px;
                text-align:center;
                border-radius:12px;
                box-shadow:0 4px 10px rgba(0,0,0,0.1);
            }

            .reviews{
                padding:50px 20px;
                text-align:center;
            }

            .review-card{
                background:white;
                max-width:700px;
                margin:20px auto;
                padding:25px;
                border-radius:12px;
                box-shadow:0 4px 10px rgba(0,0,0,0.1);
            }

            footer{
                background:#0f172a;
                color:white;
                text-align:center;
                padding:25px;
                margin-top:40px;
            }
        </style>
    </head>

    <body>

        <header>
            <div class="logo">🚗 Toy Car Store India</div>
            <nav>
                <a href="#">Home</a>
                <a href="#">Products</a>
                <a href="#">Offers</a>
                <a href="#">Contact</a>
            </nav>
        </header>

        <section class="hero">
            <h1>India's Favourite Toy Car Store</h1>
            <p>Premium Toy Cars for Kids and Collectors at Affordable Prices</p>
            <button>Shop Now</button>
        </section>

        <h2 class="section-title">Featured Toy Cars</h2>

        <section class="products">

            <div class="card">
                <img src="https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800" alt="Sports Car">
                <div class="card-content">
                    <h3>Sports Racing Car</h3>
                    <p>High-speed racing toy with premium finish.</p>
                    <div class="price">₹499</div>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=800" alt="SUV">
                <div class="card-content">
                    <h3>Mini SUV Toy Car</h3>
                    <p>Strong build quality and realistic design.</p>
                    <div class="price">₹699</div>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=800" alt="Luxury Car">
                <div class="card-content">
                    <h3>Luxury Model Car</h3>
                    <p>Collector's edition with detailed finishing.</p>
                    <div class="price">₹999</div>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

        </section>

        <h2 class="section-title">Why Choose Us?</h2>

        <section class="features">
            <div class="feature-box">
                <h3>🚚 Fast Delivery</h3>
                <p>Delivery available across India.</p>
            </div>

            <div class="feature-box">
                <h3>💳 Secure Payment</h3>
                <p>Safe and secure online transactions.</p>
            </div>

            <div class="feature-box">
                <h3>⭐ Premium Quality</h3>
                <p>High-quality toy cars at great prices.</p>
            </div>
        </section>

        <section class="reviews">
            <h2>Customer Reviews</h2>

            <div class="review-card">
                <p>"Excellent quality toy cars. My son absolutely loves them!"</p>
                <strong>- Rahul Sharma, Delhi</strong>
            </div>

            <div class="review-card">
                <p>"Fast delivery and amazing collection. Highly recommended."</p>
                <strong>- Priya Verma, Mumbai</strong>
            </div>
        </section>

        <footer>
            <p>© 2026 Toy Car Store India</p>
            <p>Powered by AWS Lambda & API Gateway</p>
            <p>📞 +91 98765 43210 | ✉ support@toycarstore.in</p>
        </footer>

    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html_content
    }
