import base64
import streamlit as st

@st.cache_data
def get_arch_diagram(graph):
  graphbytes = graph.encode("ascii")
  base64_bytes = base64.b64encode(graphbytes)
  base64_string = base64_bytes.decode("ascii")
  return "https://mermaid.ink/img/" + base64_string