from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating a travel itinerary

travel_template = "I am travelling from {city_1} to {city_2}  generate me a {day} days travel itenary if i am travel through {mode} along with travel plan like how i can reach this {city_2} from {city_1} and places to visit"


travel_prompt = PromptTemplate(template = travel_template, input_variables = ['city_1', 'city_2', 'day', 'mode'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-thinking-exp-01-21")


# Create LLM chain using the prompt template and model
travel_chain = travel_prompt | gemini_model

import streamlit as st

# st.header("✈ Travel Itinerary Creator")
# st.subheader("🧳 Your Personal Travel Itinerary Generator")

st.markdown(
    """
    <h1 style="text-align: center;">✈ Travel Itinerary Creator</h1>
    <h3 style="text-align: center;">🧳 Your Personal Travel Itinerary Generator</h3>
    """,
    unsafe_allow_html=True
)

# Creating two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Travel Details")
    city_1 = st.text_input("From City")
    city_2 = st.text_input("To City")

    day = st.number_input("Number of days", min_value=1, max_value=10, value=1, step=1)

    mode = st.selectbox(
        "Traveling Via",
        ("Train", "Aeroplane", "Bus", "Road"),
        index=None,
        placeholder="Select travel medium",
    )

    create_button = st.button("Create")

# Display results in the second column with a scrollable container
# Display results in the second column with a scrollable container
with col2:
    st.subheader("Generated Itinerary")

    if create_button:
        # Simulating a long text output
        travel = travel_chain.invoke({"city_1": city_1, "city_2": city_2, "day": day, "mode": mode})
        itinerary_content = travel.content  # Store content for printing and downloading

        # Scrollable container with text
        st.markdown(
            f"""
            <div id="print-content" style="
                width: 175%;  
                height: 600px; 
                overflow-y: auto; 
                padding: 12px; 
                border: 1px solid #660600; 
                background-color: #c7c7c7;
                border-radius: 8px;
            ">
                {itinerary_content}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Print Button (JavaScript)
        st.markdown(
            """
            <button onclick="printDiv()" style="margin: 10px; padding: 8px 12px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                🖨 Print Itinerary
            </button>

            <script>
                function printDiv() {
                    var divContents = document.getElementById("print-content").innerHTML;
                    var a = window.open('', '', 'height=500, width=800');
                    a.document.write('<html>');
                    a.document.write('<body >');
                    a.document.write(divContents);
                    a.document.write('</body></html>');
                    a.document.close();
                    a.print();
                }
            </script>
            """,
            unsafe_allow_html=True
        )

        # Download Button
        itinerary_filename = "itinerary.txt"
        st.download_button(
            label="📥 Download Itinerary",
            data=itinerary_content,
            file_name=itinerary_filename,
            mime="text/plain",
        )
# Features in This Code
✅ Scrollable Output Box

height: 300px; overflow-y: auto; ensures the output is scrollable.
✅ Print Button

Uses JavaScript (printDiv()) to print only the itinerary content.
Clicking the "🖨 Print Itinerary" button opens the print dialog.
✅ Download Button

Creates a TXT file dynamically with the itinerary content.
Clicking "📥 Download Itinerary" saves the file locally.

    
    
