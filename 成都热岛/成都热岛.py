import folium
import webbrowser

#104.05175,30.63683
map = folium.Map(location = [30.63683,104.05175],zoom_start=True)# 绘制地图，确定聚焦点([纬度，经度]，方法倍速)

folium.Marker([30.63683,104.05175],popup='<b>成都热岛</b>').add_to(map)  # 定一个点，放到地图map上
folium.Marker([30.63683,104.05175],popup='<b>成都热岛</b>',icon=folium.Icon(color='red')).add_to(map)# 把浮标变成红色
folium.Marker([30.63683,104.05175], #
              popup='<b>成都热岛</b>',
              icon=folium.Icon(color='orange',icon='info-sign')).add_to(map)# 浮标改图样
#标记一个空心圆
folium.Circle(location=[30.7000,104.70000],radius=100,color = 'crismon',popup='popup',fill=False).add_to(map)

map.save('f1.html')
webbrowser.open('f1.html')
