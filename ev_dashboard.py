import pandas as pd
import streamlit as st
import altair as alt

# Dataset with prices decreased by 15%
data = [
    {"Brand": "Tesla", "Model": "Model Y Long Range", "Battery Range": 330, "Price": 36250.0, 
     "Level 3 Charge Time (10-80%)": 25, "Battery Warranty Miles": 120000, 
     "Cargo Space (cu ft)": 76.2, "0-60 mph time": 4.8},
    {"Brand": "Tesla", "Model": "Model Y Performance", "Battery Range": 303, "Price": 37800.0, 
     "Level 3 Charge Time (10-80%)": 25, "Battery Warranty Miles": 120000, 
     "Cargo Space (cu ft)": 76.2, "0-60 mph time": 3.5},
    {"Brand": "Hyundai", "Model": "Ioniq 5 SEL", "Battery Range": 266, "Price": 30750.0, 
     "Level 3 Charge Time (10-80%)": 18, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 59.3, "0-60 mph time": 5.2},
    {"Brand": "Hyundai", "Model": "Ioniq 5 Limited", "Battery Range": 303, "Price": 36300.0, 
     "Level 3 Charge Time (10-80%)": 18, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 59.3, "0-60 mph time": 5.0},
    {"Brand": "Ford", "Model": "Mustang Mach-E Select", "Battery Range": 230, "Price": 28200.0, 
     "Level 3 Charge Time (10-80%)": 38, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 59.7, "0-60 mph time": 5.8},
    {"Brand": "Ford", "Model": "Mustang Mach-E GT", "Battery Range": 270, "Price": 37000.0, 
     "Level 3 Charge Time (10-80%)": 38, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 59.7, "0-60 mph time": 3.8},
    {"Brand": "Kia", "Model": "EV6 Wind RWD", "Battery Range": 310, "Price": 28600.0, 
     "Level 3 Charge Time (10-80%)": 18, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 50.2, "0-60 mph time": 7.2},
    {"Brand": "Kia", "Model": "EV6 GT-Line AWD", "Battery Range": 282, "Price": 35700.0, 
     "Level 3 Charge Time (10-80%)": 18, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 50.2, "0-60 mph time": 4.6},
    {"Brand": "Rivian", "Model": "R1T Adventure", "Battery Range": 314, "Price": 57000.0, 
     "Level 3 Charge Time (10-80%)": 42, "Battery Warranty Miles": 175000, 
     "Cargo Space (cu ft)": 54.1, "0-60 mph time": 3.0},
    {"Brand": "Subaru", "Model": "Solterra Premium", "Battery Range": 222, "Price": 25500.0, 
     "Level 3 Charge Time (10-80%)": 45, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 56.2, "0-60 mph time": 7.4},
    {"Brand": "Subaru", "Model": "Solterra Limited", "Battery Range": 228, "Price": 27200.0, 
     "Level 3 Charge Time (10-80%)": 45, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 56.2, "0-60 mph time": 6.5},
    {"Brand": "Volvo", "Model": "C40 Recharge", "Battery Range": 226, "Price": 29000.0, 
     "Level 3 Charge Time (10-80%)": 37, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 49.0, "0-60 mph time": 4.7},
    {"Brand": "Volvo", "Model": "XC40 Recharge Twin", "Battery Range": 223, "Price": 32000.0, 
     "Level 3 Charge Time (10-80%)": 37, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 50.8, "0-60 mph time": 4.7},
    {"Brand": "Audi", "Model": "Q4 e-tron Premium", "Battery Range": 265, "Price": 35700.0, 
     "Level 3 Charge Time (10-80%)": 38, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 54.0, "0-60 mph time": 6.2},
    {"Brand": "Chevrolet", "Model": "Bolt EUV Premier", "Battery Range": 247, "Price": 21250.0, 
     "Level 3 Charge Time (10-80%)": 60, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 56.6, "0-60 mph time": 7.0},
    {"Brand": "BMW", "Model": "iX xDrive50", "Battery Range": 324, "Price": 58500.0, 
     "Level 3 Charge Time (10-80%)": 35, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 77.9, "0-60 mph time": 4.4},
    {"Brand": "Toyota", "Model": "bZ4X XLE", "Battery Range": 252, "Price": 33750.0, 
     "Level 3 Charge Time (10-80%)": 40, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 55.0, "0-60 mph time": 7.1},
    {"Brand": "Nissan", "Model": "Ariya Venture+", "Battery Range": 304, "Price": 31450.0, 
     "Level 3 Charge Time (10-80%)": 35, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 59.7, "0-60 mph time": 7.2},
    {"Brand": "Genesis", "Model": "GV60 Advanced", "Battery Range": 248, "Price": 38900.0, 
     "Level 3 Charge Time (10-80%)": 18, "Battery Warranty Miles": 100000, 
     "Cargo Space (cu ft)": 54.7, "0-60 mph time": 4.0}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit setup
st.set_page_config(page_title="Used 2023 EV SUV Dashboard", layout="wide")
st.title("USED 2023 EV SUV Dashboard")
st.markdown("Explore used 2023 electric SUVs and customize weights to find your optimal vehicle.")

# Sidebar: Adjust feature weights
st.sidebar.header("Adjust Feature Weights")
battery_weight = st.sidebar.slider("Battery Range Weight", 0.0, 1.0, 0.35, 0.05)
price_weight = st.sidebar.slider("Price Weight", 0.0, 1.0, 0.25, 0.05)
charge_time_weight = st.sidebar.slider("Level 3 Charge Time Weight", 0.0, 1.0, 0.20, 0.05)
warranty_weight = st.sidebar.slider("Warranty Weight", 0.0, 1.0, 0.10, 0.05)
cargo_weight = st.sidebar.slider("Cargo Space Weight", 0.0, 1.0, 0.05, 0.05)
performance_weight = st.sidebar.slider("0-60 mph Time Weight", 0.0, 1.0, 0.05, 0.05)

# Calculate total weight
total_weight = battery_weight + price_weight + charge_time_weight + warranty_weight + cargo_weight + performance_weight
remaining_weight = 1.0 - total_weight

# Display weight allocation status
if total_weight > 1.0:
    st.sidebar.error(f"Total weight exceeds 100%! (Over by {round((total_weight - 1.0) * 100, 2)}%)")
elif total_weight == 1.0:
    st.sidebar.success("Perfect! Total weight is exactly 100%.")
else:
    st.sidebar.warning(f"Total weight is under 100%. (Remaining: {round(remaining_weight * 100, 2)}%)")


# Normalize columns
def normalize_column(column, reverse=False):
    normalized = (column - column.min()) / (column.max() - column.min())
    return 1 - normalized if reverse else normalized

# Ensure all necessary columns exist before further calculations
required_columns = ["Battery Range", "Price", "Level 3 Charge Time (10-80%)",
                    "Battery Warranty Miles", "Cargo Space (cu ft)", "0-60 mph time"]

missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    st.error(f"The following columns are missing: {', '.join(missing_columns)}")
else:
    # Add scores for each feature
    df["Range Score"] = normalize_column(df["Battery Range"])
    df["Price Score"] = normalize_column(df["Price"], reverse=True)
    df["Charge Time Score"] = normalize_column(df["Level 3 Charge Time (10-80%)"], reverse=True)
    df["Warranty Score"] = normalize_column(df["Battery Warranty Miles"])
    df["Cargo Space Score"] = normalize_column(df["Cargo Space (cu ft)"])
    df["Performance Score"] = normalize_column(df["0-60 mph time"], reverse=True)

    # Calculate final score
    df["Final Score"] = (
        df["Range Score"] * battery_weight +
        df["Price Score"] * price_weight +
        df["Charge Time Score"] * charge_time_weight +
        df["Warranty Score"] * warranty_weight +
        df["Cargo Space Score"] * cargo_weight +
        df["Performance Score"] * performance_weight
    )

    # Feature comparison with Final Score as default
    st.header("Feature Comparison")
    feature_options = list(df.columns.drop(["Brand", "Model"]))
    default_index = feature_options.index("Final Score") if "Final Score" in feature_options else 0
    feature = st.selectbox("Select a feature to visualize", feature_options, index=default_index)

    # Create chart
    if feature == "Final Score":
        chart_data = df.sort_values(by="Final Score", ascending=False)
    else:
        chart_data = df.sort_values(by=feature, ascending=False)

    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X(feature, title=feature),
        y=alt.Y("Model", sort="-x", title="Model"),
        tooltip=["Model", feature]
    ).properties(
        width=800,
        height=500,
        title=f"{feature} Comparison"
    )
    st.altair_chart(chart, use_container_width=True)

    # Display sorted DataFrame
    st.header("Top EV SUVs (Sorted by Final Score)")
    st.dataframe(df.sort_values(by="Final Score", ascending=False))
