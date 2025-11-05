# import liblary
import streamlit as st

# Text element
# header - buat header

st.header("INI HEADER") # MEMBUAT HEADER
st.subheader("INI SUBHEADER") # MEMBUAT SUBHEADER
st.text("INI TEXT BIASA MOTHERFATHER") # MEMBUAT TEXT BIASA
st.markdown("**ini teks bold** dan *ini italic*") # MEMBUAT MARKDOWN UNTUK FORMAT TEXT
st.markdown("""
            - ini baris 1
            - ini baris 2
            - ini baris 3
""")
st.caption("ini caption") # MEMBUAT CAPTION(TEXT KECIL DIBAWAH ELEMEN UNTUK PENJELASAN)
st.title("INI TITLE") #MEMBUAT TITLE


st.title("Praktikum 01 - VisDat")
st.caption("1-text-elements")
st.markdown("""
            - KAYS ELHAQ RABBANI - 0110222218
            - AHMAD FAUZI NUGROHO - 0110222293
            - MUHAMMAD AL FARUQ - 0110122057
""")

st.title("DISPLAYING LATEX")
st.latex(r''' \cos^2\theta = 1-2\\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + a^2 + 2ab ''')


st.header("DISPLAYING CODE")
st.subheader("PYTHON CODE")

code = ''' 
def hello():
    print("HELLO STREAMLIT FROM PYTHON")
'''

st.code(code, language='python')


st.subheader("JAVE CODE")
st.code("""
public class GFG {
        public static void main(String arg[]) {
        System.out.printIn("HELLO STRIMLIT FROM JAVA);
        }
}
""", language='java')

st.subheader("JS CODE")
st.code("""
<p id = "demo"></p>
<script>
try {
    addalert("HELLO STREAMLIT FROM JS");
}
catch(err) {
        document.getElementById("demo").innerHTML = err.message;
}        
</script>       
""", language='javascript')