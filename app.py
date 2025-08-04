import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Smart Sprinkler System",
    page_icon="🌱",
    layout="wide"
)

# Main title and description
st.title("🌱 Smart Sprinkler System")
st.markdown("### AI-Powered Irrigation Management System")
st.markdown("Enter sensor values (0 to 1 scale) to get intelligent sprinkler recommendations for your farm parcels.")

# Sidebar for additional information
st.sidebar.header("System Information")
st.sidebar.info("""
**Smart Irrigation Features:**
- 20 Multi-sensor monitoring
- AI-based decision making
- Water conservation
- Real-time predictions
- Multi-parcel management
""")

# Sensor descriptions
sensor_descriptions = [
    "Soil Moisture Level", "Air Temperature", "Air Humidity", "Light Intensity",
    "Soil pH Level", "Water Temperature", "Wind Speed", "Atmospheric Pressure",
    "Leaf Wetness", "Solar Radiation", "Soil Temperature", "Rainfall Amount",
    "Evapotranspiration", "Soil Salinity", "Plant Growth Stage", "Water Quality",
    "Nutrient Level", "Root Zone Moisture", "Canopy Temperature", "Irrigation History"
]

# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔧 Sensor Input Panel")
    
    # Collect sensor inputs with descriptions
    sensor_values = []
    
    # Create 4 columns for sensors
    sensor_cols = st.columns(4)
    
    for i in range(20):
        col_idx = i % 4
        with sensor_cols[col_idx]:
            val = st.slider(
                f"**{sensor_descriptions[i]}**", 
                min_value=0.0, 
                max_value=1.0, 
                value=0.5, 
                step=0.01,
                key=f"sensor_{i}"
            )
            sensor_values.append(val)

with col2:
    st.subheader("📊 Sensor Statistics")
    
    if sensor_values:
        avg_value = np.mean(sensor_values)
        max_value = np.max(sensor_values)
        min_value = np.min(sensor_values)
        
        st.metric("Average Value", f"{avg_value:.2f}")
        st.metric("Highest Reading", f"{max_value:.2f}")
        st.metric("Lowest Reading", f"{min_value:.2f}")
        
        # Create a simple chart
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(range(len(sensor_values)), sensor_values, color='lightblue')
        ax.set_xlabel('Sensor Number')
        ax.set_ylabel('Sensor Value')
        ax.set_title('Current Sensor Readings')
        plt.xticks(range(0, 20, 2))
        st.pyplot(fig)

# Prediction section
st.subheader("🚿 Sprinkler Control System")

# Predict button
if st.button("🔍 Analyze & Predict Sprinkler Status", type="primary"):
    st.markdown("### 📋 Irrigation Recommendations:")
    
    # Create prediction results
    results = []
    total_on = 0
    
    for i, sensor_val in enumerate(sensor_values):
        # Smart logic based on sensor type and value
        if i in [0, 11, 17]:  # Moisture-related sensors
            threshold = 0.3  # Lower threshold for moisture sensors
        elif i in [1, 6, 7]:  # Temperature/weather sensors
            threshold = 0.7  # Higher threshold for weather sensors
        else:
            threshold = 0.5  # Default threshold
            
        # Determine sprinkler status
        if sensor_val < threshold:
            status = "ON"
            status_emoji = "💧"
            total_on += 1
        else:
            status = "OFF"
            status_emoji = "⭕"
            
        results.append({
            "Parcel": f"Parcel {i+1}",
            "Sensor": sensor_descriptions[i],
            "Value": f"{sensor_val:.2f}",
            "Status": status,
            "Emoji": status_emoji
        })
    
    # Display results in a nice format
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🟢 Sprinklers ON", total_on)
    with col2:
        st.metric("🔴 Sprinklers OFF", 20 - total_on)
    with col3:
        water_saved = (20 - total_on) * 100 / 20
        st.metric("💧 Water Saved", f"{water_saved:.1f}%")
    
    # Detailed results table
    st.markdown("#### Detailed Parcel Status:")
    
    # Create columns for results
    result_cols = st.columns(4)
    
    for i, result in enumerate(results):
        col_idx = i % 4
        with result_cols[col_idx]:
            status_color = "🟢" if result["Status"] == "ON" else "🔴"
            st.markdown(f"""
            **{result['Parcel']}** {status_color}
            
            *{result['Sensor']}*
            
            Value: {result['Value']}
            
            **{result['Status']}** {result['Emoji']}
            """)

# Additional features
st.markdown("---")
st.subheader("📈 System Analytics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎯 Optimization Tips:")
    st.markdown("""
    - Monitor soil moisture sensors regularly
    - Adjust irrigation based on weather conditions
    - Consider plant growth stages for watering
    - Track water usage for conservation
    """)

with col2:
    st.markdown("#### 🔧 System Features:")
    st.markdown("""
    - 20 intelligent sensors monitoring
    - Real-time decision making
    - Water conservation algorithms
    - Multi-parcel management
    - Weather-adaptive irrigation
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<p><strong>Smart Sprinkler System v1.0</strong> | Developed with ❤️ for Sustainable Agriculture</p>
<p>AICTE-Shell-Edunet Internship Project | Green Skills using AI</p>
</div>
""", unsafe_allow_html=True)