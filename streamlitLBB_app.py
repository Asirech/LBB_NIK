
# import package
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

# --- READ DATA ---
customer_pkl = pd.read_pickle('customer_dash.pkl')

 
# --- ROW 1 ---
st.write('# Financial Portrait Dashboard')
st.write("""Discovering and Understanding Intriguing Patterns within the Financial Behavior.""")




# --- ROW 2 ---
col1, col2 = st.columns(2)
# -- PIE PLOT ---
#data plot pie
profession = pd.crosstab(index = "Number of People",
            columns = customer_pkl['Profession'],
               aggfunc= 'count',
               values = customer_pkl['NIK']
             

).transpose().reset_index()

# plot pie
plot_pie = px.pie(data_frame = profession,
                  names = 'Profession',
                  values = 'Number of People',
                  color_discrete_sequence=px.colors.sequential.RdBu)
col1.write('### Customer Count per Profession')
col1.plotly_chart(
  plot_pie,use_container_width=True  
)





# --- ROW 3 --
# -- SCATTER PLOT --

# data plot scatter
med_inc = pd.crosstab(index = "Med Income",
            columns = customer_pkl['Profession'],
               aggfunc= 'median',
               values = customer_pkl['Annual_Income']
             

).transpose().reset_index()

med_score = pd.crosstab(index = "Med Score",
            columns = customer_pkl['Profession'],
               aggfunc= 'median',
               values = customer_pkl['Spending_Score']
             

).transpose().reset_index().round()

merge_1 = med_inc.merge(right=med_score, on="Profession")

plot_scatter = px.scatter(data_frame=merge_1, 
                          x = 'Med Income',
                          y = "Med Score",
                          size = 'Med Income',
                          color = 'Profession' )

col2.write('### Relationship between Spending Score and Annual Income')
col2.plotly_chart(
  plot_scatter,use_container_width=True  )


# -- ROW 4 --
col3, col4 = st.columns(2)



## --- INPUT SLIDER --

#input_slider = col3.slider(
 #   label = 'Select Income Range',
  #  min_value = merge_1['Med Income'].min(),
   # max_value = merge_1['Med Income'].max(),
    #value=[0.00,113034000.00]
#)

#min_slider = input_slider[0]
#max_slider = input_slider[1]

#input_slider = col4.slider(
    #label = 'Select Income Range',
    #min_value = customer_pkl['Annual_Income'].min(),
    #max_value = customer_pkl['Annual_Income'].max(),
    #value=[0,1000000000]
#)

#min_slider = input_slider[0]
#max_slider = input_slider[1]



# --- HISTOGRAM PLOT ---

# plot Histogram

plot_hist = px.histogram(merge_1, x="Med Income", y="Med Score", color="Profession",
                   #marginal="box", # or violin, rug
                   hover_data= merge_1.columns)

col3.write('### Distribution of Annual Income and Spending Score')
col3.plotly_chart(
  plot_hist,use_container_width=True  )

# --- BOXPLOT ---

plot_box = px.box(customer_pkl, x="Profession", y="Spending_Score", points="all",color = "Profession",
             labels={"Spending Score": "Score", "Profession": "Occupation"})

col4.write('### Distribution of Spending Score, Annual Income, and Total Family Across Different Professions')
col4.plotly_chart(
  plot_box,use_container_width=True  )

