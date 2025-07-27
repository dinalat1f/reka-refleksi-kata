import streamlit as st

st.set_page_config(page_title="REKA – Refleksi Kata", layout="centered")

st.markdown(
    """
    <div style='text-align: center; padding: 2rem; background-color: #f5f1eb; border-radius: 15px;'>
        <h1 style='color: #5d473a;'>REKA</h1>
        <h3 style='color: #7a6655;'>Refleksi Kata</h3>
        <p style='color: #5d473a; font-size: 1.2rem;'>
            “Tempat di mana setiap kata menjadi cermin kecil untuk mengenali diri sendiri.”
        </p>
        <p style='margin-top: 2rem; font-size: 1rem; color: #7a6655;'>
            Oleh Ardina Latif
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.set_page_config(page_title="REKA Chat", layout="wide")
st.title("REKA – Ruang Refleksi Karakter")

# Chat Input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ketik di sini...")

if user_input:
    st.session_state.chat_history.append(("Kamu", user_input))
    
    # Jawaban sederhana (simulasi)
    if "insecure" in user_input.lower():
        balasan = "Ingat ya, kamu berharga bukan karena pencapaianmu, tapi karena kamu adalah kamu."
    else:
        balasan = "Terima kasih sudah bercerita. Kamu tidak sendiri."

    st.session_state.chat_history.append(("REKA", balasan))

# Tampilkan riwayat chat
for sender, msg in st.session_state.chat_history:
    if sender == "Kamu":
        st.markdown(f"**🧍 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="REKA – Refleksi Afirmasi", layout="centered")

# Load Model
@st.cache_resource
def load_model():
    generator = pipeline("text-generation", model="cahya/gpt2-small-indonesian")
    set_seed(42)
    return generator

generator = load_model()

# Fungsi membuat prompt reflektif berdasarkan tema
def buat_prompt(tema, input_user):
    tema = tema.lower()
    return f"Buat afirmasi positif dan reflektif bertema {tema} untuk seseorang yang berkata: \"{input_user}\".\nAfirmasi:"

# UI
st.markdown("<h1 style='text-align:center;'>REKA 🤍</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Refleksi Karakter dan Kata</h4>", unsafe_allow_html=True)

st.markdown("---")

# Form Input
tema = st.selectbox("Pilih Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
user_input = st.text_area("Tuliskan isi hatimu atau cerita singkatmu...")

if st.button("Refleksikan 🌿"):
    if user_input.strip() != "":
        prompt = buat_prompt(tema, user_input)
        output = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        # Potong bagian prompt supaya hanya ambil hasil afirmasinya
        afirmasi = output.replace(prompt, "").strip()

        st.markdown("### ✨ Afirmasi untukmu:")
        st.success(afirmasi)
    else:
        st.warning("Coba tuliskan sesuatu dulu, ya 🌱")
