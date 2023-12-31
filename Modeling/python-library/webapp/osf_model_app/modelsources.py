# modelsources.py

from string import Template

HTML_TEMPLATE = Template("""
<h1>Hello ${place_name}!</h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")

HTML_HOME_TEMPLATE = Template("""
<html>
<head>
    <title>OSF Modeling WebAPP - First Derivative</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    <style>html, body {width: 100%;height: 100%;margin: 0 auto;  background: white; text-align: center; padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
</head>
<body>
    <h1> - </h1>
    <h1> --- </h1>
    <h1> ----- </h1>
    <h1> ----- OSF Model Solutions ----- </h1>
    <h1> ----- </h1>
    <h1> --- </h1>
    <h1> - </h1>
    <h2> Geo-Location Model Maps </h2>
    <h5>
      <ul>
       {% for file in files %}
         <li>
           <a href={{ (request.path + '/' if request.path != '/' else '') + file }}>
               {{ (request.path + '/' if request.path != '/' else '') + file }}
           </a>
         </li>
       {% endfor %}
      </ul>
    </h5>
    <h6>{{ utc_dt }}</h6>
</body>

</html>
                              """)