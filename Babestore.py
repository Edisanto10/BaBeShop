from typing import cast
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image 

#1. as sidebar menu
with st.sidebar:
    choose=option_menu("Menu Utama",["Home", "Pembelian", "Pembayaran", "Contact Person", "About Us"], 
        icons=["House", ""],
    )

if choose == "Home": 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("BABE SHOP")
        st.caption("Website pembelian barang bekas murah dengan kualitas tinggi yang menawarkan berbagai macam kategori seperti buku, fashion, dan alat rumah tangga.")
        
    with col2:
        st.write(" ")
    with col3:
        st.image("logo.jpg")
        st.write(" ")
    def garis():
        st.write("-------------------------------------------------------------------")
    garis()

    st.title('List Nama Barang')
    st.image('https://th.bing.com/th/id/OIP.J03IYeDXNR5EqeUwsyijMwHaHa?pid=ImgDet&rs=1')

    st.header('Kipas Angin Kecil')
    st.subheader('Rp50.000')
    st.text('Kode Barang: 001')

    st.image('https://cf.shopee.co.id/file/75c57011a438d537be15e154f6905ff2')

    st.header('Rak Sepatu')
    st.subheader('Rp15.000')
    st.text('Kode Barang: 002')

    st.image('https://th.bing.com/th/id/OIP.RiBXojyJQZem4OwURHgybgHaHa?pid=ImgDet&rs=1')

    st.header('Galon')
    st.subheader('Rp20.000')
    st.text('Kode Barang: 003')

    st.image('https://5.imimg.com/data5/SELLER/Default/2020/10/ZP/NV/JW/25352026/img-9179-500x500.JPG')

    st.header('Meja Belajar Kecil')
    st.subheader('Rp30.000')
    st.text('Kode Barang: 004')

    st.image('https://th.bing.com/th/id/R.8c057d75eed9f019e3b9aff6f58a8076?rik=v2gWerYMyRdp1Q&riu=http%3a%2f%2ffaizzamzami.staff.ugm.ac.id%2ffiles%2f2016%2f04%2fbuku-SIA.jpg&ehk=KSTvi%2ftDqyWBr%2bLq0GoV9IocU0F67PKnWuBtAlvwI6I%3d&risl=&pid=ImgRaw&r=0')

    st.header('Buku Sistem Informasi Akuntansi')
    st.subheader('Rp35.000')
    st.text('Kode Barang: 005')

    st.image('https://images.wowcher.co.uk/images/deal/16438787/777x520/669281.jpg')

    st.header('Hanger')
    st.subheader('Rp3.000')
    st.text('Kode Barang: 006')

    st.image('https://www.jakartanotebook.com/images/products/103/1020/46687/134/bkz-hanger-gantungan-baju-rak-lemari-pipa-anti-slip-150x110x40cm-hkg122-matte-black-1.jpg')

    st.header('Rak Gantungan Baju')
    st.subheader('Rp40.000')
    st.text('Kode Barang: 007')

    st.image('https://lh5.googleusercontent.com/proxy/MYe6uv5w85nOT8O4jqwXNiLrAvDzF6kA04KStuxOclx5ha4z81mtuKVaFcdfmpmYyO_DA0mnDoqertRAr58VpeiXAenC05U1bq_kEV3Wzf6TiY4=s0-d')

    st.header('Kemeja Flanel')
    st.subheader('Rp20.000')
    st.text('Kode Barang: 008')

    st.image('https://cf.shopee.sg/file/c14e69bf2aa24f36548b9393386d7ea2')

    st.header('Rice Cooker Kecil')
    st.subheader('Rp85.000')
    st.text('Kode Barang: 009')

    st.image('https://ecs7.tokopedia.net/img/cache/700/product-1/2020/1/11/6387576/6387576_fc8c0d3c-2623-49c5-a5de-cff2157f6512_640_640.jpg')

    st.header('Stop Kontak Kabel')
    st.subheader('Rp10.000')
    st.text('Kode Barang: 010')

    st.image('https://www.static-src.com/wcsstore/Indraprastha/images/catalog/medium/93/MTA-7071824/oem_jemuran_handuk_alumunium_full02_jxhq5pkr.jpg')

    st.header('Jemuran Handuk Kecil')
    st.subheader('Rp50.000')
    st.text('Kode Barang: 011')
    def garis():
        st.write("-------------------------------------------------------------------")
    garis()

if choose == "Pembelian":
    st.subheader("Masukkan Data Diri Anda")

    Nama =st.text_input("Nama Pembeli : ")
    Nomor =st.text_input("Nomor Telepon : ")
    Jumlah =st.number_input("Jumlah Barang Yang Dibeli : ",0)
    Kode =st.text_input("Kode Barang : ")
    Barang = []
    Harga = []
    while Kode :
        if Kode=="001":
            Barang.append("Kipas Angin")
            Harga = int(50000)
            break
        elif Kode=="002":
            Barang.append("Rak Sepatu")
            Harga = int(15000)
            break
        elif Kode=="003":
            Barang.append("Galon")
            Harga = int(20000)
            break
        elif Kode=="004":
            Barang.append("Meja Belajar")
            Harga = int(30000)
            break
        elif Kode=="005":
            Barang.append("Buku")
            Harga = int(35000)
            break
        elif Kode=="006":
            Barang.append("Hanger")
            Harga = int(3000)
            break
        elif Kode=="007":
            Barang.append("Rak Gantumg")
            Harga = int(40000)
            break
        elif Kode=="008":
            Barang.append("Baju")
            Harga = int(20000)
            break
        elif Kode=="009":
            Barang.append("Rice Cooker")
            Harga = int(85000)
            break
        elif Kode=="010":
            Barang.append("Kabel Roll")
            Harga = int(10000)
            break
        elif Kode=="011":
            Barang.append("Jemuran Kecil")
            Harga = int(50000)
            break
        else :
            Kode=st.text_input("Kode salah, Masukkan Ulang Kode Barang : ")
            
    Total = (Jumlah*Harga)
        
    Pembayaran = st.button("Total Pembayaran")
    if Pembayaran:
        st.write("Nama Pembeli :", Nama)
        st.write("No Telepon :", Nomor)
        st.write("Kode Barang :", Kode)
        st.write("Jumlah Pembayaran : Rp",round(Total))

if choose == "Pembayaran":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("PEMBAYARAN")

    with col2:
        st.write("")
    st.header("Tempat Pembayaran")
    st.image("sopipay.jpg")
    st.image("dana.jpg")

    with col3:
        st.write("")

    st.header("Silahkan Konfirmasi Pembayaran Dengan Link Di Bawah Ini")
    st.subheader("https://forms.gle/JAK81dWHbaWBjPcK8")

if choose == "Contact Person":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.header('Ada Yang Bisa Kami Bantu?')
    with col3:
        st.write("")
        
    st.image("contact us.jpg")

if choose == "About Us":
    col1, col2 = st.columns(2)
    with col1:
        st.title("ABOUT US")
    with col2:
        st.write("")
    st.image("about us.png")