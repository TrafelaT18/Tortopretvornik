<html>
    <head>
        <title>Dodaj_kolicino_sestavine</title>
    </head>
    <body>
    <center>
    <h2> VNOS KOLIČINE</h2>
        <form action="/dodaj_kolicino/dodaj" method="POST">
            kolicina: <input type="number" name="kolicina"> <br>
            sestavina: <input type="text" name="sestavina"> <br>
            <p>Izberite tip mere:</p>
  <input type="radio" id="tip1" name="tip" value="g" checked>
  <label for="tip1">gram</label><br>
  <input type="radio" id="tip2" name="tip" value="l">
  <label for="tip2">liter</label><br>  
  <input type="radio" id="tip3" name="tip" value="ml">
  <label for="tip3">mililiter</label><br>
  <input type="radio" id="tip4" name="tip" value="zlicka">
  <label for="tip4">zlicka</label><br>
  <input type="radio" id="tip5" name="tip" value="scepec">
  <label for="tip5">scepec</label><br>  
  <input type="radio" id="tip6" name="tip" value=" ">
  <label for="tip6">kos</label><br><br>
  <input type="submit" value="dodaj">
        </form>
    </center>
    </body>
</html>