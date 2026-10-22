import streamlit as st
import time

def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(10) # 👈 This makes the function take 10s to run
    return a * b+1

a = 3
b = 210
res = expensive_computation(a, b)
st.write("Result:", res)

@st.cache_data()
def expensive_computation_3(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(5) # This makes the function take 2s to run
    return a * b

a = 2
b = st.slider("Pick a number", 0, 10) # 👈 Changed this

res = expensive_computation_3(a, b)
st.write("Result:", res)

# If the slider value does not change, the cached result is reused immediately.
# If the slider changes to a new value, the function runs again and takes 5 seconds.
# If we select a previously used value, the cached result is returned immediately.

st.title('Counter Example using Callbacks with args')
#Initialization
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count)
