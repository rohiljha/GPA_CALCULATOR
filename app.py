import streamlit as st

# Grade to point mapping
grade_scale = {
    "A+": 10, "A": 9, "B": 8, "C": 7,
    "D": 6, "E": 5, "F": 0
}

st.set_page_config(page_title="GPA Calculator", page_icon="🎓")

st.title("🎓 GPA Calculator")
st.write("Enter your courses, their credits, and grades to calculate GPA.")

# Input number of courses
num_courses = st.number_input("How many courses?", min_value=1, max_value=20, step=1)

# Store inputs
courses = []
total_credits = 0
total_weighted_score = 0

# Input table
st.subheader("📋 Course Details")
for i in range(num_courses):
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        course = st.text_input(f"Course {i+1} Name", key=f"course_{i}")
    with col2:
        credits = st.number_input(f"Credits", min_value=0.5, step=0.5, key=f"credits_{i}")
    with col3:
        grade = st.selectbox(
            "Grade",
            options=["", "A+", "A", "B", "C", "D", "E", "F"],
            key=f"grade_{i}"
        )

    if course and grade and credits:
        grade_point = grade_scale.get(grade, None)
        if grade_point is not None:
            total_credits += credits
            total_weighted_score += grade_point * credits
            courses.append((course, credits, grade))

# Calculate GPA
if st.button("Calculate GPA"):
    if total_credits == 0:
        st.error("🚫 No valid courses to calculate GPA.")
    else:
        gpa = total_weighted_score / total_credits
        st.success(f"🎯 Your GPA is: **{gpa:.2f}**")

        st.markdown("---")
        st.subheader("✅ GPA Calculation Summary")
        for course, credits, grade in courses:
            st.write(f"📘 **{course}** – Credits: {credits}, Grade: {grade}")
