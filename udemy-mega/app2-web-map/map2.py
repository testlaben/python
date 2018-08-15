import folium
import pandas

map = folium.Map(location=[39.828263, -98.579512], zoom_start=5,
                 tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi im a marker!",
                               icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("map2.html")
