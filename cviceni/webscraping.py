<html>
<head>
  <meta charset="UTF-8">
  <title>Ukazka</title>
</head>
<body>
  <h1>Nadpis prvni urovně</h1>
  <p>
    Text nějakeho odstavce, který obsahuje
    <i>zvýrazněný text</i> a také <b>
      důležitý text</b> a <u>podržený text</u>.
  </p>

  <h2>Nadpis druhé úrovně</h2>
  <div class="sekce1">
    <p>
      Druhý odstavec je v takzvaném divu, což je
      značka, která nemá sama o sobě žádný význam.
      Také zde máme
      <a href="http://www.czechitas.cz"> odkaz na
      stránky Czechitas</a>.
    </p>

    <ol type="a">
      <li>Prvni položka seznamu</li>
      <li>Druha položka seznamu</li>
      <li>Třeti položka seznamu</li>
    </ol>
  </div>
</body>
</html>

snihdf = pandas.DataFrame(snih, columns=['rok', 'hora', 'udoli'])
snihdf = snihdf.set_index('rok')
snihdf.to_html("tabulka.html")


