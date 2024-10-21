import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64


# Function to convert a font file to base64
def get_base64_of_font(font_path):
    with open(font_path, "rb") as font_file:
        return base64.b64encode(font_file.read()).decode()


# Function to convert an image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Convert the font file to base64
font_base64 = get_base64_of_font("fonts/1942.ttf")

# Inject the font via base64 in CSS
st.markdown(f"""
    <style>
    @font-face {{
        font-family: '1942Report';
        src: url(data:font/ttf;base64,{font_base64}) format('truetype');
    }}

    .a:link, .a:visited {{
      background-color: #84A59D;
      color: #F2E8CF;
      padding: 14px 25px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      width: 100%;
    }}

    .a:hover, a:active {{
      background-color: #5D847A;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: #3B524C !important;
    }}

    .image-container {{
        position: relative;
        width: 100%;
        max-width: 100%;
        text-align: center;
        color: white;
    }}

    .centered-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 90px;
        font-weight: bold;
        color: #F7EDE2;
        font-family: '1942Report', sans-serif; /* Apply the custom font */
    }}

    </style>
    """, unsafe_allow_html=True)

# Chemin vers le fichier Excel
file_path = './new/dataset_frequence_cine.xlsx'

# Chargement et nettoyage de la feuille 'mois'
df_mois_clean = pd.read_excel(file_path, sheet_name='mois', skiprows=6, nrows=45)
df_mois_clean.rename(columns={
    df_mois_clean.columns[0]: 'Years',
    df_mois_clean.columns[1]: 'January',
    df_mois_clean.columns[2]: 'February',
    df_mois_clean.columns[3]: 'March',
    df_mois_clean.columns[4]: 'April',
    df_mois_clean.columns[5]: 'May',
    df_mois_clean.columns[6]: 'June',
    df_mois_clean.columns[7]: 'July',
    df_mois_clean.columns[8]: 'August',
    df_mois_clean.columns[9]: 'September',
    df_mois_clean.columns[10]: 'October',
    df_mois_clean.columns[11]: 'November',
    df_mois_clean.columns[12]: 'December',
    df_mois_clean.columns[13]: 'Total'
}, inplace=True)

# Chargement et nettoyage de la feuille 'freqciné'
df_freqcine_clean = pd.read_excel(file_path, sheet_name='freqciné', skiprows=50, nrows=45)
df_freqcine_clean.rename(columns={
    df_freqcine_clean.columns[0]: 'Years',
    df_freqcine_clean.columns[1]: 'Sessions (thousands)',
    df_freqcine_clean.columns[2]: 'Entries (millions)',
    df_freqcine_clean.columns[3]: 'Box office (M€ current)',
    df_freqcine_clean.columns[4]: 'Average revenue per entry (€)'
}, inplace=True)
df_freqcine_clean.replace('-', np.nan, inplace=True)

# Chargement et nettoyage de la feuille 'entrées ff'
df_entrees_ff_clean = pd.read_excel(file_path, sheet_name='entrées ff', skiprows=6, nrows=33)
df_entrees_ff_clean.rename(columns={
    df_entrees_ff_clean.columns[0]: 'Years',
    df_entrees_ff_clean.columns[1]: 'More than 2 million entries',
    df_entrees_ff_clean.columns[2]: '1 to 2 million entries',
    df_entrees_ff_clean.columns[3]: '500,000 to 1 million entries',
    df_entrees_ff_clean.columns[4]: '200,000 to 500,000 entries',
    df_entrees_ff_clean.columns[5]: '100,000 to 200,000 entries',
    df_entrees_ff_clean.columns[6]: '50,000 to 100,000 entries',
    df_entrees_ff_clean.columns[7]: 'Less than 50,000 entries',
    df_entrees_ff_clean.columns[8]: 'Total'
}, inplace=True)

# Convert the image to base64
image_path = "file/cinema.webp"
image_base64 = get_base64_of_image(image_path)

# Display the image with centered text
st.markdown(f"""
        <div class="image-container">
            <img src="data:image/png;base64,{image_base64}">
            <div class="centered-text">
                Movie attendance
            </div>
        </div><br>
    """, unsafe_allow_html=True)


# Display heads of dataframes
with st.expander(f"First lines of the dataframe we are going to use:", expanded=False):
    st.write("Monthly attendance:")
    st.dataframe(df_mois_clean.head(10))

    st.write("Cinema attendance (all programs: feature films, short films, and non-film content):")
    st.dataframe(df_freqcine_clean.head(10))

    st.write("French films in theaters based on their number of admissions:")
    st.dataframe(df_entrees_ff_clean.head(10))

st.markdown('## **Revenue vs Year: Impact of Average Revenue per Entry**')

custom_colors = ['#F7EDE2', '#F5CAC3', '#F28482']

fig = px.scatter(df_freqcine_clean,
                 x='Years',
                 y='Box office (M€ current)',
                 color='Average revenue per entry (€)',
                 labels={
                     'Years': 'Years',
                     'Box office (M€ current)': 'Receipt counter (current M€)',
                     'color': 'Average revenue per entry (€)'
                 },
                 color_continuous_scale=custom_colors)

fig.update_xaxes(range=[df_freqcine_clean['Years'].min(), df_freqcine_clean['Years'].max()])
fig.update_traces(marker=dict(size=10))
st.plotly_chart(fig)


years_of_interest = [1980, 1990, 2000, 2010, 2020, 2023]
filtered_data = df_mois_clean[df_mois_clean['Years'].isin(years_of_interest)]

filtered_data = filtered_data.replace('-', pd.NA).astype(float)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

scatter_data = pd.melt(
    filtered_data,
    id_vars=['Years'],
    value_vars=months,
    var_name='Months',
    value_name='Monthly average'
)

custom_colors = ['#F28482', '#84A59D', '#F6BD60', '#C7B8A8', '#F5CAC3', '#C2837A']

st.markdown('## **Monthly averages attendance of decade**')
fig = px.line(
    scatter_data,
    x='Months',
    y='Monthly average',
    color='Years',
    markers=True,
    color_discrete_sequence=custom_colors,
    labels={'Monthly average': 'Monthly average', 'Months': 'Months'}
)
st.plotly_chart(fig)


st.markdown('## **Income by Years**')
tab1, tab2 = st.tabs(["Total", "Average"])

df_mois_revenu = pd.read_excel(file_path, sheet_name='mois', skiprows=53, nrows=45)
df_mois_revenu.rename(columns={
    df_mois_revenu.columns[0]: 'Years',
    df_mois_revenu.columns[1]: 'January',
    df_mois_revenu.columns[2]: 'February',
    df_mois_revenu.columns[3]: 'March',
    df_mois_revenu.columns[4]: 'April',
    df_mois_revenu.columns[5]: 'May',
    df_mois_revenu.columns[6]: 'June',
    df_mois_revenu.columns[7]: 'July',
    df_mois_revenu.columns[8]: 'August',
    df_mois_revenu.columns[9]: 'September',
    df_mois_revenu.columns[10]: 'October',
    df_mois_revenu.columns[11]: 'November',
    df_mois_revenu.columns[12]: 'December',
    df_mois_revenu.columns[13]: 'Total'
}, inplace=True)


months = df_mois_revenu.columns[1:-1]
df_melted = df_mois_revenu.melt(id_vars=['Years'], value_vars=months,
                                  var_name='Months', value_name='Income')

average_revenue_per_year = df_mois_revenu.drop(columns=['Total']).mean(axis=1)
df_mois_revenu['Average income'] = average_revenue_per_year

average_revenue_by_year = df_mois_revenu[['Years', 'Average income']]
# Tab 1: Display data by Years
tab1.subheader('Total income by Years')
fig_years = px.bar(df_freqcine_clean, x='Years', y='Box office (M€ current)')
fig_years.update_traces(marker_color='#F6BD60')
tab1.plotly_chart(fig_years)

# Tab 2: Display data by Months
tab2.subheader('Avery income by Years')

fig_months = px.bar(average_revenue_by_year, x='Years', y='Average income', labels={'Average income': 'Average Income (M€)', 'Years': 'Years'})
fig_months.update_traces(marker_color='#F6BD60')
tab2.plotly_chart(fig_months)

st.markdown('## **Histogram of total admissions in cinema by year for French films**')

bar_chart_data = df_entrees_ff_clean.set_index('Years')
st.bar_chart(bar_chart_data['Total'], color='#84A59D')

st.markdown('## **Number of Movies by Entries by Year**')
years = [1995, 2000, 2005, 2010, 2015, 2020, 2023]
tabs = st.tabs([str(year) for year in years])

custom_colors = ['#F28482', '#3B524C', '#84A59D', '#F6BD60', '#C7B8A8', '#F5CAC3', '#C2837A']

for i, year in enumerate(years):
    year_data = df_entrees_ff_clean[df_entrees_ff_clean['Years'] == year]

    melted_data = year_data.melt(id_vars=['Years'],
                                  value_vars=[col for col in df_entrees_ff_clean.columns if col != 'Years' and col != 'Total'],
                                  var_name='Entry Category',
                                  value_name='Number of Entries')

    fig = px.bar(melted_data,
                 x='Entry Category',
                 y='Number of Entries',
                 labels={'Number of Entries': 'Number of Movies', 'Entry Category': 'Entry Category'},
                 color='Entry Category',
                 color_discrete_sequence=custom_colors)

    tabs[i].subheader(year)
    tabs[i].plotly_chart(fig)
