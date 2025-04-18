from req_parser import extract_entities
from schema_generator import generate_schema
from pseudocode_generator import generate_pseudocode
import streamlit as st

def process_requirement(requirement):
    modules = extract_entities(requirement)
    schema = generate_schema(modules)
    pseudocode = generate_pseudocode(modules)

    return modules, schema, pseudocode


# Streamlit UI
st.set_page_config(page_title="ReqToSpec: AI Requirement Analyzer", layout="centered")
st.title("📋 ReqToSpec Tool")
st.subheader("Turn Business Requirements into Tech Blueprints 🧠➡️📐")

user_input = st.text_area("Enter a high-level business requirement:", height=200)

if st.button("Generate Insights 🚀"):
    if user_input:
        modules, schema, pseudocode = process_requirement(user_input)

        st.markdown("### ✅ Identified Modules")
        for mod in modules:
            st.success(mod)

        st.markdown("### 🗂 Suggested Schemas")
        for mod, tables in schema.items():
            st.markdown(f"**{mod}**")
            for table, fields in tables.items():
                st.json({table: fields})

        st.markdown("### 🧾 Generated Pseudocode")
        for mod, code in pseudocode.items():
            st.markdown(f"**{mod}**")
            st.code(code.strip(), language="python")
    else:
        st.warning("Please enter a requirement to analyze.")
