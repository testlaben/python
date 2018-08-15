import folium

map = folium.Map(location=[39.828263, -98.579512], zoom_start=5,
                 tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi im a marker!",
                            icon=folium.Icon(color='green')))

map.save("map1.html")
