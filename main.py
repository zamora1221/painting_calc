import streamlit as st

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio("Select a Measure", ["Exterior Measure", "Interior Measure"])

if menu == "Exterior Measure":
    st.title("Exterior Measure Calculator")

    # Project Specifics Section
    st.header("Project Specifics")
    st.subheader("Siding")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        siding_type = st.selectbox("Type", ["Cedar_Stain", "Brick", "Vinyl", "Stucco"], key="siding_type")
        brick_divider = st.number_input("Brick Divider (sq ft)", min_value=0, value=150, key="brick_divider")
    with col2:
        stucco_divider = st.number_input("Stucco Divider (sq ft)", min_value=0, value=150, key="stucco_divider")
        stucco_trim = st.number_input("Stucco Trim Only (sq ft)", min_value=0, value=150, key="stucco_trim")
    with col3:
        body2_divider = st.number_input("Body 2 Divider (sq ft)", min_value=0, value=200, key="body2_divider")
        substrate = st.selectbox("Siding Substrate", ["Wood", "Vinyl", "Fiber Cement", "Other"], key="substrate")

    st.subheader("Soffit")
    col4, col5 = st.columns([1, 1])
    with col4:
        soffit_size = st.number_input("Soffit Size (inches)", min_value=0, value=12, key="soffit_size")
        soffit_color = st.text_input("Soffit Color", "Body", key="soffit_color")
    with col5:
        rafter_height = st.number_input("Rafter Height (ft)", min_value=0, value=12, key="rafter_height")
        rafters_accented = st.selectbox("Rafters Accented", ["Yes", "No"], key="rafters_accented")

    st.subheader("Other")
    col6, col7 = st.columns([1, 1])
    with col6:
        lead_positive = st.selectbox("Lead Positive", ["Yes", "No"], key="lead_positive")
        vinyl_positive = st.checkbox("Vinyl Positive?", key="vinyl_positive")
    with col7:
        needs_pressure_wash = st.checkbox("Needs Pressure Wash?", key="needs_pressure_wash")

    st.subheader("Post Job - Salesforce (12 Hour Push to SF)")
    col8, col9 = st.columns([1, 1])
    with col8:
        booked_on_spot = st.checkbox("Booked on Spot", key="booked_on_spot")
        dnp_quote = st.checkbox("DNP Quote to Client", key="dnp_quote")
        completion_timeline = st.text_input("Completion Timeline", "Within 30 Days", key="completion_timeline")
        ideal_project_month = st.selectbox("Ideal Project Month", ["January", "February", "March", "Other"], key="ideal_project_month")
    with col9:
        hoa_approval = st.selectbox("Is HOA Approval Needed?", ["Yes", "No"], key="hoa_approval")
        estimated_days = st.number_input("Estimated Project Days", min_value=1, value=5, key="estimated_days")
        paint_type = st.selectbox("Paint Product Type(s)", ["Emerald", "Cashmere", "Duration", "Other"], key="paint_type")
        warranty_selected = st.selectbox("Warranty Selected", ["Yes", "No"], key="warranty_selected")

    # Notes Section
    st.subheader("Notes")
    estimate_notes = st.text_area("Estimate Notes", "", key="estimate_notes")
    callback_notes = st.text_area("Call Back Notes", "", key="callback_notes")
    production_notes = st.text_area("Production Notes for PM", "", key="production_notes")
    scheduling_notes = st.text_area("Scheduling Notes for CAM", "", key="scheduling_notes")
    loss_reason = st.text_input("Loss Reason", "", key="loss_reason")

    # Color Placement Measurements
    st.header("Color Placement Measurements")
    col10, col11, col12 = st.columns([1, 1, 1])
    with col10:
        fascia_story = st.selectbox("Fascia Story", ["< 20", "20+"], key="fascia_story")
        trim_length = st.number_input("Trim Length (ft)", min_value=0, value=0, key="trim_length")
    with col11:
        open_soffit_length = st.number_input("Open Soffit Length (ft)", min_value=0, value=0, key="open_soffit_length")
        accented_frieze_length = st.number_input("Accented Frieze Length (ft)", min_value=0, value=0, key="accented_frieze_length")
    with col12:
        railing_length = st.number_input("Railing Length (ft)", min_value=0, value=0, key="railing_length")
        railing_prep = st.selectbox("Railing Prep", ["None", "Light", "Heavy"], key="railing_prep")

    # Shed, Deck, and Fence
    st.header("Shed, Deck, and Fence")
    col13, col14, col15 = st.columns([1, 1, 1])
    with col13:
        deck_len = st.number_input("Deck Length (ft)", min_value=0, value=0, key="deck_len")
        deck_wid = st.number_input("Deck Width (ft)", min_value=0, value=0, key="deck_wid")
    with col14:
        fence_len = st.number_input("Fence Length (ft)", min_value=0, value=0, key="fence_len")
        pergola_len = st.number_input("Pergola Length (ft)", min_value=0, value=0, key="pergola_len")

    # House Quote Section
    st.header("House Quote")
    col16, col17, col18 = st.columns([1, 1, 1])
    with col16:
        sq_ft_body = st.number_input("Body (sq ft)", min_value=0, value=0, key="sq_ft_body")
        gallons_body = st.number_input("Gallons - Body", min_value=0.0, value=0.0, key="gallons_body")

    # Home Margin Calculator Section
    st.header("Home Margin Calculator")
    st.subheader("Warranty")
    warranty_types = ["10 YR Emerald", "11 YR Rain Refresh", "12 YR Aura", "Trim Only", "Stain (4 YR)", "Duration (8 YR)"]
    for warranty in warranty_types:
        st.number_input(f"{warranty} Price", min_value=0.0, value=0.0, key=f"price_{warranty}")

    # Negotiating Calculator Section
    st.header("Negotiating Calculator")
    st.selectbox("Product Negotiating", warranty_types, key="product_negotiating")
    st.number_input("Est. Payment After Discount ($)", min_value=0.0, value=0.0, key="est_payment")
    st.number_input("Additional Discount ($)", min_value=0.0, value=0.0, key="additional_discount")
    st.number_input("Total Discount (%)", min_value=0, max_value=100, value=0, key="total_discount")

    # Self Evaluation
    st.header("Self Evaluation")
    st.slider("Initial Walkthrough Score", min_value=0, max_value=10, value=0, key="walkthrough_score")
    st.text_area("What did you do well?", key="self_eval_well")
    st.text_area("What could you do next time?", key="self_eval_next")

    # Submit an Issue
    st.header("Have a Question? / Submit an Issue")
    st.text_area("Issue", key="issue")
    st.text_area("Question", key="question")
