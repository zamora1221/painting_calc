import streamlit as st
import pandas as pd
import os

# Constants
DATA_FILE = "projects_data.csv"

def calculate_paint_area(length, width, height, doors=0, windows=0):
    # Calculate wall area
    total_wall_area = 2 * height * (length + width)
    # Subtract area for doors and windows
    door_area = doors * 21  # assuming each door/window is 21 sq ft
    net_paint_area = total_wall_area - door_area
    return net_paint_area

def calculate_paint_required(net_area, coverage_per_gallon=350):
    return net_area / coverage_per_gallon

def calculate_cost(paint_gallons, labor_hours, paint_cost_per_gallon=25, labor_cost_per_hour=20):
    total_paint_cost = paint_gallons * paint_cost_per_gallon
    total_labor_cost = labor_hours * labor_cost_per_hour
    total_cost = total_paint_cost + total_labor_cost
    return total_paint_cost, total_labor_cost, total_cost

def project_input_form():
    st.header("Enter Project Details")

    project_name = st.text_input("Project Name", "Project A")
    length = st.number_input("Length of Room (ft)", min_value=0.0, value=20.0)
    width = st.number_input("Width of Room (ft)", min_value=0.0, value=15.0)
    height = st.number_input("Height of Room (ft)", min_value=0.0, value=10.0)
    doors = st.number_input("Number of Doors", min_value=0, value=1)
    windows = st.number_input("Number of Windows", min_value=0, value=2)
    labor_hours = st.number_input("Estimated Labor Hours", min_value=0.0, value=40.0)
    paint_type = st.selectbox("Type of Paint", ["Standard", "Premium"])

    if paint_type == "Standard":
        paint_cost_per_gallon = 25
    else:
        paint_cost_per_gallon = 40

    return {
        "project_name": project_name,
        "length": length,
        "width": width,
        "height": height,
        "doors": doors,
        "windows": windows,
        "labor_hours": labor_hours,
        "paint_cost_per_gallon": paint_cost_per_gallon
    }

def initialize_session_state():
    if 'projects' not in st.session_state:
        if os.path.exists(DATA_FILE):
            st.session_state['projects'] = pd.read_csv(DATA_FILE)
        else:
            st.session_state['projects'] = pd.DataFrame(columns=[
                "Project Name", "Length", "Width", "Height", "Doors",
                "Windows", "Labor Hours", "Paint Gallons", "Paint Cost",
                "Labor Cost", "Total Cost"
            ])

def add_project(project_data, calculations):
    new_entry = {
        "Project Name": project_data['project_name'],
        "Length": project_data['length'],
        "Width": project_data['width'],
        "Height": project_data['height'],
        "Doors": project_data['doors'],
        "Windows": project_data['windows'],
        "Labor Hours": project_data['labor_hours'],
        "Paint Gallons": round(calculations['paint_gallons'], 2),
        "Paint Cost": round(calculations['paint_cost'], 2),
        "Labor Cost": round(calculations['labor_cost'], 2),
        "Total Cost": round(calculations['total_cost'], 2)
    }
    # Convert new_entry to a DataFrame
    new_entry_df = pd.DataFrame([new_entry])
    # Concatenate the new entry to the existing projects DataFrame
    st.session_state['projects'] = pd.concat([st.session_state['projects'], new_entry_df], ignore_index=True)
    # Save to CSV for persistence
    st.session_state['projects'].to_csv(DATA_FILE, index=False)

def display_calculations(calculations):
    st.subheader("Calculation Results")
    st.write(f"**Paint Area:** {calculations['net_area']} sq ft")
    st.write(f"**Paint Required:** {calculations['paint_gallons']:.2f} gallons")
    st.write(f"**Paint Cost:** ${calculations['paint_cost']:.2f}")
    st.write(f"**Labor Cost:** ${calculations['labor_cost']:.2f}")
    st.write(f"**Total Cost:** ${calculations['total_cost']:.2f}")

def main():
    st.title("Painting Company Calculator")

    initialize_session_state()

    # Sidebar for navigation
    st.sidebar.header("Menu")
    menu = ["Add New Project", "View All Projects"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Add New Project":
        project_data = project_input_form()

        if st.button("Calculate and Add Project"):
            # Perform calculations
            net_area = calculate_paint_area(
                project_data['length'],
                project_data['width'],
                project_data['height'],
                doors=project_data['doors'],
                windows=project_data['windows']
            )
            paint_gallons = calculate_paint_required(net_area)
            paint_cost, labor_cost, total_cost = calculate_cost(
                paint_gallons,
                project_data['labor_hours'],
                paint_cost_per_gallon=project_data['paint_cost_per_gallon']
            )

            calculations = {
                "net_area": net_area,
                "paint_gallons": paint_gallons,
                "paint_cost": paint_cost,
                "labor_cost": labor_cost,
                "total_cost": total_cost
            }

            # Display results
            display_calculations(calculations)

            # Add to session state and save
            add_project(project_data, calculations)

            st.success("Project added successfully!")

    elif choice == "View All Projects":
        st.header("All Projects")
        st.dataframe(st.session_state['projects'])

        if st.session_state['projects'].empty:
            st.info("No projects added yet.")
        else:
            if st.button("Download Projects as CSV"):
                csv = st.session_state['projects'].to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='projects.csv',
                    mime='text/csv',
                )

if __name__ == "__main__":
    main()
