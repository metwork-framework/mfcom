{% extends "layer.md" %}

{% block overview %}

This is the `root` layer of the MFCOM module.

This layer mainly includes core libraries and utilities.

{% endblock %}

{% block utilities %}

{{ utility("config.py") }}

{% endblock %}
