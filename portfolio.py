import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################   02022d

side_h1 = """
    <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>Computer Vision and NLP Enthusiast </h1>
    """

st.markdown(side_h1, unsafe_allow_html=True)
image = Image.open('my_dp.png')
st.image(image, width=150)
my_name = "<h5 style = 'font-size:30px; align-items: center ; padding-top:0rem; font-color:#f9f2f2'>Yasir Ali</h5>"
st.markdown(my_name, unsafe_allow_html=True)

about_me = """"
      <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>About Me </h1>
"""
st.markdown(about_me, unsafe_allow_html=True)
st.info('''
- Experienced  as an artifical intelligence students  with more then two years of experienced in the domain of computer vision and natural language processing.   
- Strong verbal and written communication skills as demonstrated .
- worked on more then 5 research paper in the domain of computer vision.
- Currently working on Building real word NLp Tools 
- Strongly Motivated to work in the feild of Artifical intelligence.

''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #004953;">
  <a class="navbar-brand" href="https://www.youtube.com/channel/UCDTpeI7tkSctedh1IXVZaRw" target="_blank">Ai Vision </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/" style='color: #fcfcfd;font-size:18px;'>Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education" style='color: #fcfcfd;font-size:18px;' >Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience" style='color: #fcfcfd;font-size:20px;'>Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects" style='color: #fcfcfd;font-size:20px;'>Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media" style='color: #fcfcfd;font-size:20px;'>Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
edu_head = """
            <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>Education</h1>

           """
st.markdown(edu_head, unsafe_allow_html=True)

txt('**Bachelor Degree** (Mechatronics Engineering), *Mehran University*, Pakistan',
    '2020-2023')

#####################

work_exp_head = """ 
                    <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>Work Experience</h1>

                    """
st.markdown(work_exp_head, unsafe_allow_html=True)

# txt('**Fiver and Upwork**',
#     '2021-2023')


txt3('**Computer Vision:**',
     'I am experience in developing computer vision algorithms and systems for tasks such as object `detection and recognition`, `image segmentation`, and `facial recognition`.')
txt3('**YOLO object detection:**',
     'I am  experience in using the `YOLO (You Only Look Once)` algorithm for object detection and `classification`, and have experience in `training models` for specific object detection tasks.')
txt3('**Natural Language Processing:**',
     'I am  experience in developing natural language processing `(NLP) systems`, including tasks such as `text classification`, sentiment analysis, and `language translation.`')
txt3('**Unity:**',
     'I am  experience in using the Unity game engine to develop 3D games and interactive experiences, and have experience in developing `VR and AR applications` using Unity.')
txt3('**AR and VR:**',
     'I am  experience in developing augmented reality `(AR) and virtual reality (VR) applications` for a variety of platforms, including mobile devices and head-mounted displays.')
txt3('**Research Work Entitled:**', 'Heart Diseases Classification using Computer Vision.')
txt3('**Currently:**',
     'working on the solution making Ai games with unity |Influencer YOLO | Object detection and segmentation, image classification | Robotics | Natural Language processing')

#####################
Project_Head = """ 
                    <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>Projects</h1>

                    """
st.markdown(Project_Head, unsafe_allow_html=True)

txt4('Helmet-detection', 'Real time Helmet detection using yolov5 ',
     'https://github.com/yasirrustam06/HelmetDetection-usingYolov5')
txt4('text-to-speech', 'A complete text to Speech application', 'https://youtu.be/anzYz1L_I4Q')
txt4('Track-and-count-objects', 'Track and count objects with the help of yolov8 object detection',
     'https://youtu.be/zI8cZB-FTGM')
txt4('Face Mask detection', 'Face mask Detection in real time',
     'https://github.com/yasirrustam06/yolov5-FaceMask-Detection_inRealtime')
txt4('Face detection web-app', 'Complete face detection web app with streamlit',
     'https://github.com/yasirrustam06/face_detection_web_app')
txt4('YOLOv8_DeepSORT_TRACKING', 'Ylolov8 Deepsort tracking ',
     'https://github.com/yasirrustam06/YOLOv8_DeepSORT_TRACKING')
txt4('Object Recongnition with BOW', 'Object Recongnition with Bag of words ',
     'https://github.com/yasirrustam06/Object-recongnition-with-BOVW-')

#####################
pakages_heading = """ 
                    <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2;'>My Experienced Python Packages</h1>

                    """
st.markdown(pakages_heading, unsafe_allow_html=True)

txt3('**Natural language processing:**', '`NLTK`,`Spacy`,`openai`,`Hugging Face`,`chatbots`')
txt3('**Computer Vision:**',
     '`Opencv`,`Segmentation`,`Object detection`,`Yolo(you only look at once)`,`object Recongnition`')
txt3('**Programming:**', '`Python`, `R`, `Linux`')
txt3('**Data processing/wrangling:**', '`SQL`, `pandas`, `numpy`')
txt3('**Data visualization:**', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('**Machine Learning:**', '`scikit-learn` ,`pandas`')
txt3('**Deep Learning:**', '`TensorFlow` `Pytorch`')
txt3('**Web development:**', '`Flask`, `HTML`, `CSS`')
txt3('**Model deployment:**', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################

social_media_heading = """
        <h1 style='font-size:36px;font-weight:bold;border-radius:10px;color:#f9f2f2; align-items: center'>Social Media</h1>"""
st.markdown(social_media_heading, unsafe_allow_html=True)
txt2('LinkedIn', 'https://www.linkedin.com/in/yasir-ali-909600220/')
txt2('GitHub', 'https://github.com/yasirrustam06')
txt2('Kaggle', 'https://www.kaggle.com/yasir006')

txt2('Facebook', 'https://www.facebook.com/profile.php?id=100089380927093')
txt2('Youtube', 'https://www.youtube.com/channel/UCDTpeI7tkSctedh1IXVZaRw')
