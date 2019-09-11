{% extends "layer.md" %}

{% block overview %}

The `layer1_python2` layer includes Python2 MFCOM packages and utilities.

{% endblock %}

{% block utilities %}

{{ utility("layer_wrapper --layers=python3@mfcom -- get_ip_for_hostname", displayed_name="get_ip_for_hostname") }}
{{ utility("layer_wrapper --layers=python3@mfcom -- get_simple_hostname", displayed_name="get_simple_hostname") }}
{{ utility("layer_wrapper --layers=python3@mfcom -- get_full_hostname", displayed_name="get_full_hostname") }}
{{ utility("layer_wrapper --layers=python3@mfcom -- get_real_ip", displayed_name="get_real_ip") }}
{{ utility("layer_wrapper --layers=python3@mfcom -- ping_tcp_port", displayed_name="ping_tcp_port") }}
{{ utility("layer_wrapper --layers=python3@mfcom -- recursive_kill.py", displayed_name="recursive_kill.py") }}

{% endblock %}
