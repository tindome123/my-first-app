
import streamlit as st

st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=0.0)

vat = price * 0.07
net_price = price - vat

st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): {vat:.2f} บาท")

st.write(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("นายติณห์  ปัญญาดี เลขที่ 15 ม.4/5")
