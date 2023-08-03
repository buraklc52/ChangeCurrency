import streamlit as st
from urllib.request import urlopen
import xml.etree.ElementTree as et

link="https://www.tcmb.gov.tr/kurlar/today.xml"
xml=et.ElementTree(file=urlopen(link))

root=xml.getroot()

kurlar = {}
for cur in root:
    kurlar[cur[1].text] = float(cur[3].text)
kurlar["Türk Lirası"]=1

veriler = []
for cur in root:
    s = {}
    if cur.attrib['Kod']!="XDR":
        s["kod"] = cur.attrib["Kod"]
        s["isim"] = cur[1].text
        s["alis"] = float(cur[3].text)
        s["satis"] = float(cur[4].text)
        veriler.append(s)

kur1 = st.selectbox("Elinizdeki Kur:",list(kurlar.keys()))
miktar = st.number_input("Elinizdeki Miktar")
kur2 = st.selectbox("Hedef Kur:",list(kurlar.keys()))

sonuc = kurlar[kur1] / kurlar[kur2] * miktar

st.write(sonuc,kur2)

st.table(veriler)