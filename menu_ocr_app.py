import pandas as pd
import streamlit as st

# Funktion zur HTML-Generierung
def generate_html(menu_df):
    html_output = ""
    for _, row in menu_df.iterrows():
        html_output += f"""
<div class="ux_input_container enabledForNewsletter loadingUxeId" data-type="menuDish">
    <div class="ux_input_container_fields">
        <input type="text" class="text uxe_translationField" name="titleText" value="{row['Name']}">
        <input type="number" class="text uxe_translationField" name="price" value="{row['Preis']}">
        <textarea class="text uxe_translationField" name="text" rows="4">{row['Beschreibung']}</textarea>
    </div>
</div>
"""
    return html_output

# Streamlit-Web-App
st.title("Restaurant-Menü HTML-Generator")

# Tabelle hochladen
uploaded_file = st.file_uploader(
    "Lade eine CSV-Datei mit Menü-Daten hoch",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # CSV-Datei einlesen (Preis als String behandeln)
        menu_df = pd.read_csv(uploaded_file, sep=',', quotechar='"', dtype={"Preis": str})
        
        # Überprüfen, ob die erforderlichen Spalten vorhanden sind
        required_columns = ["Name", "Beschreibung", "Preis"]
        if all(column in menu_df.columns for column in required_columns):
            # Extrahierte Daten anzeigen
            st.subheader("Hochgeladene Menü-Daten")
            st.dataframe(menu_df)
            
            # HTML-Code generieren und anzeigen
            st.subheader("Generierter HTML-Code für jedes Gericht")
            html_output = generate_html(menu_df)
            st.code(html_output, language='html')
        else:
            st.error("Die CSV-Datei muss die Spalten 'Name', 'Beschreibung' und 'Preis' enthalten.")
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Lesen der CSV-Datei: {e}")