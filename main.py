import pandas as pd
import folium
from folium import plugins

# 读取CSV文件
df = pd.read_csv('stations_data2.csv')

# 根据线路名称分组
grouped_data = df.groupby('Line')

colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'yellow', 'brown', 'cyan', 'magenta', 'maroon', 'violet']
color_index = 0

# 创建地图对象
mymap = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12, tiles='http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Gray_OnlySymbol/MapServer/tile/{z}/{y}/{x}',
               attr='街道网图',)

# 遍历每个线路的数据
for name, group in grouped_data:

    # 绘制站点之间的连线
    line_coords = [(row['Latitude'], row['Longitude']) for index, row in group.iterrows()]
    folium.PolyLine(locations=line_coords, color=colors[color_index], weight=5, opacity=1).add_to(mymap)

    color_index += 1

# 遍历每个线路的数据
for name, group in grouped_data:

    # 在地图上绘制站点
    for index, row in group.iterrows():
        # 添加圆圈
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=4,  # 圆圈半径，单位为米
            color='black',  # 圆圈颜色
            fill=True,
            fill_color='black',
            fill_opacity=1,
        ).add_to(mymap)

# 在地图上显示
mymap.save('railway_network_map.html')


