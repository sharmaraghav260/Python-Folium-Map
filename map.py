import folium
import os

# Create a map object
m = folium.Map(location=[30.307182, -97.755996], zoom_start=12)

# Global tooltip
tooltip = 'Click for more Info'
l1 = [30.348182, -97.775996]
l2 = [30.288182, -97.735996]
l3 = [30.388182, -97.715996]
l4 = [30.409182, -97.795996]
l5 = [30.363045, -97.793360]

# Create custom marker icon
logoIcon = folium.features.CustomIcon('indeed.jpeg', icon_size=(25,25))

# Create markers
folium.Marker(l1, 
                popup='<strong>Location One</strong>',
                tooltip=tooltip).add_to(m)

folium.Marker(l2, 
                popup='<strong>UT Students Dreaming</strong>',
                tooltip=tooltip,
                icon=folium.Icon(icon='cloud')).add_to(m)

folium.Marker(l3, 
                popup='<strong>Location Three</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='purple')).add_to(m)

folium.Marker(l4, 
                popup='<strong>Location Four</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m)

folium.Marker(l5, 
                popup='<strong>Indeed Austin Tech Campus</strong>',
                tooltip=tooltip,
                icon=logoIcon).add_to(m)

# Rectangle Marker
DT_bounds = [[30.274182, -97.735996], [30.269182, -97.755996]]
folium.Rectangle(
    DT_bounds,
    color= "#ff7800", 
    weight= 1,
    fill=True,
    fill_color='#ff7800'
    ).add_to(m)

# Geojson overlay
overlay = os.path.join('data', 'overlay.json')
folium.GeoJson(overlay, 
    name='UT Austin',
    ).add_to(m)

# Generate map
m.save("map.html")