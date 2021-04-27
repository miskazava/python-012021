<html>
<head>
    <title>Vítejte na webu Czechitas</title>
    <style>
        h2 {
            color: blue;
        }
    </style>
</head>
<body>

{% block content %}

{% endblock %}

</body>
</html>

{% extends "base.html" %}
{% block content %}
<h2>Seznam kurzů</h2>
<p>Zde vidíte aktuální nabídku kurzů</p>
<ul>
    {% for kurz in object_list %}
    <li>{{ kurz.nazev }}, cena je {{ kurz.cena }} Kč, kurz se koná {{ kurz.zacatek }}</li>
    {% endfor %}
</ul>
{% endblock %}
