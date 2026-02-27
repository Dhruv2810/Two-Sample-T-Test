import streamlit as st
import numpy as np
from scipy import stats

# Function
def one_sample_t_test(data, pop_mean, hypothesis):
    t_stat, p_val = stats.ttest_1samp(data, pop_mean, alternative=hypothesis)
    return t_stat, p_val


# Streamlit UI
st.title("One Sample T-Test App")

st.write("Enter sample data separated by commas:")

data_input = st.text_input("Sample Data", "102, 98, 101, 105, 97, 99, 103")

pop_mean = st.number_input("Population Mean (H0)", value=108.0)

hypothesis = st.selectbox(
    "Select Alternative Hypothesis",
    options=["two-sided", "less", "greater"]
)

if st.button("Run T-Test"):
    try:
        data = np.array([float(x.strip()) for x in data_input.split(",")])
        t_stat, p_val = one_sample_t_test(data, pop_mean, hypothesis)

        st.subheader("Results")
        st.write(f"T-statistic: {t_stat:.4f}")
        st.write(f"P-value: {p_val:.4f}")

        if p_val < 0.05:
            st.success("Reject the null hypothesis (significant result).")
        else:
            st.warning("Fail to reject the null hypothesis.")

    except:
        st.error("Please enter valid numeric data separated by commas.")