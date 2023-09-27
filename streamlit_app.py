import streamlit as st
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles should be
show_pages(
    [
        Page("streamlit_app.py", "Home"),
        Page("pages/discovery_chat.py", "Chat"),
        Page("pages/summary.py", "Summary"),
        Page("pages/poc.py", "Testing Plan"),
        Page("pages/feedback.py", "Feedback"),
    ]
)

st.title('Welcome to Architect.AI!')
st.divider()

st.header("Background")
st.write("Architect.AI is designed to help users find, evaluate, and select technologies for their data architecture.")
st.write("""The current process of buying software is time-consuming, costly, and filled with misaligned incentives.""") 
st.write("  1. Knowing what types of technology that you need for you use case requires years of expertise which can be costly and filled with bias.")
st.write("  2. If inexperienced people try to make these decisions, they have to wade through massive amounts of biased case studies, benchmarks, and online documentation.")
st.write("  3. If they are able to identify which vendors they should talk to, they then have to work with sales reps who are inexperienced and incentivized to oversell and misrepresent their products. ")
st.write("Architect.AI enables buyers to quickly and easily choose the right tools for their business.")
st.divider()

st.header("How To Use")
st.write("""1. Start on the Chat page where you will have a conversation with Archie, our AI Architect. He will ask you some questions about your use case and then provide 
         recommendations on which vendors you should evaluate. You should provide as much information as possible. Expeect this to take 10-15 minutes.""")
st.write("""2. Once your conversation with Archie is finished, you can head over to the Summary page. There, you will find additional information about the vendors that 
         Archie recommended including architecture diagrams, references, and customer reviews.""")
st.write("""3. Next, check out the Testing Plan. The plan will enable you to complete your evaluations quickly and free of influence from sales reps. 
         However, we do recommend communicating with the vendors directly at this point, as they will be able to help troubleshoot any technical issues that you run into during your evaluation.""")
st.write("""4. Finally, give us some feedback! We have built this platform to help buyers make decisions on their own. Any help that you can provide that allows us to reach
         that goal quickly is much appreciated.""")







