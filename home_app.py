import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


def run_home_app():
    st.title('당뇨병을 예측하는 앱')
    st.write('왼쪽의 사이드바에서 선택하세요')
    st.image('https://t1.daumcdn.net/cfile/tistory/9937FB335A1369DE2E')