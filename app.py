import math
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")
st.title("🔍 Ultraschall Prüfung – interaktive Demo")

# Eingaberegler
col1, col2 = st.columns(2)
with col1:
    depth = st.slider("Wanddicke (mm)", 10, 100, 20)
    angle = st.slider("Winkel γ zur Senkrechten (°)", 30, 70, 45)
with col2:
    width = st.slider("Bauteilbreite (mm)", 100, 600, 300)
    probe_x = st.slider("Prüfkopfposition X (mm)", 0, width, width // 3)

show_reflection = st.checkbox("Reflexion anzeigen", value=True)

# Berechnungen
mid = width / 2
beta = math.radians(60 / 2)
offset = depth * math.tan(beta)
angle_rad = math.radians(angle)

x0, y0 = probe_x, 0
x1 = x0 + depth * math.tan(angle_rad); y1 = depth
x2 = x1 + depth * math.tan(angle_rad); y2 = 0
x3 = x2 + 0.25 * depth * math.tan(angle_rad); y3 = 0.25 * depth
x4 = x3 + 0.25 * depth * math.tan(angle_rad); y4 = 0.5 * depth

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([0,0,width,width,0],[0,depth,depth,0,0],'gray','--')
ax.plot([mid-offset,mid],[0,depth],'black',2)
ax.plot([mid+offset,mid],[0,depth],'black',2)
ax.add_patch(plt.Rectangle((x0-5,-6),10,6,color='blue'))
ax.plot([x0,x1],[y0,y1],'r',2)
ax.plot([x1,x2],[y1,y2],'r--',2)
if show_reflection:
    ax.plot([x2,x3],[y2,y3],'r--',2)
    ax.plot([x3,x4],[y3,y4],'r--',2)
ax.axvline(mid,'gray','--',1)

# Maßlinie
arrow_y = -10
left, right = min(x0,mid), max(x0,mid)
ax.annotate('',(mid,arrow_y),(left,arrow_y),arrowprops=dict(arrowstyle='<->'))
ax.annotate('',(mid,arrow_y),(right,arrow_y),arrowprops=dict(arrowstyle='<->'))
ax.text((mid+left)/2,arrow_y-3,f"{abs(mid-left):.1f} mm",ha='center')
ax.text((mid+right)/2,arrow_y-3,f"{abs(mid-right):.1f} mm",ha='center')

ax.scatter([x0],[y0],color='red')
ax.set_xlim(0,width); ax.set_ylim(depth+40,-15); ax.set_aspect('equal')
st.pyplot(fig)
