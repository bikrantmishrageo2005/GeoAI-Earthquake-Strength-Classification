import folium
from IPython.display import display

# Create world map
world_map = folium.Map(location=[0,0], zoom_start=2)

# Add earthquake points
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=3,
        color="red" if row["strength_class"] == 1 else "blue",
        fill=True,
        fill_opacity=0.6
    ).add_to(world_map)

# Display map in Colab
display(world_map)

# Save map for website
world_map.save("earthquake_global_map.html")
