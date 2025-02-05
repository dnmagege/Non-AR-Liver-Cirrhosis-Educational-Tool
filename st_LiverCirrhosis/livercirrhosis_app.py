import openai
import streamlit as st
#import pyttsx3
from io import BytesIO

from pathlib import Path

# Text-to-Speech Function
def text_to_speech(file_path):
    with open(file_path, "rb") as audio_file:
        return audio_file.read()

# Set your OpenAI API key
openai.api_key = "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"

# Page Content with Embeds for 3D Models, 2D Images, and Videos
content = {

     "Home": {
        "description": """
        Welcome to the Liver Cirrhosis Educational Tool!

        This tool provides a comprehensive guide on liver health, including the stages and complications of liver cirrhosis, fatty liver disease, and fibrosis.
        The tool also features 3D interactive models, 2D images, and a chatbot to answer your liver-related questions.

        Whether you are a patient, student, or healthcare professional, this tool is designed to help you better understand liver health and associated conditions. Explore the pages to learn more!
        """,
        "video": "st_LiverCirrhosis/media/liver-cirrhosis.mp4",  
        "audio": "st_LiverCirrhosis/audio/welcome.mp3",
         

    },
    
    
    "Healthy Liver": {
        "description": """
        
        The liver is like the body’s superhero, as it operates backstage and works for keeping you alive and healthy. It performs an array of tasks from system detoxification to the generation of digestive-friendly bile, storage, and regulation of energy levels, and hormone control.
        
        It is, in addition, one of the very few organs in the body that can rejuvenate on their own. A healthy liver performs so many life-carrying functions within the body, from immunity to blood clotting - in other words, a happy liver equates to a happy body.
        
        However, not all livers stay healthy. Liver cirrhosis is a disease of progressive deterioration of the liver due to long-term damage. In advanced stages, cirrhosis may lead to liver failure or even liver cancer and is capable of causing death. A liver transplant is very often the only curative option at this stage for most people.
        
        Fortunately, lifestyle changes and certain medications can help slow the progression of cirrhosis in some people and even reverse a part of the damage in some. It is very critical to take proper steps toward protection and care for one's liver, so it continues being the superhero of the body.
        """,
        "3d_model": """
        <iframe title="Healthy Liver" frameborder="0" 
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
        allow="autoplay; fullscreen; xr-spatial-tracking" 
        src="https://sketchfab.com/models/6c4e9bd0d49f4828b804259330c0c6c4/embed" 
        style="width: 100%; height: 500px;">
        </iframe>
        """,  
        "audio": "st_LiverCirrhosis/audio/slide1.mp3"  
    },
    "Liver Cirrhosis": {
        "description": """
        
        Liver cirrhosis is a condition in which the liver is damaged to the extent that scar tissue replaces the healthy tissues. Think of it as a factory in which the machines break down and, in turn, get replaced by pieces that just don't work.
        
        This buildup of scar tissue in the liver makes it harder and harder for the liver to perform its functions, whether it is filtering toxins from the blood or digesting nutrients. This might lead to all sorts of complications and might even affect the functioning of the liver if not checked. Causes usually include chronic alcohol intake, fatty liver diseases, and hepatitis infection.
        
        External Appearance: The cirrhotic liver is shrunken, coarse, and nodular, due to extensive scarring. The outer layer is rough and might be covered with bumps rose by the occurrence of regenerative nodules surrounded by fibrotic tissue.
        
        Internal Changes: Healthy, smooth liver tissue is replaced with fibrous scar tissue. Blood flow through the liver outflows and leads to portal hypertension-high pressure in the liver blood vessels.
        
        Color: The liver may appear dull and pale or yellowish or greenish, depending on the degree of impairment of bile flow, particularly in advanced cases.
        """,
        "3d_model": """
        <iframe title="Cirrhotic Liver" frameborder="0" 
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
        allow="autoplay; fullscreen; xr-spatial-tracking" 
        src="https://sketchfab.com/models/8764f9fd638448d1ab8fece4081c0cab/embed" 
        style="width: 100%; height: 500px;">
        </iframe>
        """,  
        "audio": "st_LiverCirrhosis/audio/slide2.mp3"  
    },
    "Symptoms of Liver Cirrhosis and Complications": {
        "description": """

        1. Fatigue and Weakness: This is poor nutrient processing and it occurs when there is accumulation of wastes in the body.

        2. Loss of Appetite and Weight: This is generally associated with nausea or vomiting.

        3. Yellow skin and eyes (jaundice): This is when liver is unable to process bilirubin in the way it should.

        4. Itchy skin or easy bruising: This is when the liver is less able to help the blood to clot.

        5. Cognitive Problems: Hepatic encephalopathy (accumulation of toxins in the brain) may lead to confusion and difficulties in concentration.

        6. Swelling: Fluid can build up in the abdomen (ascites) or legs (edema).

        Some complications can be quite serious, including:

        7. Bleeding in the stomach or esophagus: This is from increased pressure in the liver due to enlarged veins called varices.

        8. Predisposition to Infections: The body is more prone to infections due to a weak response from the immune system.
        """,
        "image": "st_LiverCirrhosis/media/symptoms.jpg" ,   
        "audio": "st_LiverCirrhosis/audio/slide3.mp3"  
    },
    "Stages of Cirrhosis": {
        "description": """

        1. Steatosis: This is the beginning of a fatty liver, with a gathering of fat in the liver. No symptoms usually occur during this stage.

        2. Fibrosis: Scarring of the liver has started to occur and begins to take hold, but the liver generally still functions in a relatively normal way.

        3. Compensated Cirrhosis: In this condition, the liver shows significant scarring; however, because of compensation, the liver is able to continue with its function in a relatively normal way and symptoms may be mild or even absent altogether.

        The most advanced stage is the decompensated one, and is known as:

        4. Cirrhosis: This is when the liver starts its failure. It becomes symptomatic, with symptoms such as jaundice and complications like ascites, the accumulation of fluid in the abdomen.
        """,
        "3d_model": """
        <iframe title="Fatty Liver" frameborder="0" 
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
        allow="autoplay; fullscreen; xr-spatial-tracking" 
        src="https://sketchfab.com/models/62f682fc032644e5b380d2b9af189e6e/embed?autostart=1" 
        style="width: 100%; height: 500px;">
        </iframe>
        """,  
        "audio": "st_LiverCirrhosis/audio/slide4.mp3"  
    },

    "Fatty Liver": {
        "description": """

        Fatty liver, or steatosis, is the abnormal accumulation of fat tissue within the liver cells. This represents the earliest and mildest form of the liver disorder, and for long periods, it usually doesn't cause any harm. 
        But often, it may also be a starting point that progresses via fibrosis to cirrhosis.

        The liver is enlarged with pale and greasy masses of fat.
        Microscopically, fat vacuoles accumulate inside liver cells, pushing the nucleus to the edge.

        Fatty liver may arise from the following: 

        NAFLD or Non-Alcoholic Fatty Liver Disease: It is related to obesity, high cholesterol, diabetes, and metabolic syndrome. 

        AFLD or Alcoholic Fatty Liver Disease: The causes include the intake of alcohol in large amounts. 

        Other Causes are: 

        Rapid weight loss, malnutrition, certain medications, or toxins.
        """,
        "3d_model": """
        <iframe title="Fatty Liver" frameborder="0" 
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
        allow="autoplay; fullscreen; xr-spatial-tracking" 
        src="https://sketchfab.com/models/36c7341eca9a4514be47bb240166331b/embed" 
        style="width: 100%; height: 500px;">
        </iframe>
        """,  
        "audio": "st_LiverCirrhosis/audio/slide5.mp3"  
    },
    "Fibrosis Liver": {
        "description": """

        Fibrosis refers to the scarring of liver tissue resulting from chronic injury or inflammation. While fatty liver consists mainly of an accumulation of fat, in the case of fibrosis, structural damage to the liver is depicted. 
        It means the liver is trying to heal itself but is making defective scar tissue in the process.

        The liver surface can be irregular and hard with scar tissue forming bridges between areas of liver that are still working normally. Under a microscope, collagen fibers, or scar tissue, would be seen replacing normal liver cells.

        When the liver has a chronic stress or     damage like:

        1. Progressive fatty liver, that is continuing accumulation of fat and inflammation in the liver.
        2. Chronic hepatitis B or C viruses, causing chronic inflammation in the liver.
        3. Alcohol abuse: The most common cause of liver damage.
        4. Autoimmune disorders or genetic conditions, such as hemochromatosis or Wilson's disease.
        """,
        
        "3d_model": """
        <iframe title="Fatty Liver" frameborder="0" 
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" 
        allow="autoplay; fullscreen; xr-spatial-tracking" 
        src="https://sketchfab.com/models/62f682fc032644e5b380d2b9af189e6e/embed?autostart=1" 
        style="width: 100%; height: 500px;">
        </iframe>
        """,  
        "audio": "st_LiverCirrhosis/audio/slide6.mp3"   
    },
    "Causes and Risk Factors": {
        "description": """

        1. Alcohol Abuse: Excessive drinking over a long period of time is one of the most common causes of liver damage.

        2. Nonalcoholic Fatty Liver Disease (NAFLD): Generally related to either obesity or diabetes, the condition is now gaining immense popularity.

        3. Chronic Hepatitis B or C: If these infections are not cleared, they can cause chronic inflammation that leads to scarring and progressive liver damage.

        4. Toxins or Medication: There are some drugs and toxins that have a toxic effect on the liver after certain exposure.

        5. Genetics: Some conditions, such as hemochromatosis, which leads to a buildup of iron, and Wilson's disease, caused by copper accumulation, run in the family and affect the liver.
        """,
        "image": "st_LiverCirrhosis/media/Cirrhosis-risk-factors.jpeg",
        "audio": "st_LiverCirrhosis/audio/slide7.mp3" 
    },
    "Conventional Treatments": {
        "description": """

        1. Lifestyle changes: This means cessation of alcohol completely, nutrition-rich diet, and weight management.

        2. Medication: It includes diuretics to reduce water accumulation, antibiotics if infected, or lactulose to clear the toxins that lead to brain malfunctioning.

        3. Procedures: If complications arise, like varices (enlarged veins that might bleed), treatments like banding or other surgical interventions could be needed.

        4. Liver transplant: This may be the only option when the liver is too damaged to function.
        """,
        "image": "st_LiverCirrhosis/media/liverdiagram.png",  
        "audio": "st_LiverCirrhosis/audio/slide7.mp3" 
    },
    "Coping with Cirrhosis Naturally": {
        "description": """

        While medical treatment is essential, there are also natural approaches to help manage the condition and support your liver:

        1. Eat a liver-friendly diet: Focus on whole foods, lots of fruits and veggies, and avoid processed junk.

        2. Stay hydrated: Drinking enough water helps your liver do its detoxing job.

        3. Get moving: Regular exercise can help improve overall health and reduce fat in the liver.

        4. Try stress management: Practices like yoga, meditation, or even simple deep breathing can reduce stress, which is great for overall health.

        5. Use herbal remedies wisely: Supplements like milk thistle may help, but always check with your doctor first.

        6. Limit toxins: Avoid harsh chemicals, pesticides, or smoking.

        7. Get good sleep: Your body, including your liver, heals best when you’re well-rested.

        8. Find support: Whether it’s a therapist, a support group, or a close friend, having someone to lean on can make a big difference.
        """,
        "image": "st_LiverCirrhosis/media/liver.jpg",  
        "audio": "st_LiverCirrhosis/audio/slide8.mp3" 
    },
    "Liver Cirrhosis Chatbot": {},
    
}

# Sidebar Navigation
st.sidebar.title("Non Ar - Liver Cirrhosis Educational Tool")
pages = list(content.keys())
page = st.sidebar.radio("Select a page:", pages)

# Display Content for Each Page
if page != "Liver Cirrhosis Chatbot":
    st.title(page)
    st.write(content[page]["description"])

    # Play Audio if Available
    if "audio" in content[page]:
        audio_path = content[page]["audio"]
        if Path(audio_path).exists():
            st.audio(text_to_speech(audio_path), format="st_LiverCirrhosis/audio/mp3")
        else:
            st.error(f"Audio file not found: {audio_path}")

    # # Auto-Play Audio if Available
    # if "audio" in content[page]:
    #     audio_path = content[page]["audio"]
    #     if Path(audio_path).exists():
    #         st.components.v1.html(f"""
    #         <audio autoplay>
    #             <source src="{audio_path}" type="st_LiverCirrhosis/audio/mpeg">
    #             Your browser does not support the audio element.
    #         </audio>
    #         """, height=50)
    #     else:
    #         st.error(f"Audio file not found: {audio_path}")


    # Display Video (if available)
    if "video" in content[page]:
        st.video(content[page]["video"])

    # Display Image (if available)
    if "image" in content[page]:
        st.image(content[page]["image"], use_container_width=True)

    # Display 3D Model (if available)
    if "3d_model" in content[page]:
        st.components.v1.html(content[page]["3d_model"], height=600)

    # if "description" in content[page]:
    #     st.write(content[page]["description"])
        
else:
    # Chatbot Page
    st.title("I am your tool assistant.")
    

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # User Input
    user_input = st.text_input("Ask me anything about liver cirrhosis")
    if st.button("Send"):
        if user_input:
            # Add the user's input to the chat history
            st.session_state["messages"].append({"role": "user", "content": user_input})

            # Call OpenAI API to get a response
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Use the ChatGPT model
                    messages=st.session_state["messages"]
                )
                bot_response = response["choices"][0]["message"]["content"].strip()

                # Add the bot's response to the chat history
                st.session_state["messages"].append({"role": "assistant", "content": bot_response})
            except Exception as e:
                bot_response = f"Error: {str(e)}"
                st.session_state["messages"].append({"role": "assistant", "content": bot_response})

    # Display Chat Messages
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Liver Assistant:** {msg['content']}")
