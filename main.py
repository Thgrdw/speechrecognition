import streamlit as st
import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()

st.title("Program Speech Recognition")
st.sidebar.title("Kelompok 1")
with st.sidebar.expander("Anggota"):
    st.markdown("""
                Aulia Yusa            1197070016</p>
                
                Gita Destalia         1197070030</p>
                
                Kurnia Sandi          1197070042</p>
                
                Muhammada Dani A.     1197070050</p>
                
                Tegar Dwi Pangestu    1197070071</p>
                """, unsafe_allow_html=True)
st.write("Program ini dirancang untuk memudahkan pembelajaran speaking dalam bahasa Inggris agar sesuai dengan pelafalan menggunakan NLP")
with st.expander(" ✔ Klik di sini untuk info lebih lanjut tentang program ✔"):
    st.markdown("""
        <p>Program ini mengadopsi metode Neural Language Processing, yang mana membuat model speech recognition dengan input voice dan output text. 
	Tujuan program dibuat ialah untuk memudahkan pembelajaran bahasa inggris khususnya speaking agar user mengetahui apakah speakingnya sudah sesuai
	seperti native speaker, sedangkan amat jarang kita menemukan native speaker bahasa inggris di lingkungan kita sehari-hari.
	Prinsip kerjanya yaitu user akan menekan button mulai merekam dan program akan melakukan perekaman suara dengan waktu tunggu 1,8 detik (default) setelah 
	user berhenti berbicara. Selanjutnya program akan memproses input voice tersebut dan menampilkannya dalam bentuk text.
	Dalam program ini menggunakan engine recognize dari google.</p>
        <p>Kode yang digunakan untuk melatih model tersedia di <a href="https://github.com/Thgrdw/speechrecognition" target="_blank">https://github.com/Thgrdw/speechrecognition</a>.</p>
    """, unsafe_allow_html=True)
klik = st.button("Mulai merekam")
if klik:
    with mic as source:
        st.write("Silahkan Berbicara")
        rekaman = engine.listen(source)
        st.write("Waktu habis !!!!")
        
        try:
            hasil = engine.recognize_google(rekaman)
            # st.write(hasil)
            out_text = '<table><tr> <th>Hasil</th></tr>'
            out_text += '<tr>' + \
                            f'<td>{hasil}</td>' + \
                        '</tr>'
            out_text += '</table><br><br>'
            st.markdown(out_text, unsafe_allow_html=True)
        except engine.UnknownValueError:
            st.warning("Tidak dengar, ulang")
        except Exception as e:
            st.warning(e)
        out_text = '<table><tr> <th>Hasil</th> <th>hasil</th> <th>Example</th> </tr>'
