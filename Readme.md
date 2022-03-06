# Desain Pemrograman Berorientasi Objek

>Saya Cahya Gumilang (2003128) mengerjakan tugas LATIHAN4DPBO2022 dalam mata kuliah Desain dan Pemrograman Berbasis Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

Repository ini berisikan Latihan 4 pada mata kuliah Desain Pemrograman Berorientasi Objek tahun 2022. 

Modul dapat ditemukan di [Modul 4 - Multiple & Hierarchical Inheritance](https://docs.google.com/document/d/1zSLOCPvmSSnlj8vAcLW6R4KRVh9lF7K2SYfrjp04Wqc/edit#)

## Design
<p align ="center"><img src="/image/design.png"/></p>
`Ship` dam `Airplane` merupakan `Vehicle` sehingga class `Vehicle` dijadikan parent dari class `Ship` dan juga `Airplane`. Disetiap kendaraan tentunya ada pengemudi, tapi disini saya menempatkan Pengemudi di `Ship` dan `Airplane` dan tidak di `Vehicle` karena beberapa kendaraan membutuhkan jumlah pengemudi yang berbeda dan juga di setiap kendaraan pengemudi memiliki nama berbeda, misalnya pengemudi `Ship` disebut Nahkoda sedangkan pengemudi `Airplane` disebut Pilot. `Driver` merupakan `Person` dan juga `Job` sehingga class `Person` dan `Job` dijadikan parent dari class `Driver`. 

## Screenshots Program
![Latihan 4](/image/py1.png)
![Latihan 4](/image/py2.png)
![Latihan 4](/image/py3.png)
![Latihan 4](/image/py4.png)
