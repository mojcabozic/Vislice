<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
</head>
<body>

  <h1>Vislice</h1>
  <h2>Igraš igro:</h2>
  <h3>Si v stanju: {{ stanje }}</h3>

  <h3>Pravilno si uganil:</h3>
  <h4>{{ igra.pravilni_del_gesla() }}</h4>

  <h3>Nepravilne črke:</h3>
  <h4>{{ igra.nepravilne_crke() }}</h4>

  <h3>Stopnja obešenosti</h3>
  <h4>{{ igra.stevilo_napak() }}</h4>

  <img src="img/{{ igra.stevilo_napak() }}.jpg" alt="Stopnja_obešenosti" >


  <form method="POST">
    <label> Vnesi črko:
      <input type="text" name="crka">
    </label>
    <input type="submit">
  </form>

  %if stanje == "W":
    <h3>Bravo, zmagal si!</h3>
    <form>
      

  %elif stanje == "L":
    <h3>Ojoj, izgubil si...</h3>
    <h3>Tvoje geslo je bilo: {{ igra.geslo }}</h3>
    

  %else:
    <form method="POST">
      <label> Vnesi črko:
        <input type="text" name="crka">
      </label>
      <input type="submit">
    </form>
    


</body>

</html>