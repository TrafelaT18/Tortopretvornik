<html>
    <head>
        <title>Izpis sestavin</title>
    </head>
    <body>
    <center>
    <h1>
        Izpis pretvorjenih sestavin
    </h1>
            % for item in seznam:
                <p style="font-weight: bold;">  {{item.sestavina}} </p> <p> original: {{item.kolicina}}{{item.mera}} <br /> pretvorjeno: {{item.pretvorjeno}}{{item.mera}}</p> <br /> <br />
            % end
    </center>
    </body>
</html>