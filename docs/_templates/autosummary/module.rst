{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}

{% block classes %}
{%- if classes %}
.. rubric:: Classes

.. autosummary::
   :toctree:
   :nosignatures:
{% for item in classes %}
   {{ item }}
{%- endfor %}
{% endif %}
{%- endblock %}

{% block functions %}
{%- if functions %}
.. rubric:: Functions

.. autosummary::
   :toctree:
   :nosignatures:
{% for item in functions %}
   {{ item }}
{%- endfor %}
{% endif %}
{%- endblock %}

{% block modules %}
{%- if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :recursive:
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{%- endblock %}
