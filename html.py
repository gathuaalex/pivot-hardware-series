main_page="""<!DOCTYPE HTML><html>
                <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
                <style>
                    html {
                    font-family: Arial;
                    display: inline-block;
                    margin: 0px auto;
                    text-align: center;
                    }
                    h3 { font-size: 2.0rem; }
                    p { font-size: 2.0rem; }
                    .units { font-size: 1.2rem; }
                    .sht31-labels{
                    font-size: 1.5rem;
                    vertical-align:middle;
                    padding-bottom: 15px;
                    }
                </style>
                </head>
                <body>
                <h3>Pivot Hardware Series</h2>

                
                <p>
                    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
                    <span class="sht31-labels">Temperature</span> 
                    <span id="temperature"></span>
                    <sup class="units">&deg;C</sup>
                </p>
                <p>
                    <i class="fas fa-tint" style="color:#00add6;"></i> 
                    <span class="sht31-labels">Humidity</span>
                    <span id="humidity"></span>
                    <sup class="units">%</sup>
                </p>
                </body>
                <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
                <script>
                setInterval(function(){
                    $.ajax(
                    {
                        type:"GET",
                        url: "/temperature",
                        success: function( data ) 
                        {
                            $('#temperature').html(data);
                        }
                    })
                }, 5000 ) ;
                setInterval(function(){
                    $.ajax(
                    {
                        type:"GET",
                        url: "/humidity",
                        success: function( data ) 
                        {
                            $('#humidity').html(data);
                        }
                    })
                }, 5000 ) ;
                </script>
                </html>
"""