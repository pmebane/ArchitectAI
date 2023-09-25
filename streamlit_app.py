import streamlit as st
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles should be
show_pages(
    [
        Page("streamlit_app.py", "Home"),
        Page("pages/discovery_chat.py", "Chat"),
        Page("pages/summary.py", "Summary"),
        #,Page("pages/poc.py", "Testing Plan"),
        Page("pages/feedback.py", "Feedback"),
    ]
)

st.title('Welcome to ArchitectAI!')
st.divider()

st.header("Background")
st.write("ArchitectAI is a platform that is designed to help users find, evaluate, and select technologies for their data architecture.")
st.write("""The current process of buying software is time-consuming, costly, and filled with misaligned incentives.""") 
st.write("  1. Knowing what types of technology that you need for you use case requires years of expertise which can be costly and filled with bias.")
st.write("  2. If inexperienced people try to make these decisions, they have to wade through massive amounts of case studies, benchmarks, and online documentation.")
st.write("  3. If they are able to identify which vendors they should talk to, they then have to deal with sales reps who have no knowledge of the user's business, are often not techincal enough to be helpful, and are paid to oversell contracts and push their software in places where it should not be used. ")
st.write("ArchitectAI was created to empower buyers to make these decisions themselves by providing unbiased guidance and direct references to useful documentation.")
st.divider()

st.header("How To Use")
st.write("""1. Start on the Chat page, where you will have a conversation with Archie, our AI Architect. He will ask you some questions about your use case, and then provide recommendations
         on which technologies you will need and which vendors you should evaluate for each technology. You should provide as much information as possible. Expeect this to take 
         10-15 minutes.""")
st.write("""2. Once your conversation with Archie is finished, you can head over to the Summary page. There, you will find additional information about the technologies that 
         Archie recommended including architecture diagrams, references, and customer reviews.""")
st.write("""3. Next, you can check out the Testing Plan. Using this while evaluating vendors for your architecture will enable you to complete the evaluations quickly and free
         of influence from sales reps. However, we do recommend communicating with the vendors directly at this point, as they will be able to help troubleshoot and technical
         issues that you run into during your evaluation.""")
st.write("""4. Finally, give us some feedback! We have built this platform to help buyers make decisions on their own. Any help that you can provide that allows us to reach
         that goal quickly is much appreciated.""")







