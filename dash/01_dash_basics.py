# Dash basics

# Dash Apps are composed of two parts:

# 1) The first part is the layout of the app and describes what the dashboard
# application looks like. Ex: where the visualization goes in the dashboard.

# 2) The second part describes the interactivity of the application. Ex: how sliders
# or buttons change the visualization.

# There are two distinct dash libraries:
    
# 1) dash_html_components
# 2) dash_core_components - offers higher-level, interactive components, that
# are generated through Java Script, CSS, and HTML through React.js library.

# Dash components (html or core), are described entirely throguh keyword attributes.
# Dash is declarative: you will primarily describe applications through these attributes.

######
## getting help with Dash
######

# import libraries
from dash import html

# use help()
print(help(html.Div)) # the help function wil print out module help
